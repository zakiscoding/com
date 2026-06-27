class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for word in strs:
            count= [0]*26

            for c in word:
                count[ord(c)-ord('a')]+=1
            dict1[tuple(count)].append(word)
        return list(dict1.values())
