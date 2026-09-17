class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxC = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxC = max(maxC, count[s[r]])
            if (r - l + 1) - maxC <= k:
                res = max(res, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1
            
        return res

# x = 1
# x = 1, y = 1