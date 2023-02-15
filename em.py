
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
fromaddr = "9namancam9@gmail.com"
toaddr = "9namancam@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Increase"
body = "Increase more than opening"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "30101975t")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()