import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.au/s?k=apple&crid=3FDFSX11F6BY2&sprefix=ap%2Caps%2C442&ref=nb_sb_noss_2'

# url = 'https://www.linkedin.com/jobs/'

head = ({'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/126.0.0.0 Safari/537.36'})


webpage = requests.get(url,headers=head)

soup = BeautifulSoup(webpage.content, 'html.parser')
links = soup.find_all("a", attrs={"class": "a-link-normal s-no-outline"})

link=(links[0].get('href'))

product_list = "https://amazon.com.au" + link
print(product_list)
new_webpage = requests.get(url, headers=head)
new_soup = BeautifulSoup(new_webpage.content, 'html.parser')
a=new_soup.find("span",attrs={"class":'a-price-whole'})
print(a.text)
ratings=new_soup.find("span",attrs={"class":'icon a-icon-star a-star-4-5 cm-cr-review-stars-spacing-big'})
print(ratings)