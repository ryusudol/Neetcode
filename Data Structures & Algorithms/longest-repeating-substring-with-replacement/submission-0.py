from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        longest_len, max_freq, l = 1, 1, 0
        for r, c in enumerate(s):
            freq[c] += 1
            max_freq = max(max_freq, freq[c])
            cur_len = (r - l + 1)
            if cur_len - max_freq <= k:
                longest_len = max(longest_len, cur_len)
            else:
                freq[s[l]] -= 1
                l += 1
        return longest_len