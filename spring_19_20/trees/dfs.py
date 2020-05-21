from tree import TreeNode

def dfs(node, val):
    # start at node
    # check if self's value is what we want
    if node == None:
        return None
    if node.val == val:
        # if it is, return
        return node
    # if not, go left
    dfs_left = dfs(node.left, val)
    if dfs_left is not None:
        return dfs_left
    # if left doesn't have it, go right
    dfs_right = dfs(node.right, val)
    # if right doesn't have it, no one does
    return dfs_right


root = TreeNode(10)
root.insert(5)
root.insert(20)
root.insert(4)
root.insert(7)

#       10
#   5       20
# 4   7

search = dfs(root, 7)
print(search.val)