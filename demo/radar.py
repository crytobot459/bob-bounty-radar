#!/usr/bin/env python3
"""radar.py - Runnable proof of the bounty-radar Bob skill.

  python3 radar.py --min-reward 300 --skills solana,dev,agent

Fetches live public listings, scores fit, prints a ranked shortlist.
Stdlib only.
"""
import argparse
import json
from datetime import datetime, timezone
from urllib.request import Request, urlopen

API = "https://earn.superteam.fun/api/listings"


def days_left(dl: str):
    try:
        d = datetime.fromisoformat((dl or "").replace("Z", "+00:00"))
        return (d - datetime.now(timezone.utc)).total_seconds() / 86400
    except Exception:
        return None


def score_rows(items, skills, min_reward):
    """Pure logic, testable without network. Returns sorted row list."""
    rows = []
    for x in items:
        if (x.get("status") or "") != "OPEN" or x.get("isWinnersAnnounced"):
            continue
        raw_reward = x.get("rewardAmount")
        if raw_reward is None or (isinstance(raw_reward, str)
                                  and not raw_reward.strip()):
            continue  # unknown reward -> excluded, never estimated
        try:
            reward = float(raw_reward)
        except Exception:
            continue
        if reward < min_reward:
            continue
        dl = days_left(x.get("deadline", "") or "")
        if dl is None or dl <= 0:
            continue
        title = x.get("title", "")
        hits = [k for k in skills if k in title.lower()]
        subs = (x.get("_count") or {}).get("Submission")
        score = (15 if reward >= 1000 else 10 if reward >= 300 else 6
                 ) + (10 if dl > 7 else 6 if dl > 3 else 3
                 ) + min(30, len(hits) * 10
                 ) + (5 if subs is not None and subs <= 5 else 3
                      if subs is not None and subs <= 15 else 1
                      if subs is not None else 3)
        rows.append((score, reward, dl, title, subs, x.get("slug", ""),
                     ",".join(hits)))
    rows.sort(reverse=True)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-reward", type=float, default=100)
    ap.add_argument("--skills", default="dev")
    ap.add_argument("--limit", type=int, default=10)
    a = ap.parse_args()
    skills = [s.strip().lower() for s in a.skills.split(",") if s.strip()]

    req = Request(API, headers={"User-Agent": "Mozilla/5.0",
                                "Accept": "application/json"})
    with urlopen(req, timeout=30) as r:
        items = json.load(r)
    print(f"scanned={len(items)} board=superteam-earn")
    rows = score_rows(items, skills, a.min_reward)
    print(f"shortlisted={len(rows)} (dropped: below-min/expired/unknown)\n")
    for i, (sc, rw, dl, title, subs, slug, hits) in enumerate(rows[:a.limit], 1):
        print(f"{i}. [{sc}] {title[:75]}")
        print(f"   ${rw:g} | {dl:.0f}d left | {subs} subs | match: {hits or '-'}")
        print(f"   https://earn.superteam.fun/listing/{slug}")
        print(f"   next: read requirements -> check eligibility -> claim")


if __name__ == "__main__":
    main()
