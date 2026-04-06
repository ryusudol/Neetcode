from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t, count_window = Counter(t), defaultdict(int)
        have, need = 0, len(count_t)
        ans, ans_len = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            count_window[s[r]] += 1
            if s[r] in count_t and count_window[s[r]] == count_t[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < ans_len:
                    ans = [l, r]
                    ans_len = r - l + 1
                
                count_window[s[l]] -= 1
                if s[l] in count_t and count_window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        return s[ans[0] : ans[1] + 1] if ans_len != float("inf") else ""