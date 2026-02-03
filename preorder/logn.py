def preOrder(self, root):
	if root.left is None and root.right is None:
            return [root.data]
        if root.left is None and root.right:
            return [root.data] + self.preOrder(root.right) 
        if root.right and root.left:
            return [root.data] + self.preOrder(root.left) + self.preOrder(root.right)
        return [root.data] + self.preOrder(root.left) 
