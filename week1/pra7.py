#1
inp = []
for i in range(10):
    x = eval(input())
    inp.append(x)
print("最大值 = ",max(inp))
print("最小值 = ",min(inp))
print("不及格個數 = ",sum(1 for item in inp if item <(60))) 
#2
inp = []
for i in range(10):
    x = eval(input())
    inp.append(x)

print("最大值 = ",max(inp))
print("最小值 = ",min(inp))
print("<0個數 = ",sum(1 for item in inp if item <0))
print(">10個數 = ",sum(1 for item in inp if item >10))
#3
inp = []
for i in range(5):
    x = eval(input())
    inp.append(x)
print(">=1,<30個數 = ",sum(1 for item in inp if item >=1 and item <30))
print(">=10,<60個數 = ",sum(1 for item in inp if item >=10 and item <60))
#4
inp = []
for i in range(7):
    x = eval(input("請輸入AQI = "))
    inp.append(x)
print("空氣良好天數 = ",sum(1 for item in inp if item <50))
print("空氣普通天數 = ",sum(1 for item in inp if item >=50 and item <100))
print("敏感族不適合天數 = ",sum(1 for item in inp if item >=100 and item <150))
print("敏感族不適合天數 = ",sum(1 for item in inp if item >=150))
#5
inp = []
avg = 0
num = eval(input("請輸入報考多益人數 = "))
for i in range(num):
    x = eval(input("請輸入成績 = "))
    inp.append(x)
    avg += x
print("最大值 = ",max(inp))
print("900分人數 = ", sum(1 for item in inp if item>=900))
print("600~700分數 = ",sum(1 for item in inp if item>=600 and item<=700))
print("平均 = ", avg/(i+1)) #從0開始i到num就停了，所以i = num-1要再加1個
#6
x = eval(input("請輸入電費(度) = "))
cost = 0
if x> 100:
    if x>300:
        cost = 100*2.2+200*3.3+(x-300)*4.4
        print(cost)
    else:
        cost = 100*2.2+(x-100)*3.3
        print(cost)
else:
    cost = x*2.2
    print(cost)
#7
x = eval(input("請輸入數字 = "))
j = 1
for i in range(1,x+1):
    j *= i
print(x,"! = ",j)
#8 費氏數列
inp =[0,1]
fir = 0
sec = 1
third = fir + sec
x = eval(input("請輸入>2的整數 = "))
for i in range(1, x-1):
    if i%3 ==2:
        fir = sec + third
        inp.append(fir)
        print(fir)
    elif i%3 ==0:
        sec = third + fir
        inp.append(sec)
        print(sec)
    else:
        third = fir + sec
        inp.append(third)
        print(third)
print(inp)
    


