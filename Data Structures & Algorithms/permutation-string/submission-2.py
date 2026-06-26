class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_count={}
        s2_count={}
        left=0
        for c in s1:
            s1_count[c]=s1_count.get(c,0)+1
        
        for right in range(len(s2)):

            c = s2[right]
            s2_count[c]=s2_count.get(c,0)+1

            if right-left+1> len(s1):
                left_char= s2[left]
                s2_count[left_char]-=1
                if s2_count[left_char]==0:
                    del s2_count[left_char]
                left+=1
            if s1_count==s2_count:
                return True
        return False