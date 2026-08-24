class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        map = {}
        abc = [chr(i) for i in range(ord('a'), ord('z')+1)]
        for str in strs:
            freq = {}
            for c in str: freq[c] = freq.setdefault(c, 0) + 1
            hash = ','.join([f'{c}:{freq[c]}' for c in abc if c in freq])
            idx = map.get(hash, -1)
            if idx<0:
                idx = len(groups)
                map[hash] = idx
                groups.append([])
            groups[idx].append(str)
        return groups