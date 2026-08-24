class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([str(len(s)).rjust(3,'0') + s for s in strs])

    def decode(self, s: str) -> List[str]:
        res = []
        pos = 0
        while pos < len(s):
            n = int(s[pos:pos+3])
            pos += 3
            res.append(s[pos:pos+n])
            pos += n
        return res
