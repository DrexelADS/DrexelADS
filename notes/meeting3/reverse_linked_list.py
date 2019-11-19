from stack import Node, Stack


def reverse_linked_list(linkedList):
    stack = Stack()

    curNode = linkedList
    while curNode.next is not None:
        stack.push(curNode)

    head = curNode  # last node is now head
    while stack.peek() is not None:
        curNode.next = stack.pop()
        curNode = curNode.next

    curNode.next = None
    return head


linkedList = Node(0)
linkedList.add_node(1)
linkedList.add_node(2)
linkedList.add_node(3)
linkedList.add_node(4)

newHead = reverse_linked_list(linkedList)