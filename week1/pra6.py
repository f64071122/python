#1-1
sum = 0
for i in range(2,32,2):
    sum +=i
print(sum)
#1-2
sum = 1
for i in range(3,27,6):
    sum *=i
print(sum)
#1-3
sum = 0
for i in range(3,13,2):
    sum += 1/i
print(sum)
#1-4
sum = 0
for i in range(1,16,3):
    sum += (i*(i+4))
print(sum)
#1-5 有點男
sum = 0
deg = 0
num = -1
for i in range(-1,-13,-3):
    num+=2
    for j in range(-1,num,2):
        deg = num
    sum += i**num
print(sum)
#利用等差數列公式
sum = 0
for i in range(4):
    #a1+(n-1)d
    sum += (-10+i*3)**(7-i*2)
print(sum)
#2
weight = 0
for i in range(1,11):
    weight = 40+i*1.3
print(weight)
#3
sum =0
for i in range(3,100,3):
    sum+=i
print(sum)
#4
sum = 0
for i in range(21,51,2):
    print(i)
    sum +=i
print(sum)
sum = 0
for i in range(1,100,2):
    if i>20 and i<51:
        print(i)
        sum +=i
print(sum)
