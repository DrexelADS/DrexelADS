class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val) -> "TreeNode":
        # start at top of tree
        if val > self.val: # Insert on right
            if self.right is not None:
                return self.right.insert(val)
            else:
                self.right = TreeNode(val)
                return self.right
        else: # Insert on left
            if self.left is not None:
                return self.left.insert(val)
            else:
                self.left = TreeNode(val)
                return self.left