input = "stpzcrnm"

defragmap = []

for a in range(128):
    inputlengths = input + "-" + str(a)
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

    defragmap.append(''.join([str(bin(x))[2:].zfill(8) for x in denseHash]))

print("used squares ", sum([x.count("1") for x in defragmap]))

defragregions = [["." for _ in range(128)] for __ in range(128)]

regioncount = 0
for y in range(128):
    for x in range(128):
        if defragmap[y][x] == "1" and defragregions[y][x] == ".":
            regioncount += 1
            searchqueue = [[y, x]]

            while(len(searchqueue) > 0):
                searched = searchqueue.pop()
                if defragmap[searched[0]][searched[1]] != "1" or defragregions[searched[0]][searched[1]] != ".": continue

                defragregions[searched[0]][searched[1]] = regioncount
                if searched[0] - 1 >= 0:
                    searchqueue.append([searched[0] - 1, searched[1]])
                if searched[1] - 1 >= 0:
                    searchqueue.append([searched[0], searched[1] - 1])
                if searched[0] + 1 < 128:
                    searchqueue.append([searched[0] + 1, searched[1]])
                if searched[1] + 1 < 128:
                    searchqueue.append([searched[0], searched[1] + 1])


print(defragregions)
print(regioncount)