def leap_year (year): #回傳true代表潤年 false 代表平年
    if year %4 !=0:
        return False
    else:
        if year %100 == 0 and year %400 !=0:
            return False
        else:
            return True
def get_day_of_month (year, month):
    thirty1 = [1,3,5,7,8,10,12]
    thirty = [4,6,9,11]
    if month in thirty1: 
        return 31
    elif month in thirty:
        return 30
    else: #2月
        if leap_year(year) == False:
            return 28            
        else:
            return 29
# 4-> 7-> 8-> 11-> 13-> 16-> 18-> 21-> 24-> 26-> 29-> 31->34 (1921/1/1)
#星期 4-> 日-> 1-> 4-> 6-> 2-> 4-> 日-> 3-> 5-> 1-> 3
def get_start_date(year, month):
    num = 4
    for i in range(1,month): #1/1不會執行
        day = get_day_of_month (year, i) #得到前一月的天數ex 2/1要得到1月的天數(31天)
        num += day%7
    if num%7 == 0:
        return 0
    if num%7 == 1:
        return 1
    if num%7 == 2:
        return 2
    if num%7 == 3:
        return 3
    if num%7 == 4:
        return 4
    if num%7 == 5:
        return 5
    if num%7 == 6:    
        return 6                                  
#week = [0,1,2,3,4,5,6]
year = eval(input())
month = eval(input())      
for i in range(7):  
    week = ["日","一","二","三","四","五","六"]
    print(week[i],end = '\t')
print('')
day = get_day_of_month (year, month)  #得到該月的天數
weekday = get_start_date(year, month) #得到每月1號星期幾
#印前面的空格
for i in range(weekday%7): #0就不用印空格
    print('',end = '\t')
for i in range(weekday%7,day + weekday%7): #印天數
    if i%7 == 6:
        print(i-(weekday-1)) #1號 = (i = 4)4-(4-1),#2號 = (i = 5)5-(4-1)
    else: #星期六要換行
        print(i-(weekday-1), end = "\t") 
# 1920每一個月份都OK
# 上面的def get_start_date num = 4代表已經知道1/1是禮拜4
#現在是年份也不知道 所以num隨著年份改變
