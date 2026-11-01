import requests 
from bs4 import BeautifulSoup

from_currency="GBP"
to_currency=input("Enter the currency you want to convert to in capital and abbreviated: ")
e_url= f"https://v6.exchangerate-api.com/v6/615d165eec7df71ec8cb40d5/latest/{from_currency}"
url="https://books.toscrape.com//"

headers= {
    "User-Agent": "PriceScraperBotV1.0 (contact:rkkbeto@gmail.com)"
}
response=requests.get(url,headers=headers, timeout=10)
e_response=requests.get(e_url,headers=headers, timeout=10)
e_data=e_response.json()


rate=e_data["conversion_rates"][to_currency]
con_price= int(book_price) * rate
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
        "price": con_price
    }

    book_sort= ", ".join(book_item.values())
    all_books.append(book_sort)



print(all_books)