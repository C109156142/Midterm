s1=""
n=input("輸入值為:").split(",")
n.sort()
m = sorted(n, reverse = True)
minn=int(s1.join(n))
maxx=int(s1.join(m))
print("最大值數列與最小值數列差值為:"+str(maxx-minn))
