A = 591
B = 393
judge = 0

# Part 1
# for _ in range(40000000):
#     A = (A * 16807) % 2147483647
#     B = (B * 48271) % 2147483647
#     if str(bin(A))[2:].zfill(32)[-16:] == str(bin(B))[2:].zfill(32)[-16:]:
#         judge += 1

# print(judge)

# Part 2
aOut = []
bOut = []

while len(aOut) != 5000000:
    A = (A * 16807) % 2147483647
    if A % 4 == 0:
        aOut.append(A)

while len(bOut) != 5000000:
    B = (B * 48271) % 2147483647
    if B % 8 == 0:
        bOut.append(B)

for i in range(len(aOut)):
    if str(bin(aOut[i]))[2:].zfill(32)[-16:] == str(bin(bOut[i]))[2:].zfill(32)[-16:]:
        judge += 1

print(judge)