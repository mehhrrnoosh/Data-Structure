# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        list =[]
        q = deque()
        q.append(root)

        while q:
            queueLen = len(q)
            levelOrderList = []

            for i in range (queueLen):

                node = q.popleft()
                levelOrderList.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            list.append (levelOrderList)
        return list    

    
