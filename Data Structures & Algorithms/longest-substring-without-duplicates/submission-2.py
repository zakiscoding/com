class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest =0
        left = 0

        for right, char in enumerate(s):
            if char in seen and left<=seen[char]:
                left=seen[char]+1
            seen[char]=right
            longest = max(longest, right-left+1)
        return longest
