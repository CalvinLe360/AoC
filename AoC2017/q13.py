firewalls = [
"0: 4",
"1: 2",
"2: 3",
"4: 4",
"6: 8",
"8: 5",
"10: 6",
"12: 6",
"14: 10",
"16: 8",
"18: 6",
"20: 9",
"22: 8",
"24: 6",
"26: 8",
"28: 8",
"30: 12",
"32: 12",
"34: 12",
"36: 12",
"38: 10",
"40: 12",
"42: 12",
"44: 14",
"46: 8",
"48: 14",
"50: 12",
"52: 14",
"54: 14",
"58: 14",
"60: 12",
"62: 14",
"64: 14",
"66: 12",
"68: 12",
"72: 14",
"74: 18",
"76: 17",
"86: 14",
"88: 20",
"92: 14",
"94: 14",
"96: 18",
"98: 18",
]
firewallsA = [
"0: 3",
"1: 2",
"4: 4",
"6: 4",
]

severity = 0
for i in range(len(firewallsA)):
    depth, layers = firewallsA[i].split(": ")
    depth, layers = int(depth), int(layers)
    currentCycle = depth % ((layers - 1) * 2)
    
    if currentCycle == 0:
        severity += layers * depth

print(severity)

delay = 0
caught = True
while caught:
    delay += 1
    caught = False

    for i in range(len(firewalls)):
        depth, layers = firewalls[i].split(": ")
        depth, layers = int(depth), int(layers)
        currentCycle = (depth + delay) % ((layers - 1) * 2)
        
        if currentCycle == 0:
            caught = True
            break

print(delay)