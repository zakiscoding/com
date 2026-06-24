class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i,v in enumerate(nums):
            if target-v in hash:
                return [hash[target-v],i]
            hash[v]=i
        
            