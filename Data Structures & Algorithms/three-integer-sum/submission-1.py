class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        newNums = sorted(nums)
        finalInd = set()
        for i in range(0,len(newNums)):
            if i != 0 and newNums[i] == newNums[i-1]:
                continue
            target = 0 - newNums[i]
            j = i + 1
            k = len(newNums)-1
            while j < k:
                if newNums[j] + newNums[k] == target:
                    currentInd = (newNums[i],newNums[j],newNums[k])
                    finalInd.add(currentInd)
                    j = j + 1
                    k = k -1
                elif newNums[j] + newNums[k] < target:
                    j = j+1
                else:
                    k = k - 1
                currentInd = ()
        newF = []
        for i in finalInd:
            newF.append(list(i))
        return newF
                    

        