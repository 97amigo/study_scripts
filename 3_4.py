l_st=[]
with open('d:\Petr\Python\input.txt','r') as inf:
	for line in inf:
		l_st.append([i for i in line.strip().split(';')])
		
for el in l_st:
	print((int(el[1])+int(el[2])+int(el[3]))/3)
sum=0
for i in range(3):
	for el in l_st:
		sum+=int(el[i+1])
	print(sum/len(l_st),end=' ')
	sum=0	


		


