#!/usr/bin/env python
#encoding=utf8
from email.Header import Header
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import smtplib   

import conf
 

#配置
conf = conf.email_conf()


#邮件内容 
contentFile = conf.content
msg = MIMEText(open( contentFile ).read())

#添加附件， 特别是 文件名为中文时 需要转换为 gb2312
fileList = conf.attacnemt
if len(  fileList  ) > 0:
    for attachmentFile in fileList:
        att = MIMEText(open(attachmentFile, 'rb').read(), 'base64', 'utf8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="' + attachmentFile.decode('utf8').encode('gb2312') + '"'
        msg.attach(att)

# header
msg['to'] = conf.to
msg['from'] = conf.host
msg['subject'] = conf.header


#email 

server = smtplib.SMTP()  
server.connect(conf.server)  
server.login(conf.user,conf.password)  
server.sendmail( conf.host,conf.to,msg.to_string() );
server.close();
