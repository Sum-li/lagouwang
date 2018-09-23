import json
import requests



header = {"Cookie":"JSESSIONID=ABAAABAAAGFABEFB093DFBA72E00093316821E95E4971CF; user_trace_token=20180921154401-430b2b64-ca4b-411e-be98-f86172880bd3; _ga=GA1.2.231300040.1537515842; LGSID=20180921154401-1b73362c-bd72-11e8-a516-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E4%25BA%2592%25E8%2581%2594%25E7%25BD%2591%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE%3Fpx%3Ddefault%26city%3D%25E4%25B8%258A%25E6%25B5%25B7; LGUID=20180921154401-1b73384e-bd72-11e8-a516-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1537515842; _gid=GA1.2.1479618188.1537515843; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1537515859; LGRID=20180921154418-259c60d0-bd72-11e8-bb56-5254005c3644; SEARCH_ID=801b32db85184bc0910c10a3da7a18ad",
          "Host":"www.lagou.com",
          'Origin': 'https://www.lagou.com',
          'Referer':'https://www.lagou.com/jobs/list_%E4%BA%92%E8%81%94%E7%BD%91%E5%A4%A7%E6%95%B0%E6%8D%AE?px=default&city=%E4%B8%8A%E6%B5%B7',
          'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
Data = {'first':'true','kd':'互联网大数据','pn':'1'}
def start_requests(myurl):
   r1 = requests.post(myurl,data=Data,headers=header,verify=False)
   r_text = r1.text
   content = json.loads(r_text)
   pagesize = content.get('content').get('pageSize')
   return pagesize

def get_result(pagesize):
    for page in range(1,pagesize+1):
        content_next = json.loads(requests.post(myurl +str(page),data=Data,headers=header,verify=False).text)
        company_info = content_next.get('content').get('positionResult').get('result')
        if company_info:
            for p in company_info:
                line =  str(p['city']).replace(',',';') + ',' + str(p['companyFullName']).replace(',',';')  + ',' + str(p['companyId']).replace(',',';')  + ',' + \
                       str(p['companyLabelList']).replace(',',';') + ',' + str(p['companyShortName']).replace(',',';')  + ',' + str(p['companySize']).replace(',',';')  + ',' + \
                       str(p['businessZones']).replace(',',';') + ',' + str(p['firstType']).replace(',',';')  + ',' + str(
                    p['secondType']).replace(',',';')  + ',' + \
                       str(p['education']).replace(',',';')  + ',' + str(p['industryField']).replace(',',';') +',' + \
                       str(p['positionId']).replace(',',';')+',' + str(p['positionAdvantage']).replace(',',';') +',' + str(p['positionName']).replace(',',';') +',' + \
                       str(p['positionLables']).replace(',',';') +',' + str(p['salary']).replace(',',';') +',' + str(p['workYear']).replace(',',';') + '\n'
                file.write(line)

if __name__=='__main__':
    title = 'city,companyFullName,companyId,companyLabelList,companyShortName,companySize,businessZones,firstType,secondType,education,industryField,positionId,positionAdvantage,positionName,positionLables,salary,workYear\n'
    file = open('%s.txt' % '爬取拉勾网', 'a')
    file.write(title)
    cityList = ['北京', '上海','深圳','广州','杭州','成都','南京','武汉','西安','厦门','长沙','苏州','天津','郑州']
    for city in cityList:
        print('爬取%s'%city)
        myurl ='https://www.lagou.com/jobs/positionAjax.json?px=default&city={}&needAddtionalResult=false&pn=1'.format(city)
        pagesize = start_requests(myurl)
       # print(pagesize)
        get_result(pagesize)
    file.close()

