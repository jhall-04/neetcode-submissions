# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            qLen = len(queue)
            cur = []
            for _ in range(qLen):
                node = queue.popleft()
                if node:
                    cur.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if cur:
                res.append(cur)
        return res
            

        