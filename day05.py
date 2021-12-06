import fileinput
import re
from collections import defaultdict

lineRegex = r'(\d+),(\d+) -> (\d+),(\d+)'

def getLine(line):
    coords = re.match(lineRegex, line).groups()
    return tuple(map(int, coords))

def getDxDy(line):
    x1, y1, x2, y2 = line
    dx = 0 if x1 == x2 else 1 if x2 > x1 else -1
    dy = 0 if y1 == y2 else 1 if y2 > y1 else -1
    return (dx, dy)

def isStraitLine(line):
    x1, y1, x2, y2 = line
    return x1 == x2 or y1 == y2

def genPoints(line):
    x1, y1, x2, y2 = line
    x, y = x1, y1
    dx, dy = getDxDy(line)
    points = [(x, y)]
    while not (x == x2 and y == y2):
        x += dx
        y += dy
        points.append((x, y))
    return points

def calcOverlap(lines):
    counts = defaultdict(int)
    for line in lines:
        for point in genPoints(line):
            counts[point] += 1
    return len(list(filter(lambda c: c > 1, counts.values())))

allLines = list(map(getLine, fileinput.input())) 
lines = list(filter(isStraitLine, allLines))

# Part 1
result = calcOverlap(lines)
print(result)

# Part 2
result = calcOverlap(allLines)
print(result)
