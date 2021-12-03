import fileinput

lines = list(map(int, fileinput.input()))

# Part 1
print(sum(lines[i] > lines[i-1] for i in range(1, len(lines))))

# Part 2
print(sum(lines[i] > lines[i-3] for i in range(3, len(lines))))

# Since the windows share two elements, we really only need to compare
# the last element of the second window with the first element of the
# first window.
# 0 1 2 
#   1 2 3