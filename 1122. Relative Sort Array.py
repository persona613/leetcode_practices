"""
38 ms runtime beats 95.52%
16.33 MB memory beats 87.27%
"""
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dcnt = Counter(arr1)
        res = []
        for n in arr2:
            res += [n]*dcnt[n]
            del dcnt[n]
        for n in sorted(dcnt.keys()):
            res += [n]*dcnt[n]
        return res


        # # Counting Sort
        # # freq list
        # arr2 = arr2 + sorted(set(arr1) - set(arr2))
        # fr = [None]*len(arr2)
        # dic = Counter(arr1)
        # for i, n in enumerate(arr2):
        #     fr[i] = dic[n]
        
        # # accmulate list
        # for i in range(1, len(fr)):
        #     fr[i] += fr[i-1]
        # res = [None]*len(arr1)

        # t = 0
        # for i, n in enumerate(arr2):
        #     for k in range(t, fr[i]):
        #         res[k] = n
        #     t = fr[i] 
        # return res


        # 
        # dcnt = Counter(arr1)
        # res = [None]*len(arr1)
        # st = end = 0
        # for n in arr2:
        #     end += dcnt[n]
        #     for k in range(st, end):
        #         res[k] = n
        #     st = end
        #     del dcnt[n]

        # for n in sorted(dcnt.keys()):
        #     end += dcnt[n]
        #     for k in range(st, end):
        #         res[k] = n
        #     st = end
        # return res