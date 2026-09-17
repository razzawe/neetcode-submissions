class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        res = []
        for word in strs:
            anagram = [0] * 26
            for char in word:
                anagram[ord(char) - ord('a')] += 1
            
            anagrams[tuple(anagram)].append(word)

        

        return list(anagrams.values())

