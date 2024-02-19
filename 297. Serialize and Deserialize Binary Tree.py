https://leetcode.com/problems/serialize-and-deserialize-binary-tree/submissions/1180331207/\
#notes: a tree is a graph as well so you can use dfs and bfs on a tree as well.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if not root:
                return [None]

            left = helper(root.left)
            right = helper(root.right)

            return [root.val] + left + right

        return str(helper(root))


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = eval(data)
        print(data)
        self.i = 0

        def dfs():
            if data[self.i] == None:
                
                self.i = self.i + 1
                return None

            root = TreeNode(data[self.i])
            self.i = self.i + 1
            root.left = dfs()
            root.right = dfs()

            return root
    
        return dfs()




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
