"""
Wrong Answer
31 / 76 testcases passed

Editorial
Input
chars =
["a","a","a","b","b","a","a"]

Use Testcase
Output
["b","2","a","5"]
Expected
["a","3","b","2","a","2"]
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        d = defaultdict(int)
        while chars:
            d[chars.pop()] += 1
        keys = list(d.keys())
        for i in range(len(d)-1, -1, -1):
            k = keys[i]
            chars.append(k)
            if d[k] > 1:
                chars.extend(list(str(d[k])))
        return len(chars)