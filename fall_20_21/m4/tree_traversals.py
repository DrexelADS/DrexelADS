class Node:
    """A very simple binary tree node"""

    def __init__(self, val=None):
        """Create a new node with default left and right branches set to None"""
        self.left = None
        self.right = None
        self.val = val


# Create the following tree
#    3
#  2   1
# 0 4 5 6

# Note: This is the same order of a Depth-First Search!
root = Node(3)
root.left = Node(2)
root.left.left = Node(0)
root.left.right = Node(4)
root.right = Node(1)
root.right.left = Node(5)
root.right.right = Node(6)


def dfs(root, val) -> bool:
    """Simple depth-first search for a value"""

    # if we hit one of these two conditions, we no longer want to
    # keep searching this part of the tree
    if root is None:
        return False

    if root.val == val:
        return True

    # we only want to return True if we found the value, we don't want
    # to return false because then we can't search the other branch
    if dfs(root.left, val):
        return True

    if dfs(root.right, val):
        return True

    # search failed, return false
    return False


def bfs(root, val, queue=None) -> bool:
    """Simple breadth-first search for a value"""

    # if we found the value, we're done! otherwise keep going
    if root.val == val:
        return True

    # our queue starts as None, we'll make one object to use
    # in recursive calls
    if queue is None:
        queue = []

    # check for children, if we find them, add them to the queue
    # an optimization exists here to check values before appending
    # which could save you from processing an extra level of the tree
    if root.left is not None:
        queue.append(root.left)

    if root.right is not None:
        queue.append(root.right)

    # take each item from the queue and recursively run a bfs on them
    # while this works fine recursively, an iterative approach could
    # make more sense here depending on your data, system, and preferences
    while len(queue) > 0:
        node = queue.pop(0)
        if bfs(node, val, queue):
            return True

    # we didn't find anything, return false
    return False
