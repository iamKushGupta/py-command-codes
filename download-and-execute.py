#!/usr/bin/env python

import requests
import subprocess
import os
import tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

download("http://yourlink.com/file_to_be_downloaded.pdf")
subprocess.Popen("file_to_be_downloaded.pdf", shell=True)

download("https://anotherlink.com/yourfile.png")
subprocess.call("yourfile.png", shell=True)

# Uncomment to execute them.
#os.remove("file_to_be_downloaded.pdf")
#os.remove("yourfile.png")
