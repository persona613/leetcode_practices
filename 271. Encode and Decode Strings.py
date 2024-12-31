"""
333 ms runtime beats 5.15%
18.20 MB memory beats 5.90%
"""
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # 8-bit: len(strs) + len(strs[i]) + strs[i]
        res = []
        n = len(strs)
        res.append(self.bit(n))
        for st in strs:
            n = len(st)
            res.append(self.bit(n))
            for c in st:
                n = ord(c)
                res.append(self.bit(n))
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        tln = int(s[:8], 2)
        start = 8
        res = []
        while start < len(s):
            # word length
            k = int(s[start: start + 8], 2)
            start += 8
            tmp = []
            for _ in range(k):
                # char
                c = int(s[start: start + 8], 2)
                c = chr(c)
                tmp.append(c)
                start += 8
            res.append("".join(tmp))
        return res

    def bit(slef, num):
        b = f"{num:08b}"
        return b



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))