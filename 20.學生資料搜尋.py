num=["123","456","789","321","654"]
name=["Tom","Cat","Nana","Lim","Won"]
obj=["DTGD","CSIE","ASIE","DBA","FDD"]
n=input("輸入查詢學號為:")
b=num.index(n)
a=num[b]
if n==a:
    print("學生資料為:"+str(num[b]+name[b]+obj[b]))
else:
    print("查無此號碼")