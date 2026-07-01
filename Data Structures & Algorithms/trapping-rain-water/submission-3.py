class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        leftM = height[left]
        rightM = height[right]
        water = 0
        while left<right:
            if leftM<rightM:
                left+=1
                leftM = max(leftM, height[left])
                water += leftM-height[left]
            else:
                right-=1
                rightM = max(rightM, height[right])
                water += rightM-height[right]
        return water