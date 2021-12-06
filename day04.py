import sys
from collections import defaultdict
from itertools import chain
from copy import deepcopy

with open(sys.argv[1]) as f:
    chunks = f.read().split('\n\n')

def makeBoard(chunk):
    return [[[int(e), False] for e in line.split()] 
            for line in chunk.split('\n')]

def updateLookup(i, board, lookup):
    for j, line in enumerate(board):
        for k, (num, _) in enumerate(line):
            lookup[num].append((i, j, k))

def checkBoard(board):
    h, w = len(board), len(board[0])
    rows = [[board[j][k][1] for k in range(w)]
                for j in range(h)]
    cols = [[board[j][k][1] for j in range(h)] 
                for k in range(w)]
    return any(all(x) for x in chain(rows, cols))

def checkBoards(boards, winners):
    for i, board in enumerate(boards):
        if checkBoard(board) and i not in winners:
            return i
    return None

def updateBoards(boards, num, lookup):
    for coord in lookup[num]:
        i, j, k = coord
        boards[i][j][k][1] = True

def getUnmarked(board):
    falses = filter(lambda e: e[1] == False, chain(*board))
    values = map(lambda e: e[0], falses)
    return values

nums = list(map(int, chunks[0].split(',')))
boards = list(map(makeBoard, chunks[1:]))
lookup = defaultdict(list)
for i, board in enumerate(boards):
    updateLookup(i, board, lookup) 

def part1(nums, boards, lookup, winners=set()):
    while True:
        num = nums.pop()
        updateBoards(boards, num, lookup)
        winner = checkBoards(boards, winners)
        if winner is not None:
            unmarked = getUnmarked(boards[winner])
            return sum(unmarked) * num, winner

def part2(nums, boards, lookup):
    winners = set()
    while len(boards) - len(winners) > 0:
        xNums = nums[:]
        result, winner = part1(xNums, boards, lookup, winners)
        winners.add(winner)
    return result

revNums = list(reversed(nums))
result, _ = part1(revNums, deepcopy(boards), lookup)
print(result)

revNums = list(reversed(nums))
result = part2(revNums, deepcopy(boards), lookup)
print(result)