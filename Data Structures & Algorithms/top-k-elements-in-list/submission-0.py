class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        finalL = dict()
        for i in nums:
            if i in finalL:
                finalL[i] += 1
            else:
                finalL[i] = 1
        rev = sorted(finalL, key = finalL.get, reverse=True)
        returnL = []
        for i in range(k):
            returnL.append(rev[i])

        return returnL