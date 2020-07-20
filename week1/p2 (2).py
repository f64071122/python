[n, k] = [int(x) for x in input().split()]
num = 0
dep = 10
while n>dep:
    dep +=k
    num +=1
print(num)
