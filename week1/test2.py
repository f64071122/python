for i in range(7):
    week = ["日","一","二","三","四","五","六"]
    print(week[i],end = '\t')
print('')
print('\t','\t','\t','\t',end = '')
#week = [0,1,2,3,4,5,6]
#已知1920/1/1 星期四->4
#先印出 1920/1 月曆
for i in range(4,35):   
    if i%7 == 6:
        print(i-3)
    else:
        print(i-3, end = "\t")
#已知1920/1/1是星期四->4，前面應該有4個大空格(Tab)
for i in range(7):
    week = ["日","一","二","三","四","五","六"]
    print(week[i],end = '\t')
print('')
for i in range(4): #4是已知
    print('',end = '\t')
for i in range(4,35):  #4是已知
    
    if i%7 == 6:
        print(i-3)
    else:
        print(i-3, end = "\t")
#剛剛是已經知道1920/1/1是星期四->4
#判斷1920每個月的第一天是0.1.2.3.4.5.6哪一個
#也就是原本已知的4變成未知
# 1/1是星期四(4)，一月有31天，31%7 = 3, 2/1就是4+3=7, 7%7 = 0也就是星期日
# 二月有28天 3/1就是0+ 28%4 = 0星期日 (平年)
# 二月有29天 3/1就是4+ 29%4 = 5星期一 (閏年)
# 三月是31天 4/1就是5+ 31%7 = 9, 9%7 = 2星期二
# 4-> 7-> 8-> 11-> 13-> 16-> 18-> 21-> 24-> 26-> 29-> 31->34 (1971/1/1)
#星期 4-> 日-> 1-> 4-> 6-> 2-> 4-> 日-> 3-> 5-> 1-> 3

