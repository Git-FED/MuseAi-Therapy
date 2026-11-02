# Medication recalls

Muse Alert should not display a broad medication-news feed. A recall alert is eligible only when the user's recorded medication matches the exact drug identity and dose/strength, with a verified source and current date.

## Matching rules

- Normalize spelling, brand/generic aliases, formulation, route, and strength.
- Require exact active ingredient and exact strength; do not infer equivalence.
- Show lot/expiration details only when the authoritative notice provides them.
- Never tell a user to stop, change, or substitute medication without directing them to a pharmacist or prescriber.
- If matching is uncertain, do not alert as a match; recommend pharmacist confirmation.
- Preserve source URL, retrieval time, notice date, and a visible uncertainty statement.
