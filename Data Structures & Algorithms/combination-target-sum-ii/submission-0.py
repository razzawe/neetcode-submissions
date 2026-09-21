class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        candidates.sort() #o(nlogn)
        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            # choose candidates[i], increment i as we are not reusing same values
            
            subset.append(candidates[i])
            dfs(i+1, total + candidates[i])
        
            #undo that choice:
            subset.pop()

            # skip nums[i], skip redundant values to remove repetitive combinations
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, total)
        dfs(0,0)

        return res