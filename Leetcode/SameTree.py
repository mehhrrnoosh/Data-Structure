# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      if not p and not q: #base
        return True
      if not p or not q:     #base
        return False
      if p.val != q.val:     #base
        return False
      return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
     

