"""
49 ms runtime beats 42.72%
16.4 MB memory beats 29.25%
"""
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        lst = sentence.split()
        vowels = {"a", "e", "i", "o", "u"}
        for i, word in enumerate(lst):
            if word[0].lower() in vowels:
                lst[i] = word + "ma" + "a"*(i+1)
            else:
                lst[i] = word[1:] + word[0] + "ma" + "a"*(i+1)
        return " ".join(lst)