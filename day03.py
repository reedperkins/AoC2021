import fileinput

nums = list(tuple(x.strip()) for x in fileinput.input())
numLength = len(nums[0])

def ones(lst, i):
    return sum(n[i] == '1' for n in lst)

# Part 1
gamma = epsilon = ''
half = len(nums) / 2
for i in range(numLength):
    gamma += '1' if int(ones(nums, i) > half) == 1 else '0'
    epsilon += '1' if int(ones(nums, i) > half) == 0 else '0'
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma * epsilon)

# Part 2
def takeMcb(lst, i, mcb):
    return list(filter(lambda n: int(n[i]) == mcb, lst))

def takeLcb(lst, i, mcb):
    return list(filter(lambda n: int(n[i]) != mcb, lst))

def part2(nums, fn):
    while nums:
        for i in range(numLength):
            mcb = int(ones(nums, i) >= len(nums) / 2)
            nums = fn(nums, i, mcb)
            if len(nums) == 1:
                return int(''.join(nums[0]), 2)

oxy = part2(nums, takeMcb)
c02 = part2(nums, takeLcb)
print(oxy * c02)

# Functional version. Cooler (no explicit loops!), but less readable)
from functools import partial, reduce
def reducer(fn, nums, i):
    if len(nums) == 1:
        return nums
    mcb = int(ones(nums, i) >= len(nums) / 2)
    return fn(nums, i, mcb)

def toInt(num):
    return int(''.join(num), 2)

def part2(nums, fn):
    nums = reduce(fn, range(numLength), nums)
    return toInt(nums[0])

oxy = part2(nums, partial(reducer, takeMcb))
c02 = part2(nums, partial(reducer, takeLcb))
print(oxy * c02)