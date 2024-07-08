"""
Submission Result: Runtime Error 
Runtime Error Message:
ValueError: math domain error
                              ^^^^^^^^^^^^^^^^^^^^^^^^
    return sum(-t/total_cnt * math.log(t/total_cnt, 2) if t else 0 for t in cnt)

Last executed input:
[1,2,3,4,5,6,7,8,9,10]
["versicolor","versicolor","setosa","virginica","virginica","versicolor","versicolor","setosa","versicolor","versicolor"]
"""
class Solution:
    def calculateMaxInfoGain(self, petal_length: List[float], species: List[str]) -> float:
        n = len(species)
        cnt = Counter(species)
        H = self.calculateEntropy(list(cnt.values()), n)
        
        arr = list(zip(petal_length, species))
        arr.sort()
        
        # max information gain
        MIG = 0
        # class code: setosa=0, versicolor=1
        cnt1 = [0, 0]
        cnt2 = [cnt["setosa"], cnt["versicolor"]]
        for i in range(n - 1):
            if arr[i][1] == "setosa":
                cnt1[0] += 1
                cnt2[0] -= 1
            else:
                cnt1[1] += 1
                cnt2[1] -= 1
                
            H1 = self.calculateEntropy(cnt1, i + 1)
            H2 = self.calculateEntropy(cnt2, n - i - 1)
            ig = H - (i+1)/n * H1 - (n-i-1)/n * H2
            MIG = max(MIG, ig)
        return MIG
        
    def calculateEntropy(self, cnt, total_cnt):
        return sum(-t/total_cnt * math.log(t/total_cnt, 2) if t else 0 for t in cnt)
                