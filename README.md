# Bounty Radar skill for IBM Bob

Turn Bob into a freelance bounty-deal desk: read the hunter's criteria,
scan public bounty boards, score fit, and draft an action plan.
Built for the IBM Bob 2.0 hackathon (AI-assisted development).

## Layout (Bob skills format)

```
.bob/skills/bounty-radar/
  SKILL.md               # skill instructions (auto-activated by description)
  references/
    boards.md            # public board endpoints + fetch contracts
    scoring.md           # fit rubric
    safety.md            # approval + honesty contracts
```

## Demo (2 min, no credentials)

```bash
cd demo && python3 radar.py --min-reward 300 --skills solana,dev,agent
```

Fetches live Superteam Earn listings, scores fit, prints a ranked shortlist.
Same workflow the skill teaches Bob; the script is the reproducible proof.
