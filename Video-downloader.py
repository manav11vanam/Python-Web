import requests
import re
from tqdm import tqdm
from bs4 import BeautifulSoup
import os

url = "http://anilist1.ir/Series/Silicon%20Valley/S05/1080p%20x265/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
# print(soup.prettify())
a_tags = soup('a')
links = []
for a in a_tags:
    link = a.get("href")
    if not link.startswith("Sil"):
        continue
    links.append(link)

# print(links)
os.makedirs("Silicon Valley", exist_ok=True)
os.chdir("Silicon Valley")
os.makedirs("S03", exist_ok=True)

for link in links:
    fname = " ".join(link.split(".")[:3])
    fname = fname + ".mkv"
    # print(fname)
    with open(fname, 'wb') as f:
        print("Downloading" , fname)
        response = requests.get((url + link), stream=True)
        try:
            total_length = int(response.headers.get('content-length'))
        except:
            print("Operation failed. Program exitting")
            quit()

        for data in tqdm(response.iter_content(chunk_size=total_length//500), total = 501):
            f.write(data)




# fname = re.findall('Brooklyn.Nine-Nine.S07E[0-9]+.+', link)[0]
# with open(fname, 'wb') as f:
#     print("Downloading" , fname)
#     response = requests.get(link, stream=True)
#     total_length = response.headers.get('content-length')
#     if total_length is None:
#         f.write(response.content)
#     else:
#         dl = 0 # written data length
#         total_length = int(total_length)
#         for data in response.iter_content(chunk_size=total_length//50):
#             dl += len(data)
#             f.write(data)
#             done = int(50*dl/total_length)
#             print('\n[{}{}]'.format('='*done, ' '*(50-done)), flush=True)
