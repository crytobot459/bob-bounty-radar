---
title: Bounty Radar — Bob skill proof
emoji: 📡
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
---

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

## Demo live (HuggingFace Spaces — judge mở URL, không setup)

Space URL (điền sau khi tạo): `https://crytobot459-bob-bounty-radar.static.hf.space`

```bash
pip install -r requirements.txt && python3 app.py
```

## Kiếm tiền sao (3 đường, sau hackathon vẫn chạy)

1. **Ăn bounty thật:** mở app, lọc min-reward + skills khớp, claim trên Superteam Earn (thường $300-5000/bounty). Radar tiết kiệm giờ lọc, không ăn chia.
2. **Bán skill-pack:** `.bob/skills/bounty-radar/` đóng gói thành $19/seat/tháng cho solo dev (review + test + docs workflow). Đây là revenue slide cho deck.
3. **Ăn giải lablab:** $12k Bob 2.0 — nộp repo này + video + deck + BOB_REPORT (xem lablab-harness).

## Nộp lablab cần thêm gì (checklist)

- [ ] `BOB_REPORT.md` export mọi session Bob (BẮT BUỘC, thiếu là mất Technology)
- [ ] Video 4-5 phút: problem 30s + live demo URL ở giữa + business case (TAM + revenue trên)
- [ ] Deck 8-10 slides + text description standalone ≥100 từ + track nhắm tên rõ
- [ ] Commit rải 25-27/9 (hiện mới 2 commits 24/9 — cần thêm 3-5 commits trong window)
- [ ] `demo_url` HF + repo public + screenshot submit tay trước 22:00 VN 27/9
