class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            findVal = target - nums[i]

            if findVal in nums:
                newVal = nums.index(findVal)

                if newVal == i:
                    try:
                        newVal = nums.index(findVal, i + 1)
                    except ValueError:
                        continue

                return [i, newVal]