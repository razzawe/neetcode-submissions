class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for word in strs:
            newWord = [0] * 26
            for char in word:
                newWord[ord(char) - ord('a')] += 1

            words[tuple(newWord)].append(word)

        return list(words.values())
