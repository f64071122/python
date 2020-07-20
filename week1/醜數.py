#質因數只有 2 3 5
def ugly(x):
    if x%2 ==0 and x%3 ==0 and x%5 ==0 or x ==1:
        return True
    else:
        return False
x =eval(input())
if ugly(x) == True:
    print("true")
else:
    print("false")