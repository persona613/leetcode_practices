"""
Wrong Answer
24 / 26 testcases passed
Editorial
Input
text =
"lloo"

Use Testcase
Output
1
Expected
0
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = defaultdict(int)
        ts = "balon"
        for c in text:
            if c in ts:
                cnt[c] += 1
        cnt["l"] = cnt["l"] // 2
        cnt["o"] = cnt["o"] // 2
        return min(cnt.values())

        # cnt = Counter(text)
        # ans = float("inf")
        # for c in "balon":
        #     if c == "l" or c == "o":
        #         ans = min(ans, cnt[c]//2)
        #     else:
        #         ans = min(ans, cnt[c])
        # return ans