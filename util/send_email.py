import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import sys
sys.path.append("d:/pythonworkspace/interfaceframework")


class SendEmail:
    def mail(self, context):
        ret = True
        try:
            receiver = "952071013@qq.com"
            sender = "568601749@qq.com"
            msg = MIMEMultipart()
            msg.attach(MIMEText(context, 'plain', 'utf-8'))#正文
            msg['From'] = formataddr(["软肋", sender])
            msg['To'] = formataddr(["萨比", receiver])
            msg['Subject'] = "zxl的自动化接口测试报告"#标题

            # 构造附件1，传送文件
            att1 = MIMEText(open('e:/py/pythonworkspace/interfaceframework/dataconfig/interface.xlsx', 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="interface.xlsx"'
            msg.attach(att1)

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，默认端口是25
            server.login(sender, "zerfnkvnvnrebcie")    # 括号中对应的是发件人邮箱账号、邮箱密码  zerfnkvnvnrebcie
            server.sendmail(sender, receiver, msg.as_string())   # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()   # 这句是关闭连接的意思
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        if ret:
            return "邮件发送成功"
        else:
            return "邮件发送失败"


if __name__ == "__main__":
    a = SendEmail()
    # b=1
    # res = a.mail("正确数为%d" %b)
    res = a.mail("aaaa")
    print(res)
