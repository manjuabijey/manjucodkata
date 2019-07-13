no=input()
s=0
for i in range(len(num)):
   s+=pow(int(no[i]),3)
if str(s)==no:
  print("yes")
else: 
  print("no")