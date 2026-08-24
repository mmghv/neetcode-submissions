class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return '\\'
        return ','.join(s.replace('\\', '\\\\').replace(',', '\\,') for s in strs)


    def decode(self, s: str) -> List[str]:
        res = []
        item = ''
        escape = False
        for c in s:
            if escape:
                escape = False
            elif c == '\\':
                escape = True
                continue
            elif c == ',':
                res.append(item)
                item = ''
                continue
            item += c
        if not escape: res.append(item)
        return res
            
