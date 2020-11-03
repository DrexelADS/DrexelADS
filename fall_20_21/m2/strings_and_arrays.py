# 0) String Building

## Bad Way
bad_str_building = "Some string"

for i in range(10):
    bad_str_building += f" -- {i}"

print(bad_str_building)

## Good Way
good_str_building = []
good_str_building.append("Some string")

for i in range(10):
    good_str_building.append(f" -- {i}")

good_str = "".join(good_str_building)
print(good_str)

# 1) Reverse a String

## First Approach
# take the input string
# make a new string
# start at the end of the original string
# copy each character into the new string
#
# "tacos"
# "socat"
def first_reverse(orig: str):
    reverse_list = []
    for i in range(len(orig)):
        end_index = len(orig) - i - 1
        reverse_list.append(orig[end_index])

    reversed_str = "".join(reverse_list)
    return reversed_str

print(first_reverse("tacos"))

## In-Place Approach
# most helpful with array inputs
# because strings are immutable (can't do inplace)
#
# take input arr
# create 2 ptrs,
#   1 to the front of the arr, 1 to the back
# while ptr1 < ptr2:
#   store ptr1's char in a temp value
#   move ptr2's char to ptr1's spot
#   move temp val to ptr2's spot
#   ptr1 += 1; ptr2 -= 1
#
# "socat"
#    1
#    2
# tmp = a
def inplace_reverse(orig: list):
    ptr1 = 0
    ptr2 = len(orig) - 1 

    while ptr1 < ptr2:
        tmp = orig[ptr1]
        orig[ptr1] = orig[ptr2]
        orig[ptr2] = tmp
        ptr1 += 1
        ptr2 -= 1

    return orig

print(inplace_reverse(['t', 'a', 'c', 'o', 's']))
