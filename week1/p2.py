#8
x = eval(input())
y = eval(input()) 
upsum=1 #(n!)
downsum1 = 1 #(k!)
downsum2 = 1 #(n-k)!
for i in range(1, x+1):
    upsum *=i
for i in range(1, y+1):
    downsum1 *=i    
for i in range(1, x-y+1):
    downsum2 *=i
print(upsum/downsum1/downsum2)