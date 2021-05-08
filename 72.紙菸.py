n=int(input("請輸入n："))
k=int(input("請輸入k："))
if k>1:
    ans=n//k
else:
    ans=0
if ans>1:
    ans1=ans//k
else:    
    ans1=0
ans2=ans1+ans+n
print("Peter可以抽%d支紙菸" % (ans2))