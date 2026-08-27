# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.DFS(root, float('-inf'), float('inf'))

    def DFS(self, root, left_max, right_min):
        if not root:
            return True
        if right_min <= root.val or root.val <= left_max:
            return False
        return self.DFS(root.left, left_max, root.val) and self.DFS(root.right, root.val, right_min)
    
        
        