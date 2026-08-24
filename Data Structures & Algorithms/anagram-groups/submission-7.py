from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for str in strs:
            strSorted = ''.join(sorted(str))
            groups[''.join(sorted(str))].append(str)
        return list(groups.values())