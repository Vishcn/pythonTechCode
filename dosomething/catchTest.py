# _*_coding:utf8_*_
# coding=utf8
__author__ = 'vish23n'
import urllib
from util import textoperator
from bs4 import BeautifulSoup
import time
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')



def getDan(text):
    text = re.sub(r"'", "''", text)
    return text

def getTime(text):
    text = textoperator.untag(text)
    text = re.sub(r'\|', '', text)
    text = text.replace(" ", "")
    return text

def getFilter(text):
    filer1 = re.search(r'.*?分享.*?', text, re.S)
    if filer1:
        return True
    return False


def getId(text):
    text = re.search(r'(?<=tid=).*?(?=&)', text, re.S)
    if text:
        text = text.group(0)
    return text;


def getPageCount(text):
    text = text.replace("爱奇艺吧（www.aqyba.com），", "")
    text = text.replace("爱奇艺最新账号：", "")
    text = text.replace("。", "")
    text = text.replace("电脑用户双击账号（密码）即可选中复制", "")
    text = text.replace("每小时更新一批爱奇艺最新vip账号，全天不间断更新爱奇艺会员账号，而且保证每个爱奇艺账号都是可以使用的，如果账号失效，请大家留言，看到后会第一时间进行更新，同时也欢迎大家把我们的网址加入浏览器收藏，方便大家第一时间获取最新爱奇艺会员账号", "")
    text = text.replace("\n\n", "")
    return text


def getHtml(text):
    text = re.sub('1.html', '', text)
    return text


def getText(text):
    text = re.sub(r'\\', '\\\\', text)
    text = re.sub(r'\'', '\\\'', text)
    return text


def getSenderId(text):
    text = re.sub('http://www.leiphone.com/news/', '', text)
    text = re.sub('.html', '', text)
    return text

def getFrom(text):
    text = re.sub('稿源：', '', text)
    return text
def filterDiv(abc):
    temp = abc.find(class_='lp-proCard clr')
    print str(temp)
    text = re.sub(str(temp), '', str(abc))
    return getDan(text)

def getItemInfo(id,url):
    newf = urllib.urlopen('http://aqyba.com/'+ url)
    html = newf.read()
    soup = BeautifulSoup(html)
    print id
    data = {}
    # data['title'] = soup.find('h1').get_text()
    timespan = soup.find(class_='t_f')
    data['content'] = getPageCount(timespan.get_text())
    data['id'] = id
    try:
        print data['content']
        text =  re.sub('----[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]', "飞鸟会员共享", data['content'])
        print text
        try:
            # print unicode(data['content'])
            urll = 'http://www.feiniao.me/sendWeibo.php?conent='+ data['content']
            # abc = urllib.urlopen(urll)
            # dd = abc.read()
            # print urll

        except Exception as err:
            print(err)
    except:
        print "same data"

def getList(aa):
    thispage = aa
    newf = urllib.urlopen(thispage)
    html = newf.read()
    soup = BeautifulSoup(html)
    items = soup.find_all("tbody")
    if len(items) >0:
        for item in items:
            print item.get("id");
            if item.get("id").startswith("normalthread"):
                try:
                    item_ = item.find_all("a")
                    item_a = item_[2]

                    getItemInfo(getSenderId(item_a.get("href")),item_a.get("href"))
                except:
                    print "catch Exception"

while True:

        ISOTIMEFORMAT='%Y-%m-%d %X'
        getList('http://aqyba.com/forum-2-1.html')
        print  'I m live start catch version:2(qiyi),time:' +time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
        mint = time.strftime( '%M', time.localtime( time.time() ) )
        print mint
        if mint =='01' or mint =='00' :
            try:
              getList('http://aqyba.com/forum-2-1.html')
              time.sleep(20)
            except:
              print "catch Exception"
        print  'end catch:' +time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
        time.sleep(9)
        sys.stdout.write("hello python world catch qiyi\n")
        sys.stdout.flush()