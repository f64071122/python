#1
side = 10
height = 5
area = side * height/2
print(area)
#2
C = 38
F = C*1.8+32
print(F)
#eval 接受"999+1" = 1000 int
#int 不接受"999+1" 中間有+號
#3
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
#4
sum = 0
for i in range(1,4):
    #score = int(input("分數 = "))
    score = eval(input("分數 = "))
    if i == 3:
        third = score
        print(third)
    sum += score
    print("sum = ", sum)
    
print("ave = ", sum/i)
print("difference = ", third - sum/i)
#5
#num = int(input("可樂數量 = "))
num = eval(input("可樂數量 = "))
for i in range(1,num+1):
    mon = 29*i 
    if i == 2:
        mon *= 0.8
    elif i == 3:
        mon *=0.65
print (mon/i)


