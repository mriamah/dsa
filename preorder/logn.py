def preOrder(self, root):
        if root.left is None and root.right is None:
            return [root.data]
        elif root.left is None and root.right:
            return [root.right.data] + self.preOrder(root.right) 
        elif root.right and root.left:
            return [root.data] + self.preOrder(root.left) + [root.right.data]
        else:
            return [root.data] + self.preOrder(root.left) 
