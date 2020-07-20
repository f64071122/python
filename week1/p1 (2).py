x = eval(input())
A = []
a = 0
for i in range(1,x+1):
    a +=i
    A.append(a)
sum = 0
for i in range(len(A)):
    sum += A[i]
print(sum)