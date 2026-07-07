class Solution:
    def trap(self, height: List[int]) -> int:
        left =0
        right = len(height)-1
        leftM = height[left]
        rightM = height[right]
        res = 0
        while left < right:            
            if leftM < rightM:
                left+=1
                leftM = max(height[left], leftM)
                res += leftM - height[left]
            else:
                right-=1
                rightM = max(height[right], rightM)
                res += rightM - height[right]
        return res
