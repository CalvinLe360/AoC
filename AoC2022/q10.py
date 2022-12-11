import math


input = [
"addx 1",
"addx 4",
"addx 1",
"noop",
"addx 4",
"addx 3",
"addx -2",
"addx 5",
"addx -1",
"noop",
"addx 3",
"noop",
"addx 7",
"addx -1",
"addx 1",
"noop",
"addx 6",
"addx -1",
"addx 5",
"noop",
"noop",
"noop",
"addx -37",
"addx 7",
"noop",
"noop",
"noop",
"addx 5",
"noop",
"noop",
"noop",
"addx 9",
"addx -8",
"addx 2",
"addx 5",
"addx 2",
"addx 5",
"noop",
"noop",
"addx -2",
"noop",
"addx 3",
"addx 2",
"noop",
"addx 3",
"addx 2",
"noop",
"addx 3",
"addx -36",
"noop",
"addx 26",
"addx -21",
"noop",
"noop",
"noop",
"addx 3",
"addx 5",
"addx 2",
"addx -4",
"noop",
"addx 9",
"addx 5",
"noop",
"noop",
"noop",
"addx -6",
"addx 7",
"addx 2",
"noop",
"addx 3",
"addx 2",
"addx 5",
"addx -39",
"addx 34",
"addx 5",
"addx -35",
"noop",
"addx 26",
"addx -21",
"addx 5",
"addx 2",
"addx 2",
"noop",
"addx 3",
"addx 12",
"addx -7",
"noop",
"noop",
"noop",
"noop",
"noop",
"addx 5",
"addx 2",
"addx 3",
"noop",
"noop",
"noop",
"noop",
"addx -37",
"addx 21",
"addx -14",
"addx 16",
"addx -11",
"noop",
"addx -2",
"addx 3",
"addx 2",
"addx 5",
"addx 2",
"addx -15",
"addx 6",
"addx 12",
"addx -2",
"addx 9",
"addx -6",
"addx 7",
"addx 2",
"noop",
"noop",
"noop",
"addx -33",
"addx 1",
"noop",
"addx 2",
"addx 13",
"addx 15",
"addx -21",
"addx 21",
"addx -15",
"noop",
"noop",
"addx 4",
"addx 1",
"noop",
"addx 4",
"addx 8",
"addx 6",
"addx -11",
"addx 5",
"addx 2",
"addx -35",
"addx -1",
"noop",
"noop",
]

inputPointer = 0
register = 1
signalStrengths = 0

executing = False

pixels = {}

for i in range(1, 241):
    instruction = input[inputPointer].split()
    # Part 1
    if (i - 20) % 40 == 0:
        # print(i, register, register * i)
        signalStrengths += register * i

    # Part 2
    pixelX = (i - 1) % 40
    pixelY = int(math.floor((i - 1) / 40))
    # print(i, pixelX, pixelY)

    if abs(pixelX - register) <= 1:
        pixels[str(pixelX) + "," + str(pixelY)] = True

    if executing:
        register += int(instruction[1])
        inputPointer = (inputPointer + 1) % len(input)
        executing = False
        # print(i, register)
    elif instruction[0] == "noop":
        inputPointer = (inputPointer + 1) % len(input)
    else:
        executing = True

print(signalStrengths)

for y in range(6):
    for x in range(0, 40):
        if str(x) + "," + str(y) in pixels:
            print("#", end="")
        else:
            print(" ", end="")
    print()