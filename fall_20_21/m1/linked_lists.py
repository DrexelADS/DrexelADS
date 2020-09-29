class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f"({str(self.val)})"


def ll_contains(head, n):
    ptr = head
    while ptr is not None:
        if n == ptr.val:
            return True
        ptr = ptr.next

    return False


def ll_append(head, n):
    ptr = head
    while ptr.next is not None:
        ptr = ptr.next

    ptr.next = Node(n)


def ll_insert(head, n, index):
    if index == 0:
        new_head = Node(n)
        new_head.next = head
        return new_head

    ptr = head
    i = 1
    while ptr is not None:
        if i == index:
            break

        ptr = ptr.next
        i += 1

    if ptr is None:
        raise Error("Index exceeds list size")

    temp = ptr.next
    ptr.next = Node(n)
    ptr.next.next = temp


def ll_remove(head, n):
    if n == head.val:
        head = head.next
        return head

    ptr = head
    while ptr.next is not None:
        if n == ptr.next.val:
            ptr.next = ptr.next.next
        ptr = ptr.next

    return head


def ll_find_middle(head):
    slow_ptr = head
    fast_ptr = head

    while (fast_ptr.next is not None
        and fast_ptr.next.next is not None):
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr


def ll_print(head):
    ptr = head
    while ptr is not None:
        print(f"{ptr.val}->", end="")
        ptr = ptr.next

    print("None")


head = Node(1)
head.next = Node(3)
head.next.next = Node(5)
ll_print(head)

print("Appending 7")
ll_append(head, 7)

ll_print(head)

middle_node = ll_find_middle(head)
print("Removing", middle_node)
ll_remove(head, middle_node.val)

ll_print(head)

print("Adding 4 at index 1")
ll_insert(head, 4, 1)
ll_print(head)

for i in range(10):
    print(f"{i} in LL: {ll_contains(head, i)}")