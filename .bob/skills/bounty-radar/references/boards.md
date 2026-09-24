# Boards

Public bounty boards. Plain HTTPS GET, no credentials, `Accept: application/json`.

| Board | Endpoint | Fields used |
| --- | --- | --- |
| Superteam Earn | `GET https://earn.superteam.fun/api/listings` | title, rewardAmount, token, deadline, sponsor.name, _count.Submission, slug |
| Algora org pages | `GET https://console.algora.io/org/<slug>/bounties` | issue links + amounts from HTML (low volume, secondary) |

Listing URL shape (Earn): `https://earn.superteam.fun/listing/<slug>`.
Timeout 30s per board. One retry, then mark the board failed.
