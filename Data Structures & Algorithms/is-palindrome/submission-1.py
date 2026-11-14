class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
                newS += i.lower()
        reverseS = ""
        for i in range(len(newS)-1,-1,-1):
            reverseS += newS[i]
        return newS == reverseS
            


        