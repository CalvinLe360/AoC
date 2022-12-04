import math

input = 325489

# Part 1
def stepsCalculator(input):
    ring = math.ceil(math.sqrt(input))
    if ring % 2 == 0: ring += 1
    # print(testInput, ring)

    corners = [ring * ring - (ring - 1) * x for x in range(4, -1, -1)]
    stepsFromCorner = ring-1
    # print(input, corners, stepsFromCorner)

    sideCorners = 0
    for x in range(len(corners)):
        if input <= corners[x]:
            sideCorners = x
            break
    # print(testInput, nearestCorner)

    totalSteps = stepsFromCorner - min(corners[sideCorners] - input, input - corners[sideCorners - 1])
    print(input, totalSteps)

if input == 1:
    print(0)
else:
    stepsCalculator(input)

# Part 2
hashmap = {
    "0,0": 1
}

x, y = 0, 0
velocity = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]
velocityPointer = 0

def sumNearestNeighbours(x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0: continue
            if f'{x-i},{y-j}' in hashmap:
                sum += hashmap.get(f'{x-i},{y-j}')

    return sum

for i in range(2, 400):
    # Info
    ring = math.ceil(math.sqrt(i))
    if ring % 2 == 0: ring += 1
    turnPoints = [ring * ring - (ring - 1) * x for x in range(3, 0, -1)]
    turnPoints.insert(0, (ring - 2) * (ring - 2) + 1)
    
    x += velocity[velocityPointer][0]
    y += velocity[velocityPointer][1]
    if i in turnPoints:
        velocityPointer = (velocityPointer + 1) % len(velocity)

    nearestNeighbourSum = sumNearestNeighbours(x, y)
    hashmap.update({f'{x},{y}': nearestNeighbourSum})

    if nearestNeighbourSum > input:
        print(nearestNeighbourSum)
        break
    