class Node:  # This is a LinkedListNode!

    def __init__(self, value):
        self.value = value
        self.next = None

    def add_node(self, value):
        curNode = self
        while curNode.next is not None:
            curNode = curNode.next

        curNode.next = Node(value)
        return curNode.next


class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode

    def peek(self):
        return self.top

    def pop(self):
        poppedNode = self.top
        self.top = self.top.next
        return poppedNode

    def pop_value(self, value):
        if self.top.value == value:
            return self.pop()

        curNode = self.top
        while curNode.next is not None:
            if curNode.next.value == value:
                poppedNode = curNode.next
                curNode.next = curNode.next.next
                return poppedNode

        return None
