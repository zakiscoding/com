class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1=defaultdict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            list1[tuple(count)].append(word)
        return list(list1.values())