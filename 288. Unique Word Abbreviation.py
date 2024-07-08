"""
191 ms runtime beats 45.76%
29.40 MB memory beats 60.68%
"""
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dic = defaultdict(set)
        for st in dictionary:
            key = self.hash(st)
            self.dic[key].add(st)

    def isUnique(self, word: str) -> bool:
        key = self.hash(word)
        if key not in self.dic:
            return True

        ret = False
        if len(self.dic[key]) == 1:
            pre = self.dic[key].pop()
            if pre == word:
                ret = True
            self.dic[key].add(pre)
        return ret

    def hash(self, word: str) -> str:
        return word[0] + str(len(word[1: -1])) + word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)