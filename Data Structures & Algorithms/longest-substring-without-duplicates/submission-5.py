class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # input: s = 'zxyzxyz'
        # output: 3
        existing = set()
        l = 0 
        maxLen = 0
        for r in range(len(s)):
          
            while s[r] in existing:
                existing.remove(s[l])
                l += 1
              
                
            maxLen = max(maxLen, r-l+1)
            existing.add(s[r])
        
        return maxLen
