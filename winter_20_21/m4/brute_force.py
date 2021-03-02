# BRUTE FORCE APPROACH
# given 2 + x = 10, what is x?

def problem(x):
    # Returns True if solves, else False
    return 2 + x == 10


# what are the possible solutions?
# - ALL INTEGER NUMBERS

# (how long are we willing to wait - -100 to 100)

# Try all possible solutions

for i in range(-10000, 10001):
    print(i)
    if problem(i):
        break

print(f"{i} is the solution")
