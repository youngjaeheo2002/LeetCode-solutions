from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited_vals = []
        visited = []
        completed = []
        completed_vals = []
        def helper(node):
            
            if not node:
                return None
            copy = Node(node.val)
            if node.val in visited_vals:
                return visited[visited_vals.index(node.val)]
            visited.append(copy)
            visited_vals.append(node.val)
            if node.val in completed:
                return completed[completed_vals.index(node.val)]
            
            for neighbor in node.neighbors:
                copy.neighbors.append(helper(neighbor))
            return copy

        return helper(node)

