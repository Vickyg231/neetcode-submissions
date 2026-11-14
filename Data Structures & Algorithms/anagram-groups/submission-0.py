class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #creating a list of the alphabets letters 
        #creating a map
        lists = defaultdict(list)
        #looping through the words of the list
        for i in strs:
            alphaL = [0]*26
            #looping through the alphabets
            for j in i:
                print(j)
                print(ord(j))
                print(ord(j)-97)
                alphaL[ord(j)-97]+=1
            lists[tuple(alphaL)].append(i)
        return list(lists.values())



        
                                







        