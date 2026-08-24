class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        map = {}
        for str in strs:
            strSorted = ''.join(sorted(str))
            idx = map.get(strSorted, -1)
            if idx<0:
                idx = len(groups)
                map[strSorted] = idx
                groups.append([])
            groups[idx].append(str)
        return groups