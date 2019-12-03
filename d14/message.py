import urllib.parse
import http.client
import json

def main():
    host = '106.ihuyi.com'
    sms_send_uri = '/webservice/sms.php?method=Submit'
    params = urllib.parse.urlencode({'account': 'C80166704', 'password': 'a41ec7b1a9736a7f002aafebd0d7aa02', 'content': '您的验证码是：147258。请不要把验证码泄露给其他人。', 'mobile': '17310301725', 'format': 'json'})
    print(params)
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()

if __name__ == "__main__":
    main()
