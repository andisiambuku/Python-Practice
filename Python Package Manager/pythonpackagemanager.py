import requests
from collections import Counter

url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
print(response)
print(response.text)
text_set = response.text
text_list = text_set.split()
text_count = Counter(text_list)
print(text_count.most_common(10))
