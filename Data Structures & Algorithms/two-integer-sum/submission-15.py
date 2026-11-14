class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            findVal = target - nums[i]
            if nums.count(findVal) != 0:
                newVal = nums.index(findVal)
                if newVal == i:
                    if nums.count(findVal) > 1:
                        newVal = nums.index(findVal,i+1)
                        return [i,newVal]
                    continue
                return [i,newVal]
                    