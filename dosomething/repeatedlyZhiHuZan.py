# -*- coding: utf-8 -*-
__author__ = 'Vishcn'
import cookielib
import urllib2
#这个不对
def make_cookie(name, value):
    return cookielib.Cookie(
        version=0,
        name=name,
        value=value,
        port=None,
        port_specified=False,
        domain="ca.lagou.com",
        domain_specified=True,
        domain_initial_dot=False,
        path="/",
        path_specified=True,
        secure=False,
        expires=None,
        discard=False,
        comment=None,
        comment_url=None,
        rest=None
    )

def a(i):
    cookie = cookielib.MozillaCookieJar()
    s = '_za=47047347-0d59-42a7-af20-bc27bb1a2819; q_c1=3474077dd352493daf38c61261dcd3f9|1447462079000|1439467831000; cap_id="ZjE2ODA5MmMzNjI5NDg1YWJiMzBiZDI2YmY2ODhjNjk=|1448343152|188a4721b2f4ce34d9d0ec69d553d7e98eb6110d"; z_c0="QUFEQVJUWWhBQUFYQUFBQVlRSlZUWUNEZTFhc2dFWjZRNFZQUXJZZzE0ZjRickZMazBKVERRPT0=|1448343168|5a0f37b01135af73fea6ea3ac42630dfee574cbb"; _xsrf=de9f8c52397eec27f92f7d5a61b96456; __utma=51854390.1745068386.1449474804.1449651488.1449662051.15; __utmb=51854390.15.9.1449662762021; __utmc=51854390; __utmz=51854390.1449474804.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20131123=1^3=entry_date=20131123=1'
    a = s.split('; ')
    for b in a:
        c = b.split('=')
        if c[0] != 'opid_wx':
            print c[0]+'='+c[1]
            cookie.set_cookie(make_cookie(c[0],c[1]))

    cookie.set_cookie(make_cookie('opid_wx', 'a'+i+'f63b619ce670fb3831966817ddc5d47ff20b6805d7e8eeb6b9cbbecd5d73947603ae59ca251a5814d9ad2bdd2a446880c36dc6f42f671dcc00a4f68dfc8a421b6398a5e701db97c6'))

    req = urllib2.Request('http://www.zhihu.com/node/AnswerVoteBarV2')
    req.add_header('User-agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 MicroMessenger/6.3.7 NetType/WIFI Language/zh_CN')
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print response.read()

if __name__ == '__main__':
    for i in range(1, 10):
        print str(i)
        a(str(i))