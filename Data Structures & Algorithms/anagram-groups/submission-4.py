class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            wordArray = [0] * 26
            for i in range(len(word)):
                wordArray[ord(word[i]) - ord('a')] += 1
            anagrams[tuple(wordArray)].append(word)
        return list(anagrams.values())
