# Merge two sorted linked lists
# Return a sorted linked list
# EX:
#  [1]->[2]->[2] -> None
#  [1]->[3]->[4]->[6] -> None
# OUT:
#  [1]->[1]->[2]->[2]->[3]->[4]->[6]->None
# Definition for singly-linked list.  
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # Use print(node) to check your work
    def __str__(self):
        values = [str(self.val)]
        cur = self.next
        while cur is not None:
            values.append(str(cur.val))
            cur = cur.next
        return "[" + "]->[".join(values) + "]"


# head([1]->)[1]->[2]->[2]->[3]->[4]->[6] -> None
#            cur
def mergeLL(l1, l2):
    # merge sorted lists and return head
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    # - Step through both lists (while) (two references)
    head = None
    cur = head
    while l1 is not None and l2 is not None:
        #   - Compare l1 to l2
        if l1.val < l2.val:
            #   - Take the lesser and add to result list
            if head is None:
                head = l1
                cur = head
            else:
                cur.next = l1
                cur = cur.next
            #   - Advance the lesser reference (node->next)
            l1 = l1.next
        else:
            if head is None:
                head = l2
                cur = head
            else:
                cur.next = l2
                cur = cur.next
            l2 = l2.next
    #   - If either is None, append the rest of the other list
    if l1 is None: 
        cur.next = l2
    else:
        cur.next = l1

    return head


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(2)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(6)

print("Starting Lists:")
print(l1)
print(l2)
print("Merged List:")
result = mergeLL(l1, l2)
print(result)