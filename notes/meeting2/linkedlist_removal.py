
class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def remove_node_iterative(self, value):

        # Move the head to the next value
        if self.value == value:
            head = self.next
            self.next = None  # !!
            return head

        # Iterate and find the value
        curNode = self

        while curNode.next.value != value:
            curNode = curNode.next

            # Value not in list
            if curNode is None:
                return self

        # Drop the value from the list
        curNode.next = curNode.next.next
        return self


head = LinkedListNode(0)
middle_1 = LinkedListNode(1)
middle_2 = LinkedListNode(2)
tail = LinkedListNode(3)


head.next = middle_1
middle_1.next = middle_2
middle_2.next = tail


head.remove_node_iterative(2)
head.remove_node_iterative(3)
