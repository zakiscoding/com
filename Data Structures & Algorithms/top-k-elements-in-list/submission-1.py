class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        freq = defaultdict(int)
        for i in nums:
            freq[i]+=1
        res = sorted(freq.items(), key = lambda x:x[1], reverse=True)
        return [num for num, count in res[:k]]