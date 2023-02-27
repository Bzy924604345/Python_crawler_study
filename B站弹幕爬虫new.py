import requests
from bs4 import BeautifulSoup
import re

#发送请求
url = 'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=323723441&date=2023-02-19'
headers = {
    'cookie': "buvid3=E2297D38-EBB1-4054-5408-A597A75AAA6391211infoc; i-wanna-go-back=-1; _uuid=C226BAFE-828D-E32A-EC45-102D969959FF891548infoc; buvid4=2A1DC894-F5C2-7604-FFF8-A38652139A1D92224-022030322-EddwJ8pQYxZfVUc0q8CgIQ==; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; LIVE_BUVID=AUTO4316469900152808; nostalgia_conf=-1; blackside_state=0; hit-dyn-v2=1; b_nut=100; rpdid=|()kYmYlk|m0J'uYY)~)|uR); DedeUserID=499599126; DedeUserID__ckMd5=11e5b3b511a997df; b_ut=5; hit-new-style-dyn=0; CURRENT_QUALITY=112; fingerprint=4df660e54da28afd3130ed53ae0bd2aa; buvid_fp=4df660e54da28afd3130ed53ae0bd2aa; CURRENT_FNVAL=4048; header_theme_version=CLOSE; SESSDATA=944223e2,1692937639,eccb9*21; bili_jct=2ac3b588387238da391ac8abb4d1d155; sid=8hbq44lr; home_feed_column=5; bsource=search_baidu; b_lsid=724B2AB4_1868D84B7F1; CURRENT_PID=e058fbf0-b5cb-11ed-9c21-2be8a037bd85; bp_video_offset_499599126=766974382116438000; innersign=1; PVID=5",
    'origin': 'https://www.bilibili.com',
    'referer': 'https://www.bilibili.com/video/BV16X4y1g7wT/?vd_source=9e6bf8efb01375dfceed4bc67b8fe4d2',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56',
}
try:
        response = requests.get(url, headers=headers, timeout=10)  # 超时设置为10秒
except:
    for i in range(4):  # 循环去请求网站
        response = requests.get(url, headers=headers, timeout=20)
        if response.status_code == 200:
            break

response.encoding = 'utf-8'
# data_list = response.text
#解析数据
data_list = re.findall('<d p=".*?>(.*?)</d>',response.text)
for data in data_list:
    with open('dm.txt',mode='a',encoding='utf-8') as f:
        f.write(data)
        f.write('\n')
    
