
class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None


head = LinkedListNode(0)
middle = LinkedListNode(1)
tail = LinkedListNode(2)

head.next = middle
middle.next = tail
