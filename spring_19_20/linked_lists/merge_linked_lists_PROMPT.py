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