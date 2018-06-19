import re
#读取文件,储存到l中：
def load_file():
    re_extract=re.compile(r'^([a-zA-Z0-9\:]+)[\s]+(\d+)[\s]+(\d+)$')
    l=[]
    with open('./data.txt') as f:
        for i in f.readlines():
                i=i.replace('\n','')
                i=i.replace('\t','')
                m=re_extract.match(i)
                if m:
                    g=m.groups()
                    d=dict(id=g[0],data=g[1],num=g[2])
                    l.append(d)
    return l