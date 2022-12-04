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

pointerA = 0
pointerB = 0
pointerSentCounterA = [0]
pointerSentCounterB = [0]

registerA = {
    "p": 0
}
registerAIncoming = []

registerB = {
    "p": 1
}
registerBIncoming = []

def parseInstruction(instructions, register, programSend: list, programReceive: list, sendCounter: list):
    ins = instructions.split()
    if ins[1] not in register:
        register[ins[1]] = 0

    print(ins)

    value = 0
    if len(ins) > 2:
        if ins[2].lstrip("-").isnumeric():
            value = int(ins[2])
        else:
            if ins[2] not in register:
                register[ins[2]] = 0
            value = register[ins[2]]
    
    if ins[0] == "set":
        register[ins[1]] = value
    if ins[0] == "add":
        register[ins[1]] += value
    if ins[0] == "mul":
        register[ins[1]] *= value
    if ins[0] == "mod":
        register[ins[1]] = register[ins[1]] % value
    if ins[0] == "snd":
        if ins[1].lstrip("-").isnumeric():
            programSend.append(int(ins[1]))
        else:
            programSend.append(register[ins[1]])
        sendCounter[0] += 1
    if ins[0] == "rcv":
        if len(programReceive) == 0:
            return 0
        register[ins[1]] = programReceive.pop(0)
    if ins[0] == "jgz" and register[ins[1]] > 0:
        return value

    return 1

maxRuntime = 20000
runtime = 0
while pointerA < len(instructions) and pointerB < len(instructions) and runtime < maxRuntime:
    tempA = pointerA
    tempB = pointerB

    pointerA += parseInstruction(instructions[pointerA], registerA, registerBIncoming, registerAIncoming, pointerSentCounterA)
    pointerB += parseInstruction(instructions[pointerB], registerB, registerAIncoming, registerBIncoming, pointerSentCounterB)

    if tempA == pointerA and tempB == pointerB:
        break

    runtime += 1

print(pointerSentCounterB)