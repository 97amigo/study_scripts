l_st = []
with open('data.txt', 'r') as inf:
	for line in inf:
		l_st.append([float(i) for i in line.strip().split(',')])

for el in l_st:
	print((int(el[0])+int(el[1])+int(el[2]))/3)
sum = 0
for i in range(3):
	for el in l_st:
		sum += int(el[i+1])
	print(sum/len(l_st), end=' ')
	sum = 0
