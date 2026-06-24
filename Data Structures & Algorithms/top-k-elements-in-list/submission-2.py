
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        dict1 = defaultdict(int)
        for i in nums:
            dict1[i]+=1

        listsort = sorted(dict1.items(), key= lambda x: x[1], reverse = True)

        return [num[0] for num in listsort[:k]]