import re
import google.protobuf 
import bili_pb2
import requests
import google.protobuf.text_format as text_format
import bili_pb2 as Danmaku

url = ('https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=323723441&date=2023-02-01')
# url = 'http://api.bilibili.com/x/v2/dm/web/seg.so'
params = {
    'type':1,         #弹幕类型
    'oid':323723441,    #cid
    #'pid':810872,     #avid
    'segment_index':1 #弹幕分段
}
resp = requests.get(url,params)
data = resp.content

danmaku_seg = Danmaku.DmSegMobileReply()
danmaku_seg.ParseFromString(data)

print(text_format.MessageToString(danmaku_seg.elems[0],as_utf8=True))




# filename = 'seg.txt'
# file = open(filename, mode='rt', newline='', encoding='utf-8', errors='ignore') # 打开文件进行读取
# text = file.read()


 
# file.close()



# lines = file.readlines() # 读取文件的内容 
# for line in lines:
#     num = re.findall("[a-zA-Z0-9]+",line)
#     #content = re.findall("[\u4e00-\u9fa5\u3002|\uff1f|\uff01|\uff0c|\u3001|\uff1b|\uff1a|\u201c|\u201d|\u2018|\u2019|\uff08|\uff09|\u300a|\u300b|\u3010|\u3011|\u007e]+",line)
#     content = re.findall("(?<=:).*?(?=@)",line)
#     if len(content) == 0:
#         continue
#     content[0] = content[0][1:]
#     print(num,content)
# file.close() # 关闭文件

# with open('乱码.txt', mode='w', encoding='gbk') as f:
#      f.write(result)
