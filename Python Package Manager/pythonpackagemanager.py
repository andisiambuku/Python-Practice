import requests

url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
print(response)
print(response.text)