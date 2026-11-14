class Solution:

    def encode(self, strs: List[str]) -> str:
        endS = ""
        for i in range(0,len(strs)):
            endS+=(strs[i])
            endS+="~"
        #print(endS)
        return endS

    def decode(self, s: str) -> List[str]:
        s = s.split("~")
        return s[0:len(s)-1]
