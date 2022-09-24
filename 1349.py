numA = []
numB = []
numC = []
a = 0
b = 0
c = 0

am = int(input())
for i in input().split():
    numA.append(int(i))

bm = int(input())
for i in input().split():
    numB.append(int(i))


cm = int(input())
for i in input().split():
    numC.append(int(i))

kol = 0

while 1:
    while numA[a] == numB[b] == numC[c]:
        kol += 1
        a += 1
        b += 1
        c += 1
        if (a == am) or (b == bm) or (c == cm):
            break

    if (a == am) or (b == bm) or (c == cm):
        break

    if numA[a] == min(numA[a], numB[b], numC[c]):
        a += 1
    elif numB[b] == min(numA[a], numB[b], numC[c]):
        b += 1
    elif numC[c] == min(numA[a], numB[b], numC[c]):
        c += 1

    if (a == am) or (b == bm) or (c == cm):
        break

print(kol)