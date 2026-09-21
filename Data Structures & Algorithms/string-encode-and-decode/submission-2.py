class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            cnt = ""
            while s[i] != "#":
                cnt += s[i]
                i += 1
            res.append(s[i + 1:i + int(cnt) + 1])
            i = i + int(cnt) + 1
        return res