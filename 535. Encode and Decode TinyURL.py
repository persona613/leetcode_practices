"""
40 ms runtime beats 35.90%
16.34 MB memory beats 95.70%
"""
class Codec:

    def __init__(self):
        self.surl_len = 7
        self.prefix = "https://tinyurl.com/"
        self.chars = "abcdefghijklmnopqrstuvwxyz \
                        ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.counter = itertools.count()
        self.dic = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        surl_id = next(self.counter)
        self.dic[surl_id] = longUrl

        surl = self.id2url(surl_id)
        return self.prefix + surl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        surl = shortUrl.split("/")[-1]
        surl_id = self.url2id(surl)
        return self.dic[surl_id]

    def id2url(self, surl_id):
        res = []
        while surl_id:
            res.append(self.chars[surl_id % 62])
            surl_id //= 62
        if len(res) < 7:
            res.extend(["a"] * (7 - len(res)))
        return "".join(res[::-1])

    def url2id(self, surl):
        surl_id = 0
        for c in surl[::-1]:
            if "a" <= c <= "z":
                surl_id = surl_id * 62 + ord(c) - ord("a")
            elif "A" <= c <= "Z":
                surl_id = surl_id * 62 + ord(c) - ord("a") + 26
            elif "0" <= c <= "9":
                surl_id = surl_id * 62 + ord(c) - ord("a") + 52
        return surl_id


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))