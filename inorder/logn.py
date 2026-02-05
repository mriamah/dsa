    def inOrder(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.data]
            
        return self.inOrder(root.left) + [root.data] + self.inOrder(root.right)
