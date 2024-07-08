"""
38 ms runtime beats 35.17%
16.46 MB memory beats 87.62%
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def dp(i):
            if i in memo: return memo[i]
            if i == 0: return [[]]

            # curr-i sentences
            curr_sents = []
            for j in range(m):
                curr_word = wordDict[j]
                size = wordsize[j]
                if i - size >= 0 and curr_word == s[i - size: i]:
                    # left_sentences_idx
                    left_sents = dp(i - size)
                    if left_sents:
                        for lsen in left_sents:
                            new_sen = lsen[:]
                            new_sen.append(j)
                            curr_sents.append(new_sen)
            memo[i] = curr_sents
            return memo[i]

        n = len(s)
        m = len(wordDict)
        memo = dict()
        wordsize = []
        for wd in wordDict:
            wordsize.append(len(wd))

        ret = dp(n)
        res = []
        for lst in ret:
            sen = []
            for word_idx in lst:
                sen.append(wordDict[word_idx])
            res.append(" ".join(sen))
        return res