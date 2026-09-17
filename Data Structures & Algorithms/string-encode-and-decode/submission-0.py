class Solution:

    def encode(self, strs: List[str]) -> str:
        new_word = ""
        for word in strs: # N
            new_word += str(len(word)) + "#" + word
        return new_word

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            length = ""
            new_word = ""
            while s[i] != '#':
                length += s[i]
                i += 1
            i += 1
            length = int(length)
            j = 0
            while j < length:
                new_word += s[i]
                i += 1
                j += 1
            res.append(new_word)

        return res
