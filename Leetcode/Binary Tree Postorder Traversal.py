from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postFunction(node):
            if node is None:
                return
            postFunction(node.left)
            postFunction(node.right)
            result.append(node.val)

        result = []
        postFunction(root)
        return result
