# Find the sum of this tree
#         5
#    2        10
# 21   31    -   1 

class TreeNode:
    def __init__(self, i):
        self.val = i
        self.left = None
        self.right = None


root = TreeNode(5)
root.left = TreeNode(2)
root.left.left = TreeNode(21)
root.left.right = TreeNode(31)
root.right = TreeNode(10)
root.right.right = TreeNode(1)

# What can we do to solve the sum of the tree?
#   - Add the left and right trees
# What can we do to solve those subproblems
#   - Add THEIR left and right trees
# What is the smallest problem we have to solve?
#   - When the node is None, it's value is zero
# How do we combine the solutions of each subproblem
#   - Add together children and self


def sum_of_tree(root):
    if root is None:
        return 0

    total = root.val + sum_of_tree(root.left) + sum_of_tree(root.right)

    return total


print(sum_of_tree(root))












