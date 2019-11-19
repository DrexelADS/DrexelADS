
class SetOfStacks:

    def __init__(self, maxToast):
        self.stacks = []
        self.maxToast = maxToast
        self.count = 0

    def push(self, value):
        if self.count % self.maxToast == 0:
            self.stacks.append(Stack())
        if len(self.stacks) == 0:
            self.stacks.append(Stack())

        self.stacks[-1].push(value)
        self.count += 1

    def peek(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[-1].peek()

    def pop(self):
        if len(self.stacks) == 0:
            return None

        poppedNode = self.stacks[-1].pop()
        self.count -= 1

        if self.count % self.maxToast == 0:
            self.stacks.pop()

        return poppedNode


    def printSetOfStacks(self):
        # [   STACK 1  ]  [   STACK 2  ]  [   STACK 3  ]
        # [RYE    BREAD]  [PUMPERNICKLE]
        # [WHITE  BREAD]  [WHITE  BREAD]
        # [PUMPERNICKLE]  [BANANA BREAD]
        # [WHITE  BREAD]  [BANANA BREAD]  [PUMPERNICKLE]
        # [BANANA BREAD]  [RYE    BREAD]  [BANANA BREAD]
        for i in range(len(self.stacks)):
            print(f"[   Stack {i}  ]\t", end="")
        print("")

        nodeList = []
        for stack in self.stacks:
            nodeList.append(stack.peek())

        printCounter = 0
        while any(
            [node is not None for node in NodeList]
        ):
            printCounter += 1
            for i in range(len(nodeList)):
                if (
                    (self.count + printCounter) / self.maxToast <= len(self.stacks)
                    and i == len(nodeList)-1
                ):
                    continue

                node = nodeList[i]
                print(f"[{node.value}]\t", end="")
                nodeList[i] = node.next
            print("")





