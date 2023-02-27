url = "https://csdnnews.blog.csdn.net/article/details/129173530?spm=1000.2115.3001.5927"

import requests
rq = requests.get(url)
if rq.status_code != 200:
    raise Exception()

html_doc = rq.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,"html.parser")

div_nodes = soup.find_all("div",id = "js_content")

for div_node in div_nodes:
    link = div_node.find("p",style = "text-align:center;")
    print(link.name,link["style"])
