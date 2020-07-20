# and =\= &
#1
x = eval(input("請輸入x值 = "))
if x>=50 and x<=70:
    y=x
    print(y)
else:
    y=100
    print(y)
#2
x = eval(input("請輸入x值 = "))
if x%2 ==0:
    print("x是偶數")
else:
    print("x是奇數")
#3
def cost(x):
    if x>=10:
        return 100 + 50*x
    else:
        return 100 + 40*x
x = eval(input("請輸入貨物重量"))
print(cost(x))
#4 split寫成list
[x, y] = input("請輸入a,b值 = ").split()
x = eval(x)
y = eval(y)
if x != 0 or y != 0:    
    if x%y == 0:
        print("a能被b整除")
    else:
        print("a不能被b整除")
else:
    print("0可以除逆數學是體育老師教的?")
#5
x= eval(input("請輸入a值 = "))
if x >=800:
    print("畢業")
else:
    print("不通過，再一年!!")
#6
[x, y] = input("請輸入溫度和AQI值 = ").split()
x = eval(x)
y = eval(y)
if x >37 or y > 150:
    print("超級熱、超級髒，避免外出")
else:
    print("視情況外出")
