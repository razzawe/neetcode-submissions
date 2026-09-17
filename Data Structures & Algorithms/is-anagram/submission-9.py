class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        setS = {}
        setT = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            setS[s[i]] = 1 + setS.get(s[i], 0)
            setT[t[i]] = 1 + setT.get(t[i], 0)
        
        return setS == setT