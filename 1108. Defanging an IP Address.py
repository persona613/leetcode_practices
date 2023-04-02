"""
48 ms runtime beats 29.47%
13.9 MB memory beats 441.12%
"""
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")