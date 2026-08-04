# RFP Knowledge Base

Market-segregated markdown for the RFP Assistant.

## Layout

| Path | Market | Purpose |
|------|--------|---------|
| `uae/` | UAE | UAE e-invoicing RFP knowledge |
| `omn/` | OMN | Oman e-invoicing RFP knowledge |
| `shared/` | Both | Company-wide facts used for either market |

Ingest tags each file with `market` from the top-level folder (`uae`, `omn`, or `shared`). Chat retrieval is filtered to the selected market plus `shared`.

After edits:

```bash
python -m app.ingest
```

Or use **Re-index** in the UI.
