class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right = len(matrix) -1

        target_row = -1
        while left<=right:
            mid = (right+left)//2
            value = matrix[mid][0]

            if value < target:
                left=mid+1
                target_row=mid
            elif value ==target:
                return True
            else:
                right = mid -1
        if target_row == -1:
            return False

        left=0
        right = len(matrix[0]) -1
        while left<=right:
            mid = (right+left)//2
            value = matrix[target_row][mid] 

            if value <target:
                left = mid+1
                target_row-mid
            elif value ==target:
                return True
            else:
                right=mid-1
        return False

