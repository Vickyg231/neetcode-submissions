class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
                newS += i.lower()
        for i in range(len(newS)//2):
            if newS[i] != newS[len(newS)-i-1]:
                return False
        return True


        