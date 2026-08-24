class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([chr(len(s)) + s for s in strs])

    def decode(self, s: str) -> List[str]:
        res, pos = [], 0
        while pos < len(s):
            n = ord(s[pos:pos+1])
            res.append(s[pos+1:pos+1+n])
            pos += 1+n
        return res
