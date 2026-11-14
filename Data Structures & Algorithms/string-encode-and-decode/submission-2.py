class Solution:

    def encode(self, strs: List[str]) -> str:
        newS = ""
        for i in strs:
            newS+=i
            newS+="-"
        return newS


    def decode(self, s: str) -> List[str]:
       s = s.split("-")
       return s[0:len(s)-1]
