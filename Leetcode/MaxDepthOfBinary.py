# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0  # Changed from return to return 0
        leftDepth = self.maxDepth(root.left)  # Added self.
        rightDepth = self.maxDepth(root.right)  # Added self.

        return max(leftDepth, rightDepth) + 1
