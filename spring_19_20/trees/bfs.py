from tree import TreeNode


class Queue:
    def __init__(self):
        self._hidden_list = []

    def enqueue(self, val):
        self._hidden_list.append(val)

    def dequeue(self):
        return self._hidden_list.pop(0)

    def __len__(self):
        return len(self._hidden_list)


def bfs(node, val, queue=Queue()):
    # check if the current value is what we want
    if node.val == val:
        return node

    # if not, add any children we can find to the queue
    if node.left is not None:
        queue.enqueue(node.left)
    if node.right is not None:
        queue.enqueue(node.right)

    # if there's nothing left in the queue, we're outta luck
    if len(queue) == 0:
        return None

    # rerun on the next child we can find
    ## side note: queues take from the front and add the end,
    ##          : unlike lists which typically add and remove 
    ##          : from the end
    next_node = queue.dequeue()  
    return bfs(next_node, val, queue)


root = TreeNode(10)
root.insert(5)
root.insert(20)
root.insert(4)
root.insert(7)
root.insert(21)
root.insert(12)
root.insert(11)
root.insert(1)
root.insert(22)

search = bfs(root, 1)
print(search.val)