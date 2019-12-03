import requests  #pip3 install requests
import json

def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    print(resp)
    print(data_model)
    #for news in data_model['newslist']:
    #    print(news['title'])

if __name__ == "__main__":
    main()
