
class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def add_node_iterative(self, value):
        tailNode = self

        # Iterate through until last node
        while tailNode.next is not None:
            tailNode = tailNode.next

        # Append new node
        tailNode.next = LinkedListNode(value)
        return tailNode.next


head_iter = LinkedListNode(0)
middle_iter = head_iter.add_node_iterative(1)
tail_iter = head_iter.add_node_iterative(2)
