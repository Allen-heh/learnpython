from time import time
from threading import Thread

import requests

class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/opt/heh/d14/pic/' + filename, 'wb') as f:
            f.write(resp.content)

def main():
    resp = requests.get('http://api.tianapi.com/meinv/?key=7f7384757414a365893d1d9e22be234d&num=10&rand=5')
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        DownloadHanlder(url).start()


if __name__ == '__main__':
    main()
