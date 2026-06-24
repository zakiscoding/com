
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        # Sort by frequency (highest first)
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Take the first k elements (just the numbers)
        return [num[0] for num in sorted_items[:k]]