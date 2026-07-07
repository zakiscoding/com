class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ''

        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c,0)+1
        
        window = {}
        res = ''
        res_len = float('inf')
        have= 0
        need = len(t_count)
        left =0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0)+1
            if c in t_count and window[c]==t_count[c]:
                have +=1
            while have == need:
                if right-left+1 <res_len:
                    res_len = right-left+1
                    res = s[left:right+1]
                left_char = s[left]
                window[left_char]-=1
                if left_char in t_count and window[left_char]<t_count[left_char]:
                    have-=1
                left+=1
        return res