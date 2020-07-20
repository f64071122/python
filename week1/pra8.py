#1 用dic建立多個list
obj = {}
for i in range(3):
    [x, y, z] = [int(x) for x in input("請輸入國、英、數: ").split()]
    obj[i] = [x, y, z]
    #obj['student' + str(i)] = eval(input())
over = 0
for i in range(len(obj)):
    score = obj[i]
    print(score)
    above90 = 0
    for item in score:
        if item >=90:
            above90 +=190
    if above90 ==3:
        over +=1
print(over)
#1-b
max = obj[0][0]
for i in range(1,len(obj)):
    if obj[i][0]> max:
        max = obj[i][0]
print(max)
#1-c
min = obj[0][2]
for i in range(1,len(obj)):
    if obj[i][2]< min:
        min = obj[i][2]
print(min)
#1-d
down60 = 0
for i in range(len(obj)):
    if obj[i][1]<60:
        down60 +=1
print(down60)
#1-e
sumc = 0
summ = 0
for i in range(len(obj)):
    sumc += obj[i][0]
    summ += obj[i][2]
print(sumc/(i+1))
print(summ/(i+1))    
#2-a
sum = 0
for i in range(0,7):
    sum += (4+3*i)
print(sum)
#2-b
sum = 0
for i in range(0,5):
    sum += (1+i*2)*(4+i*2)
print(sum)
#2-c
sum = 0
for i in range(0,4):
    sum += ((-10+i*2))**((7-i*2))
print(sum)
#2-d
sum = 0
for i in range(0,4):
    sum += (1+i*2)*(3+i*2)*(7+i*2)
print(sum)
#2-e
sum = 0
for i in range(0,4):
    sum += (1+i*2)/(3+i*4)
print(sum)
#2-f
d = 3
sum = 3
for i in range(3):
    d += (5+i*2)
    sum *=
    sum +=d

print(sum)


    
