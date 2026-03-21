import requests
from bs4 import BeautifulSoup

sahifa= "https://cbu.uz/uz/"
r=requests.get(sahifa)


soup = BeautifulSoup(r.text, 'html.parser')
news=soup.find_all(class_="exchange__item_value")
print(news[0].text)




import requests
from pprint import pprint as p

API_KEY = "90aa7088f77c45db3d146b28"

currency='USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
response = requests.get(url)
kurs = response.json()['conversion_rate']
p(f"1 dollar kursi {kurs} so'mga teng")