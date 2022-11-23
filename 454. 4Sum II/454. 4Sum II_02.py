"""
Submission Result: Time Limit Exceeded
"""
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        map1 = {}
        map2 = {}
        map3 = {}
        map4 = {}
        for d in range(len(nums1)):
            if nums1[d] not in map1:
                map1[nums1[d]] = 1
            else:
                map1[nums1[d]] += 1
            if nums2[d] not in map2:
                map2[nums2[d]] = 1
            else:
                map2[nums2[d]] += 1
            if nums3[d] not in map3:
                map3[nums3[d]] = 1
            else:
                map3[nums3[d]] += 1
            if nums4[d] not in map4:
                map4[nums4[d]] = 1
            else:
                map4[nums4[d]] += 1
        keys1 = map1.keys()
        keys2 = map2.keys()
        keys3 = map3.keys()
        keys4 = map4.keys()
        ans = 0
        for i in keys1:
            for j in keys2:
                for k in keys3:
                    for l in keys4:
                        if i+j+k+l == 0:
                            ans += map1[i]*map2[j]*map3[k]*map4[l]
        return ans
