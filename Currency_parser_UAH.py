import requests
from bs4 import BeautifulSoup

def get_curr_rate():
	source = requests.get('https://minfin.com.ua/currency/nbu/')
	soup_text = BeautifulSoup(source.text, "html.parser")

	lable = soup_text.find('table', {'class' : 'table-auto'})
	tr = lable.find('td', {'class' : 'responsive-hide'})
	return tr.text[1:6]

input(f"Курс доллара: {get_curr_rate()}")