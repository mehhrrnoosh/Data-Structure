from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            value = node.val
            result = value if low <= value <= high else 0
            if value > low:
                result += dfs(node.left)
            if value < high:
                result += dfs(node.right)
            return result

        return dfs(root)
