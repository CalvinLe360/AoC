steps = 314
buffer = []

pointer = 0
for i in range(2018):
    if i == 0:
        buffer.append(0)
        continue

    realSteps = steps % len(buffer)
    pointer = (pointer + realSteps) % len(buffer)
    buffer.insert(pointer + 1, i)
    pointer += 1

    if i == 2017:
        print(buffer[(buffer.index(2017) + 1) % len(buffer)])

# Part 2
afterZero = buffer[1]

for i in range(2018, 50000001):
    realSteps = steps % i
    pointer = (pointer + realSteps) % i
    if(pointer == 0):
        afterZero = i

    pointer += 1

print(afterZero)