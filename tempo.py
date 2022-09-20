from bs4 import BeautifulSoup
import requests


html= requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp").content

soup=BeautifulSoup(html , 'html.parser')

resume= soup.find(class_='gray -line-height-24_center')
tempmin= soup.find(id='min-temp-1')
temmax = soup.find(id='max-temp-1')


print("\n Resumo :" + resum.text)
print("temp. Minima: " + tempmin.string)
print("temp. Max:" + tempmax.string)