class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        for n in nums:
            freq[n]+=1
        buckets =[[] for _ in range(len(nums)+1)]
        for num, count in freq.items():
            buckets[count].append(num)
        res=[]
        for b in range(len(buckets)-1,0,-1):
            for i in buckets[b]:
                res.append(i)
                if len(res)==k:
                    return res