from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        abc = [chr(i) for i in range(ord('a'), ord('z')+1)]
        for str in strs:
            freq = Counter(str)
            hash = ','.join([f'{c}:{freq[c]}' for c in abc if c in freq])
            groups[hash].append(str)
        return list(groups.values())