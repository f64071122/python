#8

inp =[1,1]
fir = 1
sec = 1
third = 2*fir + sec + 1
x = eval(input())
for i in range(1, x-1):
    if i%3 ==2:
        fir = 2*sec + third + 1
        inp.append(fir)
        
    elif i%3 ==0:
        sec = 2*third + fir + 1
        inp.append(sec)
        
    else:
        third = 2*fir + sec + 1
        inp.append(third)
for i in range(len(inp)):        
    print(inp[i],sep = ' ',end = ' ')