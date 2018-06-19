from flask import Flask
from flask import request,jsonify
import load_data

app=Flask(__name__)

l=load_data.load_file()#获取数据，储存到l中

def find(l,d):
    '从数据集中寻找，返回房间号，找不到则返回-1'
    for i in l:
        if i['id']==d['id'] and i['data']==d['data']:
            return i['num']
    return -1


@app.route('/found',methods=['POST'])
def index():
    print('接收到数据:',request.json)
    rec_l=request.json
    return_list=[int(find(l,i)) for i in rec_l]
    return jsonify(return_list)

app.run()