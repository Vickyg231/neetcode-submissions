class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)
        for i in nums:
            store[i] += 1
        sortStore = sorted(store.items(),key=lambda x: x[1],reverse = True)
        #print(sortStore)
        newL = []
        for i in range(0,k):
            newL.append(sortStore[i][0])
        return newL
            
        
        