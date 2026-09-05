# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftheight=self.height(root.left)
        rightheight=self.height(root.right)
        diameter=leftheight+rightheight
        max_dia = max(self.diameterOfBinaryTree(root.left),
                  self.diameterOfBinaryTree(root.right))
        return max(diameter,max_dia)
    def height(self,root:Optional[TreeNode])->int:
        if not root:
            return 0
        return max(self.height(root.left),self.height(root.right))+1


