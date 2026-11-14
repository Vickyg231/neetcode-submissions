class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        valT = 1
        val2 = 1
        for i in nums:
            if i == 0:
                val2 = val2
                valT *= i
            else:
                val2 *= i
                valT *= i
        retL = []
        for i in nums:
            if i == 0 and nums.count(0) == 1:
                retL.append(val2)
            elif i == 0 and nums.count(0) > 1:
                retL.append(0)
            else:
                retL.append(int(valT/i))
        return retL

        