import urllib
from urllib import request, parse
import ssl

def urlResponse():
    '''
        用于解决ssl验证问题，有两个方法
    '''
    # context = ssl._create_unverified_context() # 方法 1
    ssl._create_default_https_context = ssl._create_unverified_context  # 方法 2

    # with request.urlopen('https://api.douban.com/v2/book/2129650', context=context) as f:
    with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))

def imitateReq():
    req = request.Request('http://www.douban.com/')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    ssl._create_default_https_context = ssl._create_unverified_context  # 方法 2 : 解决ssl验证
    with request.urlopen(req) as f:
        print('Status', f.status, f.reason)
        for k, v in f.getheaders():
            print("%s %s" % (k, v))
        print("Data:", f.read().decode('utf-8'))

def imitatePostReq():
    print('Login to weibo.cn...')
    email = input('Email: ')
    passwd = input('Password: ')
    loginData = parse.urlencode([('username', email), ('passowrd', passwd), ('entry', 'mweibo'), ('client_id', ''), ('savestate', '1'), ('ec', ''),
                                 ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')])
    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer',
                   'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
    ssl._create_default_https_context = ssl._create_unverified_context  # 方法 2 : 解决ssl验证

    with request.urlopen(req, data=loginData.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))

imitatePostReq()