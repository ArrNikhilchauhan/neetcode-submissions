# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=float('-inf')
        def backtrack(node):
            if not node:
                return 0
            
            left=max(backtrack(node.left),0)
            right=max(backtrack(node.right),0)

            current_sum=node.val+left+right
            self.ans=max(self.ans,current_sum)

            return node.val+max(left,right)
        backtrack(root)
        return self.ans
            

        