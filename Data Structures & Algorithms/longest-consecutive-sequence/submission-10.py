class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        print(nums)
        current = 1 
        maxV = 1
        for i in range (len(nums)-1):
            print(nums[i+1])
            print(nums[i])
            if (nums[i+1] - nums[i] == 1):
                current += 1
                print("Here")
                print(nums[i+1] - nums[i])
            elif (nums[i+1] == nums[i]):
                print("now here")
                print(nums[i+1])
                print(nums[i])
                continue
            else:
                if current >= maxV:
                    print("yipee")
                    maxV = current
                    current = 1
                    
                
        if current > maxV:
            maxV = current
        return maxV

        