# -*- coding: utf-8 -*-
'''
Created on Nov 15, 2011

@author: luochounami
'''

from email.Header import Header
from email.mime.text import MIMEText
import logutil
import smtplib
import traceback

from_smtp_server = 'smtp.exmail.qq.com'
from_mail_user = 'luozhaobo@buding.cn'
from_mail_passwd = 'yuxiang19,./'

def sendmail(content, subject='Auto-Email', to='luozhaobo@buding.cn'):
    '''Send a mail.'''
    try:
        logutil.logger.logger.debug('Send a mail "%s" to %s.' % (subject, to))
        msg = MIMEText(str(content), _charset='utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = from_mail_user
        msg['To'] = to
        s = smtplib.SMTP()
        s.connect(from_smtp_server)
        s.login(from_mail_user, from_mail_passwd)
        s.sendmail(from_mail_user, [to], msg.as_string())
        s.quit()
        logutil.logger.logger.debug('Send the mail succeed.')
        return True
    except:
        logutil.logger.logger.debug('Send the mail failed.')
        logutil.logger.logger.exception(traceback.format_exc())
        return False

if __name__ == '__main__':
    sendmail('This is a test mail.\n继续测试。')
