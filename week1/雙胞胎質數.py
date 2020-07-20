x,y = [int(x) for x in input().split(",")]
pr = []
for i in range(x,y+1):#被除數2~n
    num =0
    for j in range(2,int(i**0.5)+1): #除數 2~根號n
        if i%j ==0:
            num +=1
    if num ==0:
        pr.append(i)
for i in range(1,len(pr)):
    if pr[i] == pr[i-1] +2:
        print("(",pr[i-1],",",pr[i],")",sep = '')

