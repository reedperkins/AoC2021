import fileinput

nums = list(tuple(x.strip()) for x in fileinput.input())
numLength = len(nums[0])
half = len(nums) / 2

def ones(lst, i):
    return sum(n[i] == '1' for n in lst)

# Part 1
gamma = 0
for i in range(numLength):
    gamma |= (ones(nums, i) > half) << numLength-1-i
epsilon = ~gamma & (2**numLength - 1)
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