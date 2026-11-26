class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        anagramS = [0] * 26 
        anagramT = [0] * 26
        for c in s:
            anagramS[ord(c) - ord('a')] += 1
        for c in t:
            anagramT[ord(c) - ord('a')] += 1
        
        return anagramS == anagramT


