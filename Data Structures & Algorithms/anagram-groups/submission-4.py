class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newStrs = defaultdict(list)
        for i in strs:
            j = ''.join(sorted(i))
            newStrs[j].append(i)
        return list(newStrs.values())
        