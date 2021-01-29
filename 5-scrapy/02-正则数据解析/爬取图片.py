import requests

url = 'https://pic.qiushibaike.com/system/pictures/12369/123696902/medium/XSL7AZWCOIXDYYT0.jpg'

response = requests.get(url=url).content
with open('1.jpg', 'wb') as fp:
    fp.write(response)
