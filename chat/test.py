import requests

url = "https://www.google.com/search?q=dolar"

r = requests.get(url)

print(r.text)