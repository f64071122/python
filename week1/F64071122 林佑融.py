#已知1920/1/1 星期四
#已知1920/3/1 星期一
#1970 平年  1972潤 1976潤
#傳入 閏年 平年 1/1~3/1 差60天，閏年;差59天，平年
# 0 1 2 3 4 5 6 代表 星期日~星期六
# 30%7 = 2, 31%7 = 3, 28%7 = 0
# 1/1是星期一(1)，一月有31天，31%7 = 3, 2/1就是1+3=4 也就是星期四
# 二月有28天 3/1就是4+ 28%4 = 4星期四
# 二月有29天 3/1就是4+ 29%4 = 5星期五  
# 365%7是1 366%7是2
#思考順序
#1. 先印出 1920/1 的月曆 不用for迴圈直接print
#2. 印出1920的年曆 需要1層for迴圈跑月份
#   (月份的天數)%7 累加 後再%7判斷每月第一天是[0,1,2,3,4,5,6]星期幾
#3. 年份閒接，也就是12月和隔年1月要怎麼接 (12->0)
def leap_year (year): #回傳true代表潤年 false 代表平年
    if year %4 !=0:
        return False
    else:
        if year %100 == 0 and year %400 !=0:
            return False
        else:
            return True
def get_day_of_month (year, month):
    thirty1 = [0,1,3,5,7,8,10,12] # "0" 等一下就知道
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
#     4-> 7-> 8-> 11-> 13-> 16-> 18-> 21-> 24-> 26-> 29-> 31->34 (1921/1/1)
#星期 4-> 日-> 1-> 4 -> 6 -> 2 -> 4 -> 日-> 3 -> 5 -> 1 -> 3 ->6
#閏年 +30,平年+29
def get_start_date(year, month):
    num = 4
    for i in range(1920, year):
        if leap_year(i) ==False:
            num += 29 #365%7 = 39%7 = 1
        else:
            num += 30 #366%7 = 30%7 = 2
    for i in range(1, month):
        day = get_day_of_month (year, i)
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
print("輸入1進入年曆模式")
print("輸入2進入月曆模式")
print("輸入3進入日曆模式")
mode = eval(input())
while mode not in [1,2,3]:
    mode = eval(input())
if mode ==1:
    year = input("請輸入年份: ")
    year = eval(year)
    
    for i in range(1,13):
        print('\t','\t','\t',i,"月")
        print('') 
        day = get_day_of_month (year, i)  #得到該月的天數
        weekday = get_start_date(year, i) #得到每月1號星期幾
        for j in range(0,7):  
            week = ["日","一","二","三","四","五","六"]
            print(week[j],end = '\t')
        print('')
        for i in range(weekday%7): #0就不用印空格
            print('',end = '\t')
        for i in range(weekday%7,day + weekday%7): #印天數
            if i%7 == 6:
                print(i-(weekday-1)) #1號 = (i = 4)4-(4-1),#2號 = (i = 5)5-(4-1)
            else: #印到星期六要換行
                print(i-(weekday-1), end = "\t")
        print('\n')
elif mode ==2:
    year = input("請輸入年份: ")
    year = eval(year)
    month = input("請輸入月份: ") 
    month = eval(month)    
    for i in range(7):  
        week = ["日","一","二","三","四","五","六"]
        print(week[i],end = '\t')
    print('')
    day = get_day_of_month (year, month)  #得到該月的天數
    weekday = get_start_date(year, month) #得到每月1號星期幾
    for i in range(weekday%7): #0就不用印空格
        print('',end = '\t')
    for i in range(weekday%7,day + weekday%7): #印天數
        if i%7 == 6:
            print(i-(weekday-1)) #1號 = (i = 4)4-(4-1),#2號 = (i = 5)5-(4-1)
        else: #印到星期六要換行
            print(i-(weekday-1), end = "\t") 
else:
    year = input("請輸入年份: ")
    year = eval(year)
    month = input("請輸入月份: ") 
    month = eval(month)
    date = input("請輸入日期: ") 
    date = eval(date)
    first = get_start_date(year, month) #得到該月第一天的星期
    for i in range(1,date):
        first +=1
    week = [0,1,2,3,4,5,6]
    if first%7 == 0:
        print(year, "年" ,month, "月" ,date ,"日" ,"星期日")
    if first%7 == 1:
        print(year, "年" ,month, "月" ,date ,"日" ,"星期一")
    if first%7 == 2:
        print(year, "年" ,month, "月" ,date ,"日" ,"星期二")
    if first%7 == 3:
        print(year, "年" ,month, "月" ,date ,"日" ,"星期三")
    if first%7 == 4:
        print(year, "年" ,month, "月" ,date ,"日" ,"星期四")
    if first%7 == 5:
        print(year, "年" ,month, "月" ,date ,"日" ,"星期五")
    if first%7 == 6:    
        print(year, "年" ,month, "月" ,date ,"日" ,"星期六")
        