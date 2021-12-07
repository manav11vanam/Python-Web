import requests
from tqdm import tqdm

link = 'https://funksyou.com/fileDownload/Songs/128/34455.mp3'

response = requests.get(link, stream=True)
print(response)

try:
    total = int(response.headers.get('content-length'))
except:
    print('FAILED')
    quit()

with open('Naagin.mp3', 'wb') as f:
    print('Downloading', f.name)
    for data in tqdm(response.iter_content(chunk_size=total//100), total=101):
        f.write(data)
