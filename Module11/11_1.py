import requests

response = requests.get('https://httpbin.org/get')
print(response.text)

response = requests.put('https://httpbin.org/put', data={'foo': 'bar'})
print(response.text)

response = requests.get('https://www.python.org/static/img/python-logo.png')
with open('python_logo.png', 'wb') as image:
    image.write(response.content)