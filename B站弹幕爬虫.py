import requests
import re
import time
import random
import datetime
import pandas as pd
import google.protobuf.text_format as text_format
import bili_pb2

def get_response(html_url):
    headers = {
    'cookie': "buvid3=E2297D38-EBB1-4054-5408-A597A75AAA6391211infoc; i-wanna-go-back=-1; _uuid=C226BAFE-828D-E32A-EC45-102D969959FF891548infoc; buvid4=2A1DC894-F5C2-7604-FFF8-A38652139A1D92224-022030322-EddwJ8pQYxZfVUc0q8CgIQ==; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; LIVE_BUVID=AUTO4316469900152808; nostalgia_conf=-1; blackside_state=0; hit-dyn-v2=1; b_nut=100; rpdid=|()kYmYlk|m0J'uYY)~)|uR); DedeUserID=499599126; DedeUserID__ckMd5=11e5b3b511a997df; b_ut=5; hit-new-style-dyn=0; CURRENT_QUALITY=112; CURRENT_FNVAL=4048; header_theme_version=CLOSE; fingerprint=2cca9590be56eed89c2a4cef540298a9; buvid_fp=2cca9590be56eed89c2a4cef540298a9; home_feed_column=5; go_old_video=1; PVID=1; b_lsid=4B31A910D_18691599091; SESSDATA=783977da,1693027814,77983*21; bili_jct=5d13dffe24bac58a28486af947ec1f38; sid=7v7q6hri; bp_video_offset_499599126=767233261240844300; innersign=1",
    'origin': 'https://www.bilibili.com',
    'referer': 'https://www.bilibili.com/video/BV16X4y1g7wT/?vd_source=9e6bf8efb01375dfceed4bc67b8fe4d2',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
    }
    # headers_list = [
    # {
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56'
    # }, 
    # # {
    # #     'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
    # # }
    # ]
    # headers = random.choice(headers_list)

    try:
        response = requests.get(html_url, headers=headers)
        response.encoding = 'utf-8'  # 超时设置为10秒
    except:
        for i in range(4):  # 循环去请求网站
            response = requests.get(html_url, headers=headers, timeout=20)
            if response.status_code == 200:
                break
    return response

def get_date(html_url):
    response = get_response(html_url)
    json_data = response.json()
    date = json_data['data']
    print(date)
    return date

def save(content):
    for i in content:
        with open('B站弹幕.txt', mode='w', encoding='utf-8') as f:
            f.write(i)
            f.write('\n')
            print(i)


def main(date_url):
    #date = get_date(date_url)
    #for date in date:
        #time.sleep(10)
    #时间列表
    start = datetime.datetime.strptime("2023-02-01", "%Y-%m-%d")
    end = datetime.datetime.strptime("2023-02-01", "%Y-%m-%d")
    date_generated = pd.date_range(start, end)
    data_list = []
    date_list = date_generated.strftime("%Y-%m-%d")
    for date in date_list:
        url = ('https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=323723441&date=%s'%(date))
        html_data = get_response(url).text
        # print(html_data)
        # result = re.findall("[\u2E80-\u2FDF\u3040-\u318F\u31A0-\u31BF\u31F0-\u31FF\u3400-\u4DB5\u4E00-\u9FFF\uA960-\uA97F\uAC00-\uD7FF]+ ", html_data)
        # print(result)
        # save(html_data)
    # with open('B站弹幕.txt', mode='a', encoding='utf-8') as f:
    #     f.write(result)
        my_seg = bili_pb2.DmSegMobileReply()
        my_seg.ParseFromString(html_data)
        # for j in my_seg.elems:
        #     parse_data = text_format.MessageToString(j, as_utf8=True)

        print(text_format.MessageToString(my_seg.elems[0],as_utf8=True))


if __name__ == '__main__':
    date_url = 'https://api.bilibili.com/x/v2/dm/history/index?month=2023-02&type=1&oid=323723441'
    main(date_url)