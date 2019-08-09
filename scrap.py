from bs4 import BeautifulSoup   
import requests
import pandas as pd

# membuat soup object untuk web scraping dari website www.99.co.id
url = 'https://www.99.co/id/perumahan'
webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, 'html.parser')

# mengambil data luas rumah dan disimpan dalam list luas
luas = []
for element in soup.find_all(title = 'Luas Bangunan'):
    luas.append(int(element.get_text().split('m')[0]))
# print(luas)

# mengambil data harga rumah dan disimpan dalam list harga
harga = []
for element in soup.find_all(itemprop = 'price'):
    harga.append(int(element.get('content')))
# print(harga)

'''
hasil data harga dan luas rumah akan berubah tergantung data 
yang dimunculkan web saat kita melakukan request.get dan hanya terbatas 16 data
'''

# membuat pandas dataframe berisi harga dan luas rumah
rumah = pd.DataFrame({
    'luas':luas, 'harga':harga
})
print(rumah)
# rumah.to_csv('rumah.csv') # bila ingin menyimpan harga dan luas rumah dalam file csv