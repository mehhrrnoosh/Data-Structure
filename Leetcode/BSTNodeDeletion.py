class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            if root.val == key:
                if root.left is None and root.right is None:
                    return None
                elif root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    # both children are available
                    pointer = root.right
                    while pointer.left:
                        pointer = pointer.left
                    root.val = pointer.val
                    root.right = self.deleteNode(root.right, pointer.val)
            elif root.val > key:
                root.left = self.deleteNode(root.left, key)
            else:
                root.right = self.deleteNode(root.right, key)
            return root
