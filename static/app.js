const messagesEl = document.getElementById("messages");
const form = document.getElementById("chatForm");
const input = document.getElementById("messageInput");
const sendBtn = document.getElementById("sendBtn");
const reindexBtn = document.getElementById("reindexBtn");
const statusEl = document.getElementById("status");
const providerBadge = document.getElementById("providerBadge");
const marketSelect = document.getElementById("marketSelect");

/** @type {{role: string, content: string}[]} */
let history = [];
let busy = false;

const MARKET_LABELS = { uae: "UAE", omn: "OMN" };

function currentMarket() {
  return marketSelect.value === "omn" ? "omn" : "uae";
}

function setStatus(text, isError = false) {
  statusEl.textContent = text || "";
  statusEl.classList.toggle("error", Boolean(isError));
}

function ensureEmptyState() {
  if (messagesEl.children.length === 0) {
    const empty = document.createElement("div");
    empty.className = "empty";
    empty.id = "emptyState";
    empty.textContent = `Ask an RFP question about ${MARKET_LABELS[currentMarket()]} e-invoicing.`;
    messagesEl.appendChild(empty);
  }
}

function clearEmptyState() {
  const empty = document.getElementById("emptyState");
  if (empty) empty.remove();
}

function resetConversation() {
  history = [];
  messagesEl.innerHTML = "";
  ensureEmptyState();
  input.placeholder = `Ask an RFP question about ${MARKET_LABELS[currentMarket()]} e-invoicing…`;
}

function appendMessage(role, content = "") {
  clearEmptyState();
  const el = document.createElement("div");
  el.className = `message ${role}`;
  el.textContent = content;
  messagesEl.appendChild(el);
  messagesEl.scrollTop = messagesEl.scrollHeight;
  return el;
}

function renderSources(messageEl, sources) {
  if (!sources?.length) return;
  const box = document.createElement("div");
  box.className = "sources";
  const label = document.createElement("div");
  label.textContent = "Sources:";
  const list = document.createElement("ul");
  for (const source of sources) {
    const item = document.createElement("li");
    const marketPrefix = source.market ? `[${source.market}] ` : "";
    item.textContent = source.section_title
      ? `${marketPrefix}${source.path} — ${source.section_title}`
      : `${marketPrefix}${source.path}`;
    list.appendChild(item);
  }
  box.appendChild(label);
  box.appendChild(list);
  messageEl.appendChild(box);
}

function parseSse(buffer) {
  const normalized = buffer.replace(/\r\n/g, "\n").replace(/\r/g, "\n");
  const parts = normalized.split("\n\n");
  const rest = parts.pop() || "";
  const events = [];

  for (const part of parts) {
    if (!part.trim()) continue;
    let event = "message";
    const dataLines = [];
    for (const line of part.split("\n")) {
      if (line.startsWith("event:")) {
        event = line.slice(6).trim();
      } else if (line.startsWith("data:")) {
        let value = line.slice(5);
        if (value.startsWith(" ")) value = value.slice(1);
        dataLines.push(value);
      }
    }
    if (!dataLines.length) continue;
    events.push({ event, data: dataLines.join("\n") });
  }

  return { events, rest };
}

async function refreshHealth() {
  try {
    const res = await fetch("/api/health");
    const data = await res.json();
    const docs = data.document_count ?? 0;
    const counts = data.market_counts || {};
    const market = currentMarket();
    const marketDocs = (counts[market] || 0) + (counts.shared || 0);
    providerBadge.textContent = `${MARKET_LABELS[market]} · ${data.provider} · ${marketDocs}/${docs} chunks`;
    if (!data.kb_exists) {
      setStatus("Knowledge folder not found.", true);
    } else if (docs === 0) {
      setStatus("Index is empty. Click Re-index knowledge base to ingest.");
    } else if (!data.ok) {
      const err = data.provider_health?.error || "Provider not ready";
      setStatus(err, true);
    } else {
      setStatus("");
    }
  } catch (err) {
    providerBadge.textContent = "offline";
    setStatus(String(err), true);
  }
}

async function reindex() {
  if (busy) return;
  busy = true;
  reindexBtn.disabled = true;
  setStatus("Indexing knowledge base…");
  try {
    const res = await fetch("/api/ingest", { method: "POST" });
    const data = await res.json();
    if (!res.ok) {
      throw new Error(data.detail || data.message || "Ingest failed");
    }
    setStatus(data.message || "Indexed.");
    await refreshHealth();
  } catch (err) {
    setStatus(String(err.message || err), true);
  } finally {
    busy = false;
    reindexBtn.disabled = false;
  }
}

async function sendMessage(text) {
  if (busy) return;
  busy = true;
  sendBtn.disabled = true;
  setStatus("Thinking…");

  appendMessage("user", text);
  const assistantEl = appendMessage("assistant", "");
  let answer = "";
  let sources = [];

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "text/event-stream",
      },
      body: JSON.stringify({
        message: text,
        history,
        market: currentMarket(),
      }),
    });

    if (!res.ok) {
      let detail = "Chat failed";
      try {
        const errBody = await res.json();
        detail = errBody.detail || errBody.message || detail;
      } catch (_) {
        /* ignore */
      }
      throw new Error(detail);
    }

    if (!res.body) {
      throw new Error("No response body from chat API");
    }

    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";

    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });

      const parsed = parseSse(buffer);
      buffer = parsed.rest;

      for (const item of parsed.events) {
        if (item.event === "sources") {
          sources = JSON.parse(item.data);
        } else if (item.event === "token") {
          const payload = JSON.parse(item.data);
          answer += payload.text || "";
          assistantEl.textContent = answer;
          messagesEl.scrollTop = messagesEl.scrollHeight;
        } else if (item.event === "error") {
          const payload = JSON.parse(item.data);
          throw new Error(payload.message || "Stream error");
        }
      }
    }

    if (buffer.trim()) {
      const parsed = parseSse(buffer + "\n\n");
      for (const item of parsed.events) {
        if (item.event === "sources") {
          sources = JSON.parse(item.data);
        } else if (item.event === "token") {
          const payload = JSON.parse(item.data);
          answer += payload.text || "";
          assistantEl.textContent = answer;
        } else if (item.event === "error") {
          const payload = JSON.parse(item.data);
          throw new Error(payload.message || "Stream error");
        }
      }
    }

    if (!answer.trim()) {
      assistantEl.textContent =
        "No response generated. If you opened this via localhost:8000, try http://127.0.0.1:8787 — another process may be intercepting localhost.";
    }
    renderSources(assistantEl, sources);
    history = [
      ...history,
      { role: "user", content: text },
      { role: "assistant", content: answer },
    ].slice(-16);
    setStatus("");
  } catch (err) {
    assistantEl.textContent = `Error: ${err.message || err}`;
    setStatus(String(err.message || err), true);
  } finally {
    busy = false;
    sendBtn.disabled = false;
    input.focus();
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const text = input.value.trim();
  if (!text) return;
  input.value = "";
  sendMessage(text);
});

input.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    form.requestSubmit();
  }
});

marketSelect.addEventListener("change", () => {
  resetConversation();
  refreshHealth();
});

reindexBtn.addEventListener("click", reindex);

ensureEmptyState();
refreshHealth();
