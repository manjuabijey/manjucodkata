pri=int(input())
for i in range(2,pri):
    if(pri%i==0):
        print("no")
        break
else:
    print("yes")