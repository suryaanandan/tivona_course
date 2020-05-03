#Question 2

import sys
import smtplib 
import os.path
import requests
import traceback
from email import encoders 
from bs4 import BeautifulSoup
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email.mime.multipart import MIMEMultipart 


#Code to download image from wikipedia
city = input("\nPlease enter city name to download image of the city from wikipedia  : ")
url = "https://en.wikipedia.org/wiki/"
url = url + city
response = requests.get(url)
html_text = response.content

soup = BeautifulSoup(html_text,'html.parser')
infobox = soup.find("table", {"class":"infobox"})
image_tag = infobox.find("img")
src = image_tag.attrs["src"]
if src.startswith("//"):
   src = url.split("//")[0] + src
with open(city,"wb") as file :
            response = requests.get(src)
            content = response.content
            file.write(content)
            print("Image downloaded\n")




# code to send downloaded image in mail
print("\nPlease provide required details to send the downloaded image in mail to your friend\n")
msg = MIMEMultipart() 

# Getting sender mail id
fromaddr = input("Please enter send mail id : ")
# storing the senders email address   
msg['From'] = fromaddr 

# Getting password to login
mail_password = input("Please enter your mail password to login : ")

# Getting receiver mail id
toaddr = input("Please enter receiver mail id : ")
# storing the receivers email address  
msg['To'] = toaddr 

 
# storing the subject 
subject = "Image of " + city + " in wikipedia" 
msg['Subject'] = subject
  
# string to store the body of the mail 
body = "Hi, \nThis image has been downloaded from wikipedia and sent using python"
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
filename = city

attachment = open(filename, "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 

# Converts the Multipart msg into a string 
text = msg.as_string()
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
 
try : 
    s.login(fromaddr, mail_password)  

    # sending the mail
    s.sendmail(fromaddr, toaddr, text) 
    print("\nMail sent successfully")
    print("\nIf you are using gmail to sent mails from Python, and your work is done then please disable Access for less secure apps in your gmail settings. Because smtp is less secured app\n")
except smtplib.SMTPException: 
    print("\nIf you are using gmail, by default smtp is blocked. So if you want to send mails from your Python, you need to enable Access for less secure apps in your gmail settings.\n")
    traceback.print_exc(file=sys.stdout)
    sys.exit()
s.quit() 

