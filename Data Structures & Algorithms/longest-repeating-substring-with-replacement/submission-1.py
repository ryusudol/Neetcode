from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_freq, l = 1, 0
        for r, c in enumerate(s):
            freq[c] += 1
            max_freq = max(max_freq, freq[c])
            if (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
        return len(s) - l