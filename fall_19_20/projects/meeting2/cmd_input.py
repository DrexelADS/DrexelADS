from enum import Enum

from calculator import calculator

class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

    def printll(self):
        curNode = self
        while curNode.next is not None:
            print(f"{curNode.value} -> ", end="")
            curNode = curNode.next

        print(f"{curNode.value} -> None")


class OPCODE(Enum):
    ADD = 0
    SUBTRACT = 1
    MULTIPLY = 2
    DIVIDE = 3
    SPECIAL = 4


def build_linked_list(value):
    head = None
    curNode = None
    remaining = value
    while remaining % 10 > 0 or remaining // 10 > 0:
        newnode = Node(remaining % 10)

        if head is None:
            head = newnode
            curNode = head
        else:
            curNode.next = newnode
            curNode = newnode

        remaining //= 10

    return head


def operation_lookup(opcode):
    if opcode == "+":
        return OPCODE.ADD
    elif opcode == "-":
        return OPCODE.SUBTRACT
    elif opcode == "*" or opcode == "x":
        return OPCODE.MULTIPLY
    elif opcode == "/":
        return OPCODE.DIVIDE

    return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 4:
        val1 = sys.argv[1]
        val2 = sys.argv[3]
        op = operation_lookup(sys.argv[2])

        if op is None:
            print("Bad Op")
            exit()

        ll1 = build_linked_list(int(val1))
        ll2 = build_linked_list(int(val2))

        print("Inputs:\n\t", end="")
        ll1.printll()
        print("\t", end="")
        ll2.printll()
        print("\t", end="")
        print(op)

        print("BEGIN CALCULATOR")
        calculator(ll1, ll2, op)

    else:
        print("Bad Input")
        exit()
