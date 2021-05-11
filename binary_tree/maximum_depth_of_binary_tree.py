# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

# solution 1

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# solution 2

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0

        q = deque([(1, root)])

        while q:
            depth, node = q.popleft()
            if node.left:
                q.append((depth + 1, node.left))
            if node.right:
                q.append((depth + 1, node.right))
        
        return depth