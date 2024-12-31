"""
59 ms runtime beats 20.06%
16.96 MB memory beats 59.89%
"""
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [1000000] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            # curr layer height and width
            currH = 0
            currW = shelfWidth
            # cut books in different point if width sum <= shelfWidth
            for j in range(i, 0, -1):
                bw, bh = books[j - 1]
                if bw > currW:
                    break
                currH = max(currH, bh)
                currW -= bw
                # curr-cut's solution of total height
                currS = currH + dp[j - 1]
                # update dp[i] minim solution of total height
                if currS < dp[i]:
                    dp[i] = currS
        return dp[-1]