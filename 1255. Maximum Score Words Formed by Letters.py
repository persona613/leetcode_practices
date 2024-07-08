"""
36 ms runtime beats 98.87%
16.66 MB memory beats 75.28%
"""
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        def cost_letters(i):
            chars = words_char_cnt[i]
            # check letters cnt
            for char, cnt in chars.items():
                if cnt > letters_cnt.get(char, 0):
                    return False
            # take off letters
            for char, cnt in chars.items():
                letters_cnt[char] -= cnt
            return True
            
        def give_back_letters(i):
            chars = words_char_cnt[i]
            for char, cnt in chars.items():
                letters_cnt[char] += cnt

        # index, path score
        def backtrack(i, sc):
            if i == n:
                if sc > ans[0]:
                    ans[0] = sc
                return
            
            # take curr word in path
            if words_score[i] != -1:
                if cost_letters(i):
                    sc += words_score[i]
                    backtrack(i + 1, sc)
                    sc -= words_score[i]
                    give_back_letters(i)
            # not take curr
            backtrack(i + 1, sc)

        letters_cnt = Counter(letters)

        words_char_cnt = defaultdict(lambda: defaultdict(int))
        for i, word in enumerate(words):
            words_char_cnt[i] = Counter(word)

        words_score = defaultdict(int)
        for i, word in enumerate(words):
            chars = words_char_cnt[i]
            sc = 0
            for char, cnt in chars.items():
                if cnt <= letters_cnt.get(char, 0):
                    sc += score[ord(char) - ord("a")] * cnt
                else:
                    words_score[i] = -1
            words_score[i] = sc

        n = len(words)
        ans = [0]
        backtrack(0, 0)
        return ans[0]