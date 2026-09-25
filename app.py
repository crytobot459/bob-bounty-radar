#!/usr/bin/env python3
"""app.py — HF Spaces (Gradio) cho Bounty Radar.
Judge mở URL là dùng được: nhập skills + min-reward -> shortlist live Superteam Earn.
Local: pip install -r requirements.txt && python3 app.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "demo"))
from radar import score_rows  # noqa: E402

import json
from urllib.request import Request, urlopen

API = "https://earn.superteam.fun/api/listings"

try:
    import gradio as gr
except Exception:
    gr = None


def fetch_live():
    req = Request(API, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
    with urlopen(req, timeout=30) as r:
        return json.load(r)


def rank(min_reward, skills_txt, limit=10):
    skills = [s.strip().lower() for s in (skills_txt or "").split(",") if s.strip()]
    try:
        items = fetch_live()
        board = f"superteam-earn live (scanned={len(items)})"
    except Exception as e:
        return f"Lỗi mạng board: {str(e)[:200]} — thử lại sau 1 phút."
    rows = score_rows(items, skills, float(min_reward or 0))
    if not rows:
        return f"{board}\nKhông có bounty khớp — giảm min-reward hoặc đổi skills."
    out = [board, ""]
    for i, (sc, rw, dl, title, subs, slug, hits) in enumerate(rows[:int(limit or 10)], 1):
        out.append(f"{i}. [{sc}] {title[:80]}")
        out.append(f"   ${rw:g} | {dl:.0f}d left | {subs} subs | match: {hits or '-'}")
        out.append(f"   https://earn.superteam.fun/listing/{slug}")
    out.append("")
    out.append("Next: read requirements -> check eligibility -> claim (Bob không claim hộ).")
    return "\n".join(out)


if __name__ == "__main__":
    if gr is None:
        print("Chưa có gradio — pip install -r requirements.txt")
        print(rank(300, "solana,dev,agent"))
    else:
        demo = gr.Interface(
            fn=lambda mr, sk: rank(mr, sk, 10),
            inputs=[
                gr.Number(value=300, label="min-reward USD"),
                gr.Textbox(value="solana,dev,agent", label="skills (cách nhau dấu phẩy)"),
            ],
            outputs=gr.Textbox(label="Ranked bounties", lines=20),
            title="Bounty Radar — Bob skill proof (IBM Bob 2.0)",
            description="Nhập skills + min-reward, nhận shortlist Superteam Earn có điểm. Repo: github.com/crytobot459/bob-bounty-radar",
        )
        demo.launch()
