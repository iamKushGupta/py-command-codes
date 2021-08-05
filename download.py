import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

download("https://yourwebsiteaddress.com/pagefiles/103952/1056x594/completeaddressoftargetfile.jpg")
