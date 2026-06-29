import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap=[]
        for char, freq in count.items():
            heapq.heappush(heap,(-freq,char))
        
        res=[]
        prev_char=''
        prev_freq=0
        while heap:
            freq , char= heapq.heappop(heap)
            freq+=1
            res.append((char))
            if prev_freq<0:
                heapq.heappush(heap,(prev_freq, prev_char))
            prev_char=char
            prev_freq=freq
        ans = ''.join(res)
        if len(res)!=len(s):
            return ''
        return ans
