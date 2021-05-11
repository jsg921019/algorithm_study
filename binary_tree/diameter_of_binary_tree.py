# https://leetcode.com/problems/diameter-of-binary-tree/

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.answer = 0

        def dfs(node):
            
            if node is None:
                return 0
            
            left, right = dfs(node.left), dfs(node.right)
            self.answer = max(self.answer, left+right)
            return max(left, right) + 1
            
        dfs(root)
        return self.answer