#测试用的脚本，主要用到了requests模块
import requests
import json

# 测试用的list
# 前两个是有效的，最后一个是无效的
l=[{'id':'38:91:d5:9f:82:90','data':'96'},
   {'id':'38:91:d5:9f:82:90','data':'99'},
   {'id':'38:91:d5:9f:82:90','data':'30'}]

# 路径
# 注意不是根路径'/',需要假设参数'found'
url='http://127.0.0.1:5000/found'

#发起请求
r=requests.post(url,json=l)

#获取返回的数据，原格式是字节流，需要通过编码，json数据转list作格式转换
recv_list=json.loads(r.content.decode())
print(recv_list)