"""
54 ms runtime beats 40.41%
16.4 MB memory beats 7.89%
"""
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.",\
               "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..",\
               "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.",\
               "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-",\
               "y":"-.--", "z":"--.."}
        tfset = set()
        for word in words:
            tf = ""
            for c in word:
                tf += dic[c]
            tfset.add(tf)
        return len(tfset)