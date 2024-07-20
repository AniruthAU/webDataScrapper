import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL and headers
url = 'https://www.amazon.com.au/s?k=apple&crid=3FDFSX11F6BY2&sprefix=ap%2Caps%2C442&ref=nb_sb_noss_2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

webpage = requests.get(url, headers=headers)
soup = BeautifulSoup(webpage.content, 'html.parser')

# Find all product links
product_links = soup.find_all("a", attrs={"class": "a-link-normal s-no-outline"})

# Lists to store product information
products = []
prices = []
ratings = []

# Iterate through each product link
for link in product_links:
    product_url = "https://www.amazon.com.au" + link.get('href')
    product_page = requests.get(product_url, headers=headers)
    product_soup = BeautifulSoup(product_page.content, 'html.parser')

    # Find product name
    product_name = product_soup.find("span", attrs={"id": "productTitle"})
    if product_name:
        products.append(product_name.get_text(strip=True))
    else:
        products.append("N/A")

    # Find product price
    product_price = product_soup.find("span", attrs={"class": 'a-price-whole'})
    if product_price:
        prices.append(product_price.get_text(strip=True))
    else:
        prices.append("N/A")

    # Find product rating
    product_rating = product_soup.find("span", attrs={"class": "a-icon-alt"})
    if product_rating:
        ratings.append(product_rating.get_text(strip=True))
    else:
        ratings.append("N/A")

# Create a DataFrame with the collected data
df = pd.DataFrame({
    "Product Name": products,
    "Price": prices,
    "Rating": ratings
})

# Display the DataFrame
print(df)
