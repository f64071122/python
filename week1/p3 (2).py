n = eval(input())
nums = n
numx = 1
for i in range(n): #幾層
    for j in range(nums-1,0,-1):
        print(" ", end = '')#一層的空格
    nums -=1
    for j in range(0,numx):   #一層的x
        if j == numx-1:
            print("X")
        else:
            print("X", end = '')
    numx +=1
    