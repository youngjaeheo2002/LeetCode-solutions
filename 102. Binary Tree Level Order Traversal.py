# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)

        if len(left) > len(right):

            for i in range(len(right)):
                left[i] = left[i] + right[i]

            returnVal = [[root.val]] + left

            return returnVal

        else:

            for i in range(len(left)):
                right[i] = left[i] + right[i]

            returnVal = [[root.val]] + right

            return returnVal


        
