"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        seen = {}
        self.dfs(node, seen)
        return seen[node]
        
    def dfs(self, node, seen):
        if node in seen:
            return seen[node]
        clone = Node(node.val)
        seen[node] = clone
        for neighbor in node.neighbors:
            seen[node].neighbors.append(self.dfs(neighbor, seen))
        return seen[node]
        




        