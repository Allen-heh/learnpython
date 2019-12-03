from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    sender = 'xxxx@163.com'
    receivers = 'xxxx@qq.com'

    message = MIMEText('用python发送示例代码', 'plain', 'utf-8')
    message['From'] = Header('张楚岚', 'utf-8')
    message['To'] = Header('冯宝宝', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.163.com')

    smtper.login(sender, 'xxxx')
    smtper.sendmail(sender, receivers, message.as_string())
    print('ok!')

if __name__ == '__main__':
    main()
