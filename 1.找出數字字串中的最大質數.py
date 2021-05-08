a=input("請輸入正整數:")
list1=[]
list2=[]
j=0
for i in range(0,len(a)):
    for j in range(0,len(a)+1):
        if a[i:j]!="":
            list1.append(int(a[i:j]))

for i in list1:
    s=0
    for j in range(1,i+1):  
        if i%j==0:
            s+=1
    if s==2:
        list2.append(j) 

if list2==[]:
    print("No prime found")
else:
    print("子字串中最大的質數為:"+str(max(list2)))


