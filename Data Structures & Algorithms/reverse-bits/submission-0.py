class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        for i in range(32):
            if ((n >> i) & 1) == 1:
                answer |= (1 << (31 - i))
            
        return answer