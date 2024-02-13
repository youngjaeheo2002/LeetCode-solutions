# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            
            if not root:
                return (True,None,None)

            left = helper(root.left)
            right = helper(root.right)

            if (root.left) and root.right:

                root_valid = (root.val > left[2]) and \
                (root.val < right[1]) and left[0] and right[0]
                min_subtree = min(left[1],right[1],root.val)
                max_subtree = max(right[2],left[2],root.val)
                #print(root_valid)
                return (root_valid,min_subtree,max_subtree)

            elif (root.left) and (not root.right):
                root_valid = root.val > left[2] and \
                left[0] and right[0]
                min_subtree = min(left[1],root.val)
                max_subtree = max(left[2],root.val)
                #print(root_valid)
                return (root_valid,min_subtree,max_subtree)

            elif (root.right) and (not root.left):
                root_valid = root.val < right[1] and \
                left[0] and right[0]

                min_subtree = min(right[1],root.val)
                max_subtree = max(right[2],root.val)
                #print(root_valid)
                return (root_valid,min_subtree,max_subtree)
            else:
                #print(True)
                return (True,root.val,root.val)

        return helper(root)[0]
