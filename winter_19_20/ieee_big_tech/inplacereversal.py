def in_place_reversal(L):
    ptr1 = 0
    ptr2 = len(L) - 1

    while ptr1 < ptr2:
        temp = L[ptr1]
        L[ptr1] = L[ptr2]
        L[ptr2] = temp
        ptr1 += 1
        ptr2 -= 1

L = ["cat", "duck", "dog", "rabbit", "squirrel"]
print(L)
in_place_reversal(L)
print(L)