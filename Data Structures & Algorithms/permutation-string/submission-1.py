class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        num=len(s1)
        for i in range(0,len(s2)+1):
            if sorted(s2[i:i+num])==sorted(s1):
                return True
        return False