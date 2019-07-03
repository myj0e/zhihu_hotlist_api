
#协议头
PROTOCOL='http'

#接口url
URL='api.zhihu.com' #勿带http://或https://一类协议头

#请求路径
PATH='/topstory/hot-lists/total'

#请求参数
PAYLOAD={
    'limits':10,
    'reverse_order':0
}
#请求头
HEADERS={
    'Host': f'{URL}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip,deflate,br',
    'DNT': '1',
    'Cache-Control' : 'no-cache',
    'Pragma': 'no-cache',
    'TE' : 'Trailers',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}