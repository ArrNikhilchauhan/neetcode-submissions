# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        path_maximum=float('-inf')
        self.ans=0
        def traverse(node,path_maxi):

            if not node:
                return 

            path_maxi=max(path_maxi,node.val)

            if  path_maxi<=node.val:
                self.ans+=1   
            
            traverse(node.left,path_maxi)
            traverse(node.right,path_maxi)

        traverse(root,path_maximum)

        return self.ans