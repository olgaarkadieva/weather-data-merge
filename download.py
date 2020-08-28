import os
import shutil
import tempfile
import urllib.request
import zipfile

from bs4 import BeautifulSoup


# In this file i am extracting data from website using BeautifulSoup library ... downlaoded data will be stored in data directory 

base_url = "http://www.submm.caltech.edu/submm.org/site/weather/" # url to scrape website
datadir = "./data/"  #data directory

print(f"scraping data from {base_url}")
with urllib.request.urlopen(base_url + "cc.html") as response:
    #using bs4 resposne to collect data from resquested url 
    soup = BeautifulSoup(response.read(), "html.parser")

    datalinks = [link["href"] for link in soup.findAll('a') if "txt" in link.attrs["href"]] # find all the anchor tag with txt extension 
    # and store in varaible

if not os.path.exists(datadir):
    #create folder or directory if it does not exists.
    os.mkdir(datadir)
assert os.path.isdir(datadir) # check if directory path refers to correct path location of directory  

for i,datalink in enumerate(datalinks):
    # we have already store link of file in datalink variable now we will download files of every datalink to local system and extract to data directory  
    print(f"downloading ({i}/{len(datalinks)}) {datalink}")
    url = base_url + datalink
    with urllib.request.urlopen(url) as response:
        with tempfile.TemporaryFile() as tf:
            shutil.copyfileobj(response, tf)
            tf.seek(0)
            # storing zip file in tempfile vatriable  
            with zipfile.ZipFile(tf, 'r') as zf:
                zf.extractall(datadir)
                #extract zip file in data directory


#Now we have downlaoded data from website now we will merge data into single file and remove unnecessary data in merge_data.py file               

