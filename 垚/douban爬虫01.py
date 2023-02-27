from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import xlwt
import sqlite3



def main():
    baseurl='https://movie.douban.com/top250?start='
    datalist=getData(baseurl)#获取数据
    savepath='.\\豆瓣top250.xls'
    saveData(datalist,savepath)#保存数据
    # askurl('https://movie.douban.com/top250?start=')

#正则表达式
#影片超链接规则
findlink=re.compile(r'<a href="(.*?)">')#.表示一个字符，*表示0个到多个字符，？表示一次或多次,r写在外面确保里面的字符串不会有特殊含义
#找图片
findphoto=re.compile(r'<img alt=.*src="(.*?)"',re.S)#re.S：忽略换行符
#片名
findname=re.compile(r'<span class="title">(.*)</span>')
#评分
findgrade=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findnumber=re.compile(r'<span>(\d*)人评价</span>')#\d表示数字
#介绍
findremark=re.compile(r'<span class="inq">(.*)</span>')
#相关内容
findcontent=re.compile(r'<p class="">(.*?)</p>',re.S)

def getData(baseurl):
    datalist=[]
    for i in range(0,10):
        url=baseurl+str(i*25)
        html=askurl(url)
        soup=BeautifulSoup(html,'html.parser')
        for item in soup.find_all('div',class_="item"):#下划线表示class为属性
            data=[]  #保存电影信息在这里
            item_2=str(item)  #转化为字符串，利用正则表达式筛选
            #link:获取影片超链接
            link=re.findall(findlink,item_2)[0]  #利用findlink方法筛选item_2,findlink在上面定义（全局变量）,找第一个
            data.append(link)
            photo=re.findall(findphoto,item_2)[0]
            data.append(photo)
            name = re.findall(findname, item_2)
            #有中外双语搞两个，没有外语处留空
            if(len(name)==2):
                cnname=name[0]
                data.append(cnname)
                enname=name[1].replace('/','')
                data.append(enname)
            else:
                data.append(name[0])
                data.append('')
            grade=re.findall(findgrade, item_2)[0]
            data.append(grade)
            number=re.findall(findnumber, item_2)[0]
            data.append(number)
            remark=re.findall(findremark, item_2)
            if len(remark)!=0:
                remark=remark[0].replace('。','')#去掉句号
                data.append(remark)
            else:
                data.append('')
            content= re.findall(findcontent, item_2)[0]
            content=re.sub('<br(\s+)?/>(\s+)?','',content)#去掉<br/>
            content=re.sub('/','',content)#替换/
            content = re.sub('\xa0', ' ', content)
            data.append(content.strip())  #去掉前后的空格
            datalist.append(data)
    # print(datalist)
    return datalist


#得到指定一个URL的网页内容
def askurl(url):
    head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43'}
#head伪装
    request=urllib.request.Request(url,headers=head)
    html=''
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode('utf-8')
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,'code'):#e这个对象中是否有code
            print(e.code)
        if hasattr(e,'reason'):

            print(e.reason)
    return html


def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)  # 创建workbook对象,定义压缩效果
    sheet = book.add_sheet('豆瓣电影top250',cell_overwrite_ok=True)  # 创建工作表,数据可覆盖
    col=('电影详情链接','图片链接','片名','外文名','评分','打分人数','评价','概况')
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print('第%d条'%i)
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save(savepath)  # 保存


main()