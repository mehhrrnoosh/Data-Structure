
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def depthFirstSearch(root):
            if root is None:
                return
            depthFirstSearch(root.left)
            result.append(root.val)
            depthFirstSearch(root.right)

        result = []
        depthFirstSearch(root)
        return result
