class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right=max(piles)
        k= 0
        while left<right:
            k=(right+left)//2 
            hours=0
            for pile in piles:
                hours+=(pile+k-1)//k
            if hours <=h:
                right=k
            else:
                left= k+1
        return left
