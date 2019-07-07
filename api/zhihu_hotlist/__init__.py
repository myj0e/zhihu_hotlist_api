import requests
import os
import sys
import json
import brotli


sys.path.append(os.path.dirname(__file__))

import config
from data_structure import entry

url=config.PROTOCOL+'://'+config.URL+config.PATH
headers=config.HEADERS
payload=config.PAYLOAD

def get_list()->dict:
    r=requests.get(url,params=payload,headers=headers)
    if r.status_code!=200:
        print('Request Error: {code}'.format(code=r.status_code))
        exit(-1)
    response=brotli.decompress(r.content).decode()
    r=json.loads(response)
    return r['data']


def hotlist():
    r=get_list()
    ret=[]
    try:
        for i in r:
            x=entry()
            x.heat=i['detail_text']
            x.title=i['target']['title']
            x.url=i['target']['url']
            x.describe=i['target']['excerpt']
            x.cover==i['children'][0]['thumbnail']
            x.comment_count=int(i['target']['comment_count'])
            x.follower_count=int(i['target']['follower_count'])
            ret.append(x)
    except KeyError:
        print('api_KeyError')
        ret=[]
    return ret


if __name__=='__main__':
    r=hotlist()
    for i in r:
        print(f"{i.title} {i.follower_count}")
