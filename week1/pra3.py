#1
side = eval(input("邊長 = "))
hei = eval(input("高 = "))
area = side * hei/2
print(area)
#2
C = eval(input("攝氏溫度 = "))
F = C*1.8+32
print("華氏溫度 = ",F,"F")
#eval 接受"999+1" = 1000 int
#int 不接受"999+1" 中間有+號
#3
F = eval(input("華氏溫度 = "))
C = (F-32)*5/9
print("攝氏溫度 = ",C,"C")
#4
hei = eval(input("身高(公分) = ")) #公分
wei = eval(input("體高(公斤) = ")) #公斤
BMI = wei/(hei*0.01)/(hei*0.01)
print(BMI)
#5
def X(a,b):
    return  (a+b*b)/(a-3*b)/(2*a+b)
def Y(a,b):
    return  (a*a*a+b*b)/3/b/(a-5*b)
x = eval(input("請輸入a = "))
y = eval(input("請輸入b = "))
print("X = ", X(x,y),"Y = ", Y(x,y))
#6
sum = 0
for i in range(1,6):
    #score = int(input("分數 = "))
    score = eval(input("分數 = "))
    print(type(score)) #沒有int是str
    sum += score
    #avg = int(score)/i

print("sum = ", sum)
#print("ave = ", avg)
print("ave = ", sum/i)
#7
sum = 0
for i in range(1,4):
    #score = int(input("分數 = "))
    score = eval(input("分數 = "))
    if i == 1:
        first = score
        print(first)
    sum += score
    print("sum = ", sum)
    
print("ave = ", sum/i)
print("difference = ", first - sum/i)
#8
num = eval(input("油箱容量 = "))
print("95要 = ", 21.6*num)
print("98要 = ", 23.4*num)


