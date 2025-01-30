from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.jumia.co.ke/mlp-samsung-shop/').text
soup = BeautifulSoup(html_text, 'html.parser')

header = soup.find('div', class_='-pvs col12')
header_text = header.h1.text[:7]

products = soup.find_all('article', class_='prd _fb col c-prd')

for index, product in enumerate(products):
    name = product.find('h3', class_='name').text.strip()
    price = product.find('div', class_='prc').text.strip()
    rating = product.find('div', class_='stars _s')
    rating_elements = rating.text.strip() if rating else 'no rating'
    link = product.find('a', class_='core')['href']
    full_link = f'https://www.jumia.co.ke/{link}'
    print(f'company Name: {header_text} \n'
          f'product: {name} \n'
          f'Price: {price} \n'
          f'Rating: {rating_elements} \n'
          f'link: {full_link} \n')

    with open('JumiaSamsungProduct', 'w') as jumiaScraping:
        jumiaScraping.write(f'company Name: {header_text} \n')
        jumiaScraping.write(f'product: {name} \n')
        jumiaScraping.write(f'Price: {price} \n')
        jumiaScraping.write(f'Rating: {rating_elements} \n')
        jumiaScraping.write(f'link: {full_link} \n')
        jumiaScraping.write(f'file saved: {index}')



