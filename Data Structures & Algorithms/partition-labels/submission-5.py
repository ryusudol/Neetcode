from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        positions = defaultdict(int)
        for i, c in enumerate(s):
            positions[c] = i
        print(positions)
        res = []
        l, r = 0, positions[s[0]]
        while r < len(s):
            i = l
            while i < r + 1:
                if positions[s[i]] > r:
                    r = positions[s[i]]
                i += 1
            res.append(r - l + 1)
            if r == len(s) - 1:
                break
            l = r + 1
            r = positions[s[l]]
        return res