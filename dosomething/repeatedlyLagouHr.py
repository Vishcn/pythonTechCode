# -*- coding: utf-8 -*-
__author__ = 'Vishcn'
import cookielib
import urllib2
#这个是拉钩最美HR评选刷票用的小脚本
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
    s = '_ga=GA1.3.1792343653.1449476762; _gat=1; JSESSIONID=A064BA2EFCB29ABEF834B578099FCDBB; cookie_activity_uv_=cookie_activity_uv_CAREERISM-THREAD-LEVEL-NAVIGATION_hr_H5; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1449578043; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1449476762,1449533180; LGMOID=20151207162556-CDE57677F49D70E1CCC9EC27C67B4725; LGRID=20151208203403-g71a7e45-9da7-11e5-bd53-5254005c3644; LGSID=20151208202238-5eb346ed-9da6-11e5-bd53-5254005c3644; LGUID=20151207162601-86773457-9cbc-11e5-a17a-525400f775ce; PRE_HOST=; PRE_LAND=http%3A%2F%2Fca.lagou.com%2Fcareerism%2FbestEmployers%2Fvote%2Fh5%2Fhr%2F2493.html%3Fauthed%3Dauthed%26accessToken%3DOezXcEiiBSKSxW0eoylIeODsYKQKmHyoKZbDczha6EpM5UMskhkTPOxhMSVIIoMAjommMc36bgbktvTdwXGOmgWZXP5U97AhK2ULKdHZd65UfN4Me4j2XM6yATmqLke9rVshgV1b_rkprl37O6VyXw%26from%3Dtimeline%26isappinstalled%3D0; PRE_SITE=; PRE_UTM=; _ga=GA1.2.1792343653.1449476762; opid_wx=f73b219ce670fb3831966817ddc5d47ff20b6805d7e8eeb6b9cbbecd5d73947603ae59ca251a5814d9ad2bdd2a446880c36dc6f42f671dcc00a4f68dfc8a421b6398a5e701db97c6; pgv_pvi=3242180608; pgv_si=s7425828864; user_trace_token=20151207162556-ddf74c6a5c6642819d5fa55cec1e9a50'
    a = s.split(' ')
    for b in a:
        c = b.split('=')
        if c[0] != 'opid_wx':
            cookie.set_cookie(make_cookie(c[0],c[1]))

    cookie.set_cookie(make_cookie('opid_wx', 'a'+i+'f63b619ce670fb3831966817ddc5d47ff20b6805d7e8eeb6b9cbbecd5d73947603ae59ca251a5814d9ad2bdd2a446880c36dc6f42f671dcc00a4f68dfc8a421b6398a5e701db97c6'))

    req = urllib2.Request("http://ca.lagou.com/careerism/bestEmployers/vote/pc/vote.json?applyType=62&id=2796")
    req.add_header('User-agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 MicroMessenger/6.3.7 NetType/WIFI Language/zh_CN')
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print response.read()

if __name__ == '__main__':
    for i in range(1, 10):
        print str(i)
        a(str(i))