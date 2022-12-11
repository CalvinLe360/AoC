from functools import reduce
import math


input = [
"Monkey 0:",
"  Starting items: 76, 88, 96, 97, 58, 61, 67",
"  Operation: new = old * 19",
"  Test: divisible by 3",
"    If true: throw to monkey 2",
"    If false: throw to monkey 3",
"",
"Monkey 1:",
"  Starting items: 93, 71, 79, 83, 69, 70, 94, 98",
"  Operation: new = old + 8",
"  Test: divisible by 11",
"    If true: throw to monkey 5",
"    If false: throw to monkey 6",
"",
"Monkey 2:",
"  Starting items: 50, 74, 67, 92, 61, 76",
"  Operation: new = old * 13",
"  Test: divisible by 19",
"    If true: throw to monkey 3",
"    If false: throw to monkey 1",
"",
"Monkey 3:",
"  Starting items: 76, 92",
"  Operation: new = old + 6",
"  Test: divisible by 5",
"    If true: throw to monkey 1",
"    If false: throw to monkey 6",
"",
"Monkey 4:",
"  Starting items: 74, 94, 55, 87, 62",
"  Operation: new = old + 5",
"  Test: divisible by 2",
"    If true: throw to monkey 2",
"    If false: throw to monkey 0",
"",
"Monkey 5:",
"  Starting items: 59, 62, 53, 62",
"  Operation: new = old * old",
"  Test: divisible by 7",
"    If true: throw to monkey 4",
"    If false: throw to monkey 7",
"",
"Monkey 6:",
"  Starting items: 62",
"  Operation: new = old + 2",
"  Test: divisible by 17",
"    If true: throw to monkey 5",
"    If false: throw to monkey 7",
"",
"Monkey 7:",
"  Starting items: 85, 54, 53",
"  Operation: new = old + 3",
"  Test: divisible by 13",
"    If true: throw to monkey 4",
"    If false: throw to monkey 0",
"",
]
inputExample = [
"Monkey 0:",
"  Starting items: 79, 98",
"  Operation: new = old * 19",
"  Test: divisible by 23",
"    If true: throw to monkey 2",
"    If false: throw to monkey 3",
"",
"Monkey 1:",
"  Starting items: 54, 65, 75, 74",
"  Operation: new = old + 6",
"  Test: divisible by 19",
"    If true: throw to monkey 2",
"    If false: throw to monkey 0",
"",
"Monkey 2:",
"  Starting items: 79, 60, 97",
"  Operation: new = old * old",
"  Test: divisible by 13",
"    If true: throw to monkey 1",
"    If false: throw to monkey 3",
"",
"Monkey 3:",
"  Starting items: 74",
"  Operation: new = old + 3",
"  Test: divisible by 17",
"    If true: throw to monkey 0",
"    If false: throw to monkey 1",
]

monkeys = []

for i in range(0, len(input), 7):
    newMonkey = {}
    newMonkey["items"] = [int(x) for x in input[i+1].lstrip("  Starting items: ").split(", ")]
    newMonkey["operation"] = input[i+2].lstrip("  Operation: new = old ").split()
    newMonkey["divisible"] = int(input[i+3].lstrip("  Test: divisible by "))
    newMonkey["trueMonkey"] = int(input[i+4].lstrip("    If true: throw to monkey "))
    newMonkey["falseMonkey"] = int(input[i+5].lstrip("    If false: throw to monkey "))
    newMonkey["actions"] = 0

    # print(newMonkey)
    monkeys.append(newMonkey)

divisibleModulo = reduce(lambda a,b: a * b, [x["divisible"] for x in monkeys])
for _ in range(10000):
    for i in range(len(monkeys)):
        monkey = monkeys[i]

        while len(monkey["items"]) > 0:
            item = monkey["items"].pop(0)

            value = 0
            if monkey["operation"][1].isnumeric():
                value = int(monkey["operation"][1])
            else:
                value = item

            if monkey["operation"][0] == "*":
                item *= value
            elif monkey["operation"][0] == "+":
                item += value

            item = item % divisibleModulo

            if item % monkey["divisible"] == 0:
                monkeys[monkey["trueMonkey"]]["items"].append(item)
            else:
                monkeys[monkey["falseMonkey"]]["items"].append(item)

            monkey["actions"] += 1

monkeyBusiness = sorted([x["actions"] for x in monkeys], reverse=True)

print(monkeyBusiness[0] * monkeyBusiness[1], monkeyBusiness)