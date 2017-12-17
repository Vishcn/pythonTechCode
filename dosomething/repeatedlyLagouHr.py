# -*- coding: utf-8 -*-
__author__ = 'Vishcn'
import cookielib
import urllib2
import json
from bs4 import BeautifulSoup
import re
import time
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
    s = 'hiido_ui=0.41118479729630053; bbs_ed28_saltkey=OiSnR1jZ; bbs_ed28_lastvisit=1456103174; __wyy=174eb8781dd5497e8f6df1ff3bb9c49d; bbs_ed28_visitedfid=2017D1058D1362D1317; bbs_ed28_ulastactivity=34d7vDh03BPUP%2F2amqbOJ4X9O47xwQ0NPixDxBFij05Jst2ayHDm; pgv_pvi=3683792845; _ga=GA1.2.597920159.1456106791; wh=2%7C73837857_73837857%2C2%7C58640936_58640936; 595208759_lc=58640936; Hm_lvt_79c375aa39fc2aae3161264213dee7ec=1456106661,1456717419; Hm_lpvt_79c375aa39fc2aae3161264213dee7ec=1456897830; Hm_lvt_34a908ea88275f6ef0a72588f9c0be86=1456192213,1456192252,1456222387,1456717419; Hm_lpvt_34a908ea88275f6ef0a72588f9c0be86=1456897830; yyuid=247687090; username=gay1471481; password=887346BC6754EFCF7421F83CCD796D2D7CBE150B; osinfo=B42BB0FB1F5211FC84FEB96536C42426D43B2A3B; oauthCookie=7D0ADE87663F7D70A8A0E48609C864CB84B089B8C915134D73825019C37AD412C2B6805D4DA83D6B3E269D083AD613FAB29FFD5D1FCF4A6CB478EC47D58A54F95CBCAF8A6287EDC9B96E19943E9AFECBD575F92ED7F0EE6B3D5A18BA9D11AAC0175A38C99B70E20AD0FD2652C957080767FDB2ED146D6469A84078E2A78F0C0FB54520D5D074FFEF14C190BE2E0C9C9582FFA4B539504C909A41470985EC74C8E33655CFA07EBDE36A29C63E0F0FEFDA487FBC5A38C995741A256282EB21EE3E4F16671DD46CFA5DE4BAB78F2843C7B05C6D70B2F1DC11660DAF98FBA0FCEAF3AC4DABDA1A50E269CFF04B1721CD6230BF48AF599031345640813CB5D3C739751CD37529100BAE6E7C006E5D3D04FB83; JSESSIONID=5F7036FD256CCAC109C8B7964F9026D5; gh_username=gay1471481'
    a = s.split('; ')
    for b in a:
        c = b.split('=')
        if c[0] != 'opid_wx':
            print c[0]+':'+c[1]
            cookie.set_cookie(make_cookie(c[0],c[1]))

    #cookie.set_cookie(make_cookie('opid_wx', 'b'+i+'b619ce6fb3831966817ddc5d47ff20b6805d7e8eeb6b9cbbecd5d73947603ae59ca251a5814d9ad2bdd2a446880c36dc6f42f671dcc00a4f68dfc8a421b6398a5e701db97c6'))

    req = urllib2.Request("http://channel.yy.com/member/creation!displaySeedInfo.action?seed=112")
    req.add_header('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
    req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print response.read()

def b(c,d):

        # a = str(5355)+str(b) +str(7) +str(33)
        # a = str(i+3) +str(i+2) +str(i+1) + str(i)+ str(i+3)
        opener = urllib2.build_opener()
        # opener.addheaders.append(('Cookie','LGMOID=20161021090953-CC82210191834F529A442487B8E1AC89; user_trace_token=20161021090953-12fcaf79-972b-11e6-b588-525400f775ce; LGUID=20161021090953-12fcb207-972b-11e6-b588-525400f775ce; JSESSIONID=AD5331732FEF6EA00F9B57E6D8F867A7; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=http%3A%2F%2Factivity.lagou.com%2Factivity%2Fdist%2FshiliMax%2Fm_index.html%3Fdata%3D1686%26from%3Dtimeline%26isappinstalled%3D0; _ga=GA1.2.367096160.1477012193; LGSID=20161021102552-afd40977-9735-11e6-b5cd-525400f775ce; LGRID=20161021102842-158b5ae4-9736-11e6-b5cd-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1477012193,1477012774,1477016752; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1477016923'))
        # opener.addheaders.append(('Cookie','hiido_ui=0.41118479729630053; bbs_ed28_saltkey=OiSnR1jZ; bbs_ed28_lastvisit=1456103174; __wyy=174eb8781dd5497e8f6df1ff3bb9c49d; bbs_ed28_visitedfid=2017D1058D1362D1317; bbs_ed28_ulastactivity=34d7vDh03BPUP%2F2amqbOJ4X9O47xwQ0NPixDxBFij05Jst2ayHDm; pgv_pvi=3683792845; _ga=GA1.2.597920159.1456106791; wh=2%7C73837857_73837857%2C2%7C58640936_58640936; 595208759_lc=58640936; Hm_lvt_79c375aa39fc2aae3161264213dee7ec=1456106661,1456717419; Hm_lpvt_79c375aa39fc2aae3161264213dee7ec=1456897830; Hm_lvt_34a908ea88275f6ef0a72588f9c0be86=1456192213,1456192252,1456222387,1456717419; Hm_lpvt_34a908ea88275f6ef0a72588f9c0be86=1456897830; yyuid=247687090; username=gay1471481; password=887346BC6754EFCF7421F83CCD796D2D7CBE150B; osinfo=B42BB0FB1F5211FC84FEB96536C42426D43B2A3B; oauthCookie=7D0ADE87663F7D70A8A0E48609C864CB84B089B8C915134D73825019C37AD412C2B6805D4DA83D6B3E269D083AD613FAB29FFD5D1FCF4A6CB478EC47D58A54F95CBCAF8A6287EDC9B96E19943E9AFECBD575F92ED7F0EE6B3D5A18BA9D11AAC0175A38C99B70E20AD0FD2652C957080767FDB2ED146D6469A84078E2A78F0C0FB54520D5D074FFEF14C190BE2E0C9C9582FFA4B539504C909A41470985EC74C8E33655CFA07EBDE36A29C63E0F0FEFDA487FBC5A38C995741A256282EB21EE3E4F16671DD46CFA5DE4BAB78F2843C7B05C6D70B2F1DC11660DAF98FBA0FCEAF3AC4DABDA1A50E269CFF04B1721CD6230BF48AF599031345640813CB5D3C739751CD37529100BAE6E7C006E5D3D04FB83; JSESSIONID=5960E5AC2F82C52D1084C19651F375A5; gh_username=gay1471481'))
        # print a + "#######"
        tex = str(c)+str(d)+str(c)+str(d)
        f = opener.open('https://m.10010.com/NumApp/NumberCenter/qryNum?callback=jsonp_queryMoreNums&provinceCode=11&cityCode=110&monthFeeLimit=0&groupKey=85236889&searchCategory=3&net=01&amounts=200&codeTypeCode=&qryType=02&goodsNet=4&_=1498570954761&searchValue='+tex)
        a=  f.read()
        print tex
        a=a[20:]
        a=a[:-3]
        res_json = json.loads(a)
        # print res_json
        # print res_json['numArray']
        for e in res_json['numArray']:
            if e>10:
                print e
        soup = BeautifulSoup(f)
        # es_json = json.loads(res)
        # c = .split('numArray')
        # print c[1]
        items = soup.find_all("sid")
        for aa in items:
            if aa.getText().startswith( a ):
                print aa.getText()
            if aa.getText().endswith( a ):
                print aa.getText()
        # print "######"
        time.sleep(5)


if __name__ == '__main__':
    # for d in range(1,10):)
    # b(5,6)
        for c in range(1,10):
            for d in range(0,10):
                b(c,d)