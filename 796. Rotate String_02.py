"""
Wrong Answer
49 / 54 testcases passed

Editorial
Input
s =
"aa"
goal =
"a"

Use Testcase
Output
true
Expected
false
"""
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return goal in s + s