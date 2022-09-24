import random
import time

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
example = 'stierlitz'
while len(example) < 199999:
    letter = random.choice(letters)
    point = random.randrange(0, len(example))
    example = example[:point] + letter + letter + example[point:]

print(example)
str = example

# str = input()
#
# str = str + '!'
# i = 0
# Nstr = ''
#
# while i < len(str) - 1:
#     if str[i] == str[i + 1]:
#         i += 2
#     else:
#         Nstr += str[i]
#         i += 1
#
# print(Nstr)

start = time.clock()

#str = input()
k = 0
t = []

while k < len(str):
    t.append(str[k])
    if len(t) > 1:
        if t[len(t)-1] == t[len(t)-2]:
            t.pop()
            t.pop()
    k += 1

print(''.join(t))


print("Time:", time.clock() - start)







