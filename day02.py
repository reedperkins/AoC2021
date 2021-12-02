import fileinput
from functools import reduce

def convertMove(move):
    dir, amt = move.strip().split()
    return (dir, int(amt))

moves = list(map(convertMove, fileinput.input())) 

# Part 1
def reducer(curPos, newPos):
    curDy, curDx = curPos
    dir, amt = newPos
    if dir == 'forward':
        return (curDy, curDx + amt)
    elif dir == 'down':
        return (curDy + amt, curDx)
    else:
        return (curDy - amt, curDx)

finalDx, finalDy = reduce(reducer, moves, (0, 0))
print(finalDx * finalDy)

# Part 2
def reducer2(curPos, newPos):
    curDy, curDx, curAim = curPos
    dir, amt = newPos
    if dir == 'forward':
        newDy = curAim * amt + curDy 
        newDx = curDx + amt
        return (newDy, newDx, curAim)
    elif dir == 'down':
        return (curDy, curDx, curAim + amt)
    else:
        return (curDy, curDx, curAim - amt)

finalDy, finalDx, _ = reduce(reducer2, moves, (0, 0, 0))
print(finalDy * finalDx)