import fileinput
from functools import reduce

lines = list(map(int, fileinput.input()))

def countIncrease(total, i):
    return total + 1 if lines[i] > lines[i-1] else total

def countWindowIncrease(total, i):
    return total + 1 if sum(lines[i:i+3]) > sum(lines[i-1:i+2]) else total

# Part 1
print(reduce(countIncrease, range(1, len(lines)), 0))

# Part 2
print(reduce(countWindowIncrease, range(1, len(lines)), 0))