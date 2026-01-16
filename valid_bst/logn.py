def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True 
        if root.left and (root.val <= root.left.val or \
            (root.left.left and root.val <= root.left.left.val) or
            (root.left.right and root.val <= root.left.right.val)):
            return False
        if root.right and (root.val >= root.right.val or \
            (root.right.right and root.val >= root.right.right.val) or
            (root.right.left and root.val >= root.right.left.val)):
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)
