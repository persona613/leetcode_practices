"""
210 ms runtime beats 83.16%
18.70 MB memory beats 82.99%
"""
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        # total satisfied customers
        tsc = sum(customers[i] for i in range(n) if grumpy[i] == 0)

        # un-satisfied customers
        unsc = 0
        for i in range(minutes):
            unsc += customers[i] if grumpy[i] == 1 else 0

        # max un-satisfied customers
        mx = unsc
        for i in range(minutes, n):
            unsc += customers[i] if grumpy[i] == 1 else 0
            unsc -= customers[i - minutes] if grumpy[i - minutes] else 0
            if unsc > mx:
                mx = unsc
        return mx + tsc