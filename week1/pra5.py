#1 判斷大小
[x,y] = input("請輸入a、b值 = ").split()
x = eval(x)
y = eval(y)
if (x>y):
    print("a>b")
elif (x<y):
    print("a<b")
else:
    print("a=b")
#2 票價
x = eval(input("請輸入身高(公分) = "))
if x<150:
    if x>=120:
        print(100)
    else:
        print("free!")
else:
    print(200)
#3
[x,y,z] = input("請輸入a、b、c值 = ").split()
a = eval(x)
b = eval(y)
c = eval(z)
if a>b and a>c:
    print(100)
elif c>b and c>a:
    print(10)
elif b>a and b>c:
    print(1)
else:
    print(0)
#4 
cost = input("請輸入金錢 = ")
#print(len(cost))
len = len(cost)
cost = eval(cost)
costlist =[]
#if判斷為數，位數補0
if len ==2:
    costlist.append(0)
elif len ==1:
    costlist.append(0)
    costlist.append(0)

for i in range(len-1,-1,-1): 
    #len-1為0的數量ex1234,len=4,0有3個
    
    a = int(cost/(10**i)) #a=商數
    #print("a = ",a)
    costlist.append(a) #list加入商數
    #print("cost = ",cost)
    cost %= (10**i) #餘數 
    #print("i = ",i)
print(costlist[0],"個百元"," ",costlist[1],"個十元","",costlist[2],"個一元")

#5
x = eval(input("請輸入金額 = "))
fif = 0
ten = 0
balance = 100-x
if balance >=50:
    balance -=50
    fif +=1
    ten = int(balance/10)
    balance %=10
    print("找",fif,"個50、", ten,"個10、", balance,"個1")
else:
    ten = int(balance/10)
    balance %=10
    print(fif, ten, balance)
#6
x = eval(input("請輸入空氣品質 = "))
if x>150:
    print("避免外出")
else:
    if x>100:
        print("敏感")
    else:
        if x>50:
            print("普通")
        else:
            print("良好")
#7
[x,y] = input("請輸入身高(公分)、體重(公斤) = ").split()
x = eval(x)
y = eval(y)
if x>=150 and x<=190:
    if y>=50 and y<=90:
        print("簽下去")
else:
    print("好爽喔")
#8
#8
x = eval(input("請輸入西元 = "))
if x%4 !=0:
    print("平年")
else:
    if x% 100 == 0 and x%400 !=0:
        print("平年")
    else:
        print("閏年")    




    



