# Sending emails with attachments using Python  

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = "email_address_of_the_sender"
toaddr = "email_address_of_the_receiver"

# MIMEMultipart 
msg = MIMEMultipart() 

# senders email address 
msg['From'] = fromaddr 

# receivers email address 
msg['To'] = toaddr 

# the subject of mail
msg['Subject'] = "subject_of_the_mail"

# the body of the mail 
body = "body_of_the_mail"

# attaching the body with the msg 
msg.attach(MIMEText(body, 'plain')) 

# open the file to be sent
# rb is a flag for readonly 
filename = "file_name_with_extension"
attachment = open("Path of the file", "rb") 

# MIMEBase
attac= MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
attc.set_payload((attachment).read()) 

# encode into base64 
encoders.encode_base64(attc) 

attc.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# attach the instance 'p' to instance 'msg' 
msg.attach(attc) 

# creates SMTP session 
email = smtplib.SMTP('smtp.gmail.com', 587) 

# TLS for security 
email.starttls() 

# authentication 
email.login(fromaddr, "Password_of_the_sender") 

# Converts the Multipart msg into a string 
message = msg.as_string() 

# sending the mail 
email.sendmail(fromaddr, toaddr, message) 

# terminating the session 
# s.quit() is an example if your variable is `s.sendmail()`
email.quit() 
