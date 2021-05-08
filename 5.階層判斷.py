
m=int(input("請輸入階乘值M:"))
n = i = 1
while (i<=m):
    i*=n
    n+=1
print("超過M為"+str(m)+"的最小階層N值為:"+str(n-1))
