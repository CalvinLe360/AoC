lengths = [187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216]

chash = list(range(256))
pointer = 0
skipSize = 0

for x in range(len(lengths)):
    if lengths[x] <= 1:
        pointer += lengths[x] + skipSize
        skipSize += 1 
        continue

    subarray = []
    for i in range(lengths[x]):
        subarray.append(chash[(pointer + i) % len(chash)])
    subarray.reverse()
    for i in range(lengths[x]):
        chash[(pointer + i) % len(chash)] = subarray[i]
    
    pointer += lengths[x] + skipSize
    skipSize += 1

print(chash[0] * chash[1])