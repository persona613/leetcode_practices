"""
354 ms runtime beats 13.56%
24.85 MB memory beats 94.66%
"""
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        def root(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                if prefix in dic:
                    return prefix
            return word

        dic = set(dictionary)
        arr = sentence.split()
        for i in range(len(arr)):
            arr[i] = root(arr[i])
        return " ".join(arr)