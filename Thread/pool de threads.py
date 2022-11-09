import time
import concurrent.futures
import requests


img_urls = ['https://unsplash.com/photos/fxrwJGMCz_g/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjY4MDAyOTQ1&force=true'
            'https://unsplash.com/photos/bX9B9c-YasY/download?ixid=MnwxMjA3fDB8MXxzZWFyY2h8OXx8Ymx1ZSUyMGdhbGF4eXxlbnwwfHx8fDE2Njc5MTg3Nzg&force=true'
            ]


def download_image(img_url):


    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)
    
end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")
