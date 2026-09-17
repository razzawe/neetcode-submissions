# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        res = 0
        def dfs(root):
            if not root:
                return None
            
            dfs(root.left)
            dfs(root.right)
            heapq.heappush(heap, root.val)
            
        dfs(root)
        for _ in range(k):
            res = heapq.heappop(heap)
        
        return res
