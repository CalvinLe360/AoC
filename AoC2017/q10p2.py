inputlengths = "187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216"
lengths = [ord(x) for x in inputlengths]
lengths.extend([17, 31, 73, 47, 23])

chash = list(range(256))
pointer = 0
skipSize = 0

for _ in range(64):
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

denseHash = []
for i in range(16):
    block = chash[i * 16: (i+1) * 16]
    target = block[0]
    for j in range(1, 16):
        target = target ^ block[j]
    denseHash.append(target)

print(''.join([str(hex(x))[2:4] for x in denseHash]))