# _*_coding:utf8_*_
__author__ = 'meng'
import re
import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf8')

def saveList(date):
    # conn = MySQLdb.connect(host='10.86.32.93',
    #                        port   = 3322,
    #                        user='root',
    #                        passwd='b6f3g2',
    #                        db='syshotel',
    #                        charset='utf8')
    conn = MySQLdb.connect(host='sqld.duapp.com',
                           port   = 4050,
                           user='5773c830686545f39d7f36f09f38fde3',
                           passwd='e31d32500f964db3afd1efe406dcd08f',
                           db='cStCPZavTNxgbaBFMreF',
                           charset='utf8')
    cursor = conn.cursor()
    Sql = "insert into `news_info` ( `create_time`,`title`,`title_img_src`, `description`, `content`, `real_from`, `from_url`, `from_name`, `from_id`, `real_create`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    Sql %= ( date['create_time'],getDan(str(date['title'])),
             date['title_img_src'],
             getDan(str(date['description'])),
             getDan(str(date['content'])),
             '', '', date['from_name'],

    date['from_id'],
    date['create_time'])
    cursor.execute(Sql)

    conn.commit()
    conn.close()
    cursor.close()

def getDan(text):
    text = re.sub(r"'", "''", text)
    return text