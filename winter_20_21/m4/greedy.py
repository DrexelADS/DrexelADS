# Find a large path in a binary tree
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


def large_path(root):
    # Where are we?
    #  - start at the root value
    total = 0

    cur_node = root
    # What are we trying to achieve?
    #  - find a large path from root to leaf

    # What will help us most RIGHT NOW?
    #  - the largest child node from the current node
    while cur_node != None:
        total += cur_node.val

        if (cur_node.left is not None 
            and cur_node.right is not None):
            if cur_node.left.val > cur_node.right.val:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
            continue

        elif cur_node.left is not None:
            cur_node = cur_node.left

        cur_node = cur_node.right

    return total

print(large_path(root))




