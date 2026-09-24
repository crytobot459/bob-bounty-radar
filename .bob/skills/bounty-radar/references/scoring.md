# Scoring

Fit points, higher is better. Maximum 100.

| Signal | Rule | Points |
| --- | --- | --- |
| Reward known | Required; unparseable amounts stay `null` and exclude the row | gate |
| Reward size | >= 1000 / >= 300 / >= 100 / else | 15 / 10 / 6 / 3 |
| Deadline | Future required; > 7d / > 3d / > 0 | 10 / 6 / 3 |
| Skills overlap | Each criteria keyword found in title/sponsor, cap 30 | 10 each |
| Competition | Submissions <= 5 / <= 15 / else / unknown | 5 / 3 / 1 / 3 |
| Agent-fit bonus | Fully completable by an agent (code/PR/deliverable, no identity, funds, or travel needed) | +10 |

Keep at most 10 rows. Always show total scanned vs shortlisted.
