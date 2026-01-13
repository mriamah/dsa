def isSameTree(self, p, q):
    result_left = result_right = False
    if p is None and q is None:
      return True
    elif p and q and p.left is None and q.left is None and q.right is None and p.right is None: # leafs
      return p.val == q.val
    elif p and q and p.val == q.val:
      result_left = self.isSameTree(p.left, q.left)
      result_right = self.isSameTree(p.right, q.right)

    return result_left and result_right
