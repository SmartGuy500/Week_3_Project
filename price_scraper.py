from pickle import GET

import requests 
from bs4 import BeautifulSoup
import pandas as pd


url="https://books.toscrape.com//"

headers= {
    "User-Agent": "PriceScraperBotV1.0 (contact:rkkbeto@gmail.com)"
}
try:    
    response=requests.get(url,headers=headers, timeout=10)
except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")


"""
    from_currency="GBP"
    to_currency=input("Enter the currency you want to convert to in capital and abbreviated: ")
    e_url= f"GET https://v6.exchangerate-api.com/v6/615d165eec7df71ec8cb40d5/pair/{from_currency}/{to_currency}/{int_price}"
    e_response=requests.get(e_url,headers=headers, timeout=10)
    e_data=e_response.json()
    rate=e_data["conversion_rates"][to_currency]
    con_price= int(int_price) * rate

    for price in cards:
            
            base_price=price.select("p.price_color")[0].get_text()
            int_price=base_price.replace("£","")
            con_price= int(f"https://v6.exchangerate-api.com/v6/615d165eec7df71ec8cb40d5/pair/{from_currency}/{to_currency}/{int_price}")
"""
#print(response)
#print(response.status_code)
#print(response.content)

soup=BeautifulSoup(response.content, "html.parser")
#print(soup.prettify)

cards=soup.select("article.product_pod")
#print(len(cards))

all_books=[]


for book in cards:
    book_title=book.select("h3 a")[0]["title"]
    book_availability=book.select("p.instock.availability")[0].get_text().strip()
    book_price=book.select("p.price_color")[0].get_text()


    book_item={
        "title": book_title,
        "availability": book_availability,
        "price": book_price
    }

    book_sort= ", ".join(book_item.values())
    all_books.append(book_sort)



#print(all_books)

df=pd.DataFrame(all_books, columns=["Books"])
print(df.head())
df.to_excel("books.xlsx", index=False)
df.to_csv("books.csv", index=False)

