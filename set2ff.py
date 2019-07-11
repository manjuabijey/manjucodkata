n,ma=map(int,input().split())
for i in range(n+1,ma):
	for k in range(2,i):
		if(i%k==0):
			break
	else:
		print(i,end=" ")