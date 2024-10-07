# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.hash = dict()
        def buildHash(inorder): # hash the inorder as we look up position of preorder root node and partition 
                                # the array based on that
            for i in range(len(inorder)):
                self.hash[inorder[i]] = i

        def helper(preStart,preEnd,inStart,inEnd):
            # base condition
            if(inStart>inEnd):
                return None
            # pick the node from preorder array
            root = TreeNode(preorder[preStart])
            # get hash position from root value
            pos = self.hash[root.val]
            # number of elements to its left
            leftElements = pos-inStart
            root.left = helper(preStart+1,preStart+leftElements,inStart,pos-1)
            root.right = helper(preStart+leftElements+1,preEnd,pos+1,inEnd)
            return root

        buildHash(inorder)
        preEnd = len(preorder)-1 # end of the preorder array
        inEnd = len(inorder)-1 # end of the inorder array
        root = helper(0,preEnd,0,inEnd) 
        return root
            
