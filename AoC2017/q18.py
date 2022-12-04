instructions = [
"set i 31",
"set a 1",
"mul p 17",
"jgz p p",
"mul a 2",
"add i -1",
"jgz i -2",
"add a -1",
"set i 127",
"set p 622",
"mul p 8505",
"mod p a",
"mul p 129749",
"add p 12345",
"mod p a",
"set b p",
"mod b 10000",
"snd b",
"add i -1",
"jgz i -9",
"jgz a 3",
"rcv b",
"jgz b -1",
"set f 0",
"set i 126",
"rcv a",
"rcv b",
"set p a",
"mul p -1",
"add p b",
"jgz p 4",
"snd a",
"set a b",
"jgz 1 3",
"snd b",
"set f 1",
"add i -1",
"jgz i -11",
"snd a",
"jgz f -16",
"jgz a -19",
]

pointer = 0

registers = {}
lastPlayed = {}
recovered = {}

while pointer < len(instructions):
    ins = instructions[pointer].split()
    if ins[1] not in registers:
        registers[ins[1]] = 0
    # print(ins)

    value = 0
    if len(ins) > 2:
        if ins[2].lstrip("-").isnumeric():
            value = int(ins[2])
        else:
            if ins[2] not in registers:
                registers[ins[2]] = 0
            value = registers[ins[2]]
    
    if ins[0] == "set":
        registers[ins[1]] = value
    if ins[0] == "add":
        registers[ins[1]] += value
    if ins[0] == "mul":
        registers[ins[1]] *= value
    if ins[0] == "mod":
        registers[ins[1]] = registers[ins[1]] % value
    if ins[0] == "snd":
        lastPlayed[ins[1]] = registers[ins[1]]
    if ins[0] == "rcv":
        if ins[1] in lastPlayed and lastPlayed[ins[1]] != 0:
            recovered[ins[1]] = lastPlayed[ins[1]]
            break
    if ins[0] == "jgz" and registers[ins[1]] > 0:
        pointer += value - 1

    pointer += 1

print(recovered)
