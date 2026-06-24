class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1={}
        for i,v in enumerate(nums):
            if target-v in hash1:
                return [hash1[target-v], i]
            else:
                hash1[v]=i