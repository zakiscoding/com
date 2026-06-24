class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1=defaultdict(list)
        for i in strs:
            key=tuple(sorted(i))
            list1[key].append(i)
        return list(list1.values())