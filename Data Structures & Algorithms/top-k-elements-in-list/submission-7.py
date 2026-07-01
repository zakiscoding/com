
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):
        freq = defaultdict(int)
        for n in nums:
            freq[n]+=1
        buckets = [[] for i in range(len(nums)+1)]

        for num,count in freq.items():
            buckets[count].append(num)
        
        res=[]
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res
