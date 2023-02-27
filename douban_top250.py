from 爬虫study import url_manager
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pprint

def download_all_htmls():
    #构建分页数字列表
    page_indexs = range(0,250,25)
    htmls = []
    for index in page_indexs:
        new_url = f"https://movie.douban.com/top250?start={index}&filter="
        print(new_url)
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56'}
        r = requests.get(url = new_url, headers= headers)
        if r.status_code != 200:
            raise Exception("status_error",r.status_code)
        htmls.append(r.text)
        print(len(htmls))
    return htmls

def parser_single_html(html):
    """
        解析单个HTML,得到数据
        @return list({"link","title",[label]})
    """
    soup = BeautifulSoup(html,"html.parser")
    article_items = (soup.find("div",class_ = "article")
                     .find("ol",class_ = "grid_view")
                     .find_all("div",calss_ = "item"))
    data = []
    for article_item in article_items:
        rank = article_item.find("div",class_ = "pic").find("em").get_text()
        print(rank)
        img = article_item.find("img").get('src')

        info = article_item.find("div",class_ = "info")
        title = info.find("div",class_ = "hd").find("span",class_ ="title").get_text()
        stars = (info.find("div",class_ = "bd")
                       .find("p",class_ = "star")
                       .find_all("span"))
        rating_star = stars[0]["class"][0]
        rating_num = stars[1].get_text()
        commments_num = stars[3].get_text()

        data.append(rank)
        # append({
        #     "rank":rank,
        #      "titel":title,
        #      "image":img,
        #      "rating_star": rating_star.replace("rating","").replace("-t",""),
        #      "rating_num": rating_num,
        #      "commments_num": commments_num.replace("评价人数","")})
    print(len(data))
    return data

    
if __name__ == '__main__':
    htmls = download_all_htmls()

    datas = []
    for html in htmls:
        parser_single_html(html)

        datas.append(parser_single_html(html))
    df = pd.DataFrame(datas)
    df.to_excel("豆瓣电影TOP205.xlsx")
    

        
    
    
