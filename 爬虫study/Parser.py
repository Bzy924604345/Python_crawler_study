from bs4 import BeautifulSoup

#根据网页字符串创建BeautifulSoup对象
soup = BeautifulSoup(
    html_doc, #HTML文档字符串
    'html.parser', #HTML解析器
    from_encoding = 'htf-8' #HTML文档的编码
    )