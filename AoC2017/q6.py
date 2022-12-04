from collections import OrderedDict
import math


banks = [
    4,	1,	15,	12,	0,	9,	9,	5,	5,	8,	7,	3,	14,	5,	12,	3,
]
banksExample = [0, 2, 7, 0]

def solution(bank: list[int]):
    configurations = OrderedDict()
    configurations[''.join([str(x) + "," for x in bank])] = True
    firstEncountered = ""

    while True:
        maxBlocksIndex = bank.index(max(bank))
        blocksFullyDistributed = int(math.floor(bank[maxBlocksIndex] / len(bank)))
        blocksLeftOver = bank[maxBlocksIndex] % len(bank)

        bank[maxBlocksIndex] = 0
        bank = [x + blocksFullyDistributed for x in bank]

        for i in range(blocksLeftOver):
            pointer = (maxBlocksIndex + 1 + i) % len(bank)
            bank[pointer] += 1
        
        newConfiguration = ''.join([str(x) + "," for x in bank])
        # print(newConfiguration)

        if newConfiguration in configurations:
            firstEncountered = newConfiguration
            break
        else:
            configurations[newConfiguration] = True
    
    print(len(configurations))
    print(len(configurations) - list(configurations.keys()).index(firstEncountered))

# solution(banksExample)
solution(banks)