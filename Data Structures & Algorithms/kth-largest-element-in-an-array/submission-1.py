class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target= len(nums)-k
        left=0
        right=len(nums)-1

        while left<=right:
            pivot = nums[right]
            p = left
            for i in range(left, right):
                if nums[i]<=pivot:
                    nums[i],nums[p] = nums[p], nums[i]
                    p+=1
            nums[right],nums[p] = nums[p], nums[right]

            if target==p:
                return nums[p]
            elif target>p:
                left = p+1
            else:
                right = p-1