'''
Runtime: 117 ms, faster than 8.19% of Python3 online submissions for Richest Customer Wealth.
Memory Usage: 13.9 MB, less than 32.36% of Python3 online submissions for Richest Customer Wealth.
'''


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        length = len(accounts)
        max_wealth = 0
        
        for account in accounts:
            wealth = 0
            for bank in account:
                wealth += bank
            if wealth > max_wealth:
                max_wealth = wealth
                
        return max_wealth