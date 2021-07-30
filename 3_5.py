d_st={}
l_st=[]
with open('input.','r') as inf:
	for line in inf:
		l_st=line.strip().split()
		d_st.setdefault(int(l_st[0]),[0,0])[0]+=int(l_st[2])
		d_st.setdefault(int(l_st[0]),[0,0])[1]+=1
print(d_st)
		
for i in range(1,12):
    print(i,d_st[i][0]/d_st[i][1] if i in d_st.keys() else '-')
