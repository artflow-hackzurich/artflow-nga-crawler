import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

start_id = 461264
download_count = 1024

for i in range(start_id, start_id + download_count):
    detail_url = 'https://customprints.nga.gov/detail/' + str(i)
    html_text = requests.get(detail_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    image_tag = soup.find('link', rel='image_src')

    if image_tag is not None:
        image_url = image_tag['href']

        if image_url is not None:
            url_details = urlparse(image_url)
            url_filename = os.path.basename(url_details.path)
            response = requests.get(image_url)
            file = open('data/' + url_filename, 'wb')
            file.write(response.content)
            file.close()

print('Downloaded ' + download_count + ' images')
