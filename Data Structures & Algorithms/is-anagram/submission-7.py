class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        setA = {}
        setB = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            setA[s[i]] = 1 + setA.get(s[i], 0)
            setB[t[i]] = 1 + setB.get(t[i], 0)

        return setA == setB