"""
33 ms runtime beats None %
16.8 MB memory beats None %
"""
class Solution:
    def calculateMaxInfoGain(self, petal_length: List[float], species: List[str]) -> float:
        classes = list(set(species))
        index = dict()
        for i, name in enumerate(classes):
            index[name] = i
        
        k = len(classes)
        cnt = [0] * k
        n = len(species)
        for i in range(n):
            cl = species[i]
            idx = index[cl]
            cnt[idx] += 1
        H = self.calculateEntropy(cnt, n)
        
        arr = list(zip(petal_length, species))
        arr.sort()
        
        # max information gain
        MIG = 0
        cnt1 = [0] * k
        cnt2 = cnt.copy()
        for i in range(n - 1):
            cl = arr[i][1]
            idx = index[cl]
            cnt1[idx] += 1
            cnt2[idx] -= 1
                
            H1 = self.calculateEntropy(cnt1, i + 1)
            H2 = self.calculateEntropy(cnt2, n - i - 1)
            ig = H - (i+1)/n * H1 - (n-i-1)/n * H2
            MIG = max(MIG, ig)
        return MIG
        
    def calculateEntropy(self, cnt, total_cnt):
        # print(f"{cnt = }, {total_cnt = }")
        return sum(-t/total_cnt * math.log(t/total_cnt, 2) if t else 0 for t in cnt)
        