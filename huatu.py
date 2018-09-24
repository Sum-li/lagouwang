import pandas as pd
from pyecharts import Bar
from pyecharts import Page
from pyecharts import Pie
df = pd.read_csv('/home/lsgo28/PycharmProjects/demo/爬取拉勾网.csv')
df_duplicates=df.drop_duplicates(subset='positionId',keep='first')

def cut_word(word,method):
    position=word.find('-')
    length=len(word)
    if position !=-1:
        bottomsalary=word[:position-1]
        topsalary=word[position+1:length-1]
    else:
        bottomsalary=word[:word.upper().find('K')]
        topsalary=bottomsalary
    if method=="bottom":
        return bottomsalary
    else:
        return topsalary
df_duplicates['topsalary']=df_duplicates.salary.apply(cut_word, method="top")
df_duplicates['bottomsalary']=df_duplicates.salary.apply(cut_word, method="bottom")
df_duplicates.bottomsalary.astype('int')
df_duplicates.topsalary.astype('int')
df_duplicates["avgsalary"]=df_duplicates.apply(lambda x:(int(x.bottomsalary)+int(x.topsalary))/2,axis=1)
city_list = df_duplicates["city"].drop_duplicates(keep='first')
money = []
money1 = []
number = []
number1 = []
k = 0
l = 0
m = 0
n = 0
for city in city_list:
    for city_,money_ in zip(df_duplicates["city"],df_duplicates["avgsalary"]):
        if city_==city:
            k +=money_
            l += 1
    number.append(l)
    money.append(k/l)
workyears_list = ['应届毕业生','1年以下','1-3年','3-5年','5-10年','10年以上','不限']
for workyears in workyears_list:
    for workyears_,money_ in zip(df_duplicates["workYear"],df_duplicates["avgsalary"]):
        if workyears_==workyears:
            m += money_
            n += 1
    number1.append(n)
    money1.append(m/n)
pie = Pie("职位数量饼图")
bar = Bar("各大城市职业的平均月薪（K）")
bar1 = Bar("各大城市职位数")
bar2 = Bar("各类工作经验平均月薪（K）")
pie.add("",workyears_list,number1,is_stack=True)
bar.add("月薪",city_list,money,is_stack=True)
bar1.add("公司",city_list,number,is_stack=True)
bar2.add("经验",workyears_list,number1,is_stack=True)
page = Page()
page.add(bar)
page.add(bar1)
page.add(bar2)
page.add(pie)
page.render("图文.html")
