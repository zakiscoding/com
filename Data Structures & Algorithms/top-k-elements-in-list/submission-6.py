
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):
        freq=defaultdict(int)
        for n in nums:
            freq[n]+=1
        bucket = [[] for _ in range(len(nums)+1)]

        for num, count in freq.items():
            bucket[count].append(num)
        res= []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res