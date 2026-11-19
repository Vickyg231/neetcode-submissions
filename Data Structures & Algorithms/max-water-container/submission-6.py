class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0;
        k = len(heights)-1
        j = 0
        while k != j:
            maxH = min(heights[j],heights[k])
                #print(maxH)
            Vol = maxH*(k-j)
                #print(Vol)
            if Vol > maxA:
                maxA = Vol
            if heights[k] < heights[j]:
                k = k-1
            else:
                j = j +1
        return maxA