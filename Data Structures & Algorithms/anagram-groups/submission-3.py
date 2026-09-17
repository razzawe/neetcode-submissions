class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for item in strs:
            count = [0] * 26
            for i in range(len(item)):
                count[ord(item[i]) - ord('a')] += 1
            res[tuple(count)].append(item)
        return list(res.values())