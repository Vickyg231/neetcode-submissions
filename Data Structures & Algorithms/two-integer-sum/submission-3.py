class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            value = target-nums[i]
            if i+1 != len(nums) and value in nums[i+1:]:
                    return [i, nums.index(value,i+1)]
        return []