class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        longest = 0

        for i,char in enumerate(s):
            if char in seen and seen[char]>=left:
                left= seen[char]+1
            seen[char]=i
            longest=max(longest,i-left +1)
        return longest