class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = set(s)
        t1 = set(t)
        if len(t1) > len(s1):
            for i in t1:
                if s.count(i) != t.count(i):
                    return False
        else:
            for i in s1:
                if s.count(i) != t.count(i):
                    return False
        return True
        