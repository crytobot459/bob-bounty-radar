#!/usr/bin/env python3
"""Unit tests for radar scoring (no network). Run: python3 -m unittest test_radar -v"""
import unittest
from radar import score_rows


def item(title="Build a dev bot", reward="500", deadline="2026-12-31T00:00:00.000Z",
         subs=3, status="OPEN", won=False, slug="x"):
    return {"title": title, "rewardAmount": reward, "deadline": deadline,
            "status": status, "isWinnersAnnounced": won, "slug": slug,
            "_count": {"Submission": subs}}


class TestScore(unittest.TestCase):
    def test_basic_pass(self):
        rows = score_rows([item()], ["dev", "bot"], 100)
        self.assertEqual(len(rows), 1)
        self.assertGreaterEqual(rows[0][0], 30)

    def test_below_min_dropped(self):
        self.assertEqual(score_rows([item(reward="50")], ["dev"], 100), [])

    def test_expired_dropped(self):
        self.assertEqual(
            score_rows([item(deadline="2020-01-01T00:00:00.000Z")], ["dev"], 0), [])

    def test_unknown_reward_dropped(self):
        self.assertEqual(score_rows([item(reward=None)], ["dev"], 0), [])

    def test_winners_announced_dropped(self):
        self.assertEqual(score_rows([item(won=True)], ["dev"], 0), [])

    def test_sorted_desc(self):
        rows = score_rows([item(title="Small post", reward="150", subs=90),
                           item(title="Big dev build", reward="5000", subs=1)],
                          ["dev"], 100)
        self.assertEqual(len(rows), 2)
        self.assertGreaterEqual(rows[0][0], rows[1][0])

    def test_no_skill_match_still_listed(self):
        rows = score_rows([item(title="Video contest", reward="500")], ["dev"], 100)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][6], "")


if __name__ == "__main__":
    unittest.main()
