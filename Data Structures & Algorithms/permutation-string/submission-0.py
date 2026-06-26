class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        num=len(s1)
        for i in range(len(s2)-num+1):
            if sorted(s2[i:i+num])==sorted(s1):
                return True
        return False