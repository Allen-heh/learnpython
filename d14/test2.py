from requests import head
header=head('https://github.com/get')
print('text:',header.text) #不会返回内容信息
print('headers:',header.headers) #返回头信息
print(header.cookies.items()) #返回cookies元组列表
