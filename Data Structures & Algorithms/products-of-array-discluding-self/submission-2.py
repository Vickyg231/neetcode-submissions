class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resultWZ = 1
        result = 1
        for i in nums:
            if i != 0:
                resultWZ *= i
            result *= i
        print(result)
        results = []
        for i in nums:
            if i == 0 and nums.count(0) > 1:
                results.append(0)
            elif i == 0:
                results.append(resultWZ)
            else:
                results.append(result//i)
        return results
