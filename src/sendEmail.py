#!/usr/bin/env python
#encoding=utf8
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import smtplib   
import base64

#
# this is email conf 
#
class email_conf:
    # 附件 list
    attacnemt = ['../test/中文.txt']
    # 发送人 list
    to = ['1203316364@qq.com']
    content = '../test/test.html'
    host = '1203316364@qq.com' 
    server = 'smtp.exmail.qq.com'
    user = '1203316364@qq.com'
    password = '*'
    header = '运营报表'
     

def sendEmalSSL( conf = email_conf() ):
    #构造
    msg = MIMEMultipart()

    #邮件内容 
    contentFile = conf.content
    msg.attach(MIMEText(open( contentFile ).read(),'html'))

    #添加附件， 特别是 文件名为中文时 需要转换为 gb2312
    fileList = conf.attacnemt
    if len(  fileList  ) > 0:
        for attachmentFile in fileList:
            att = MIMEText(open(attachmentFile, 'r').read(), 'base64', 'utf8')
            att["Content-Type"] = 'application/octet-stream'
            formateFileName = getFileName( attachmentFile )
            att["Content-Disposition"] = 'attachment; filename="' + formateFileName.decode('utf8').encode('gb2312') + '"'
            msg.attach(att)
    # header
    msg['to'] = ','.join(conf.to)
    msg['from'] = conf.host
    msg['subject'] = conf.header

    #email 
    server = smtplib.SMTP_SSL(conf.server,465)  

    # 调试
    #server.set_debuglevel(1)

    server.login(conf.user,conf.password)  

    server.sendmail( conf.host,','.join(conf.to),msg.as_string() );

    server.close();

# get file name by path
def getFileName(path):
    split = path.split('/')
    fileName = split[len(split) -1]
    return fileName
     

sendEmalSSL()
