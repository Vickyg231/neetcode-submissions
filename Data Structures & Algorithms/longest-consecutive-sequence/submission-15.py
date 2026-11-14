class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for i in numSet:
            if i-1 not in numSet:
                temp = 1

                while i+temp in numSet:
                    temp += 1

                if temp > longest:
                    longest = temp

        return longest