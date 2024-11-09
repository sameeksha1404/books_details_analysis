import requests
from bs4 import BeautifulSoup
import json

# Base URL for books to scrape
base_url = "https://books.toscrape.com/catalogue/page-{}.html"
books = []

# Scrape the first 5 pages to gather more than 100 books
for page in range(1, 6):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    for book in soup.select('.product_pod'):
        title = book.h3.a['title']
        price = book.select_one('.price_color').text
        availability = book.select_one('.availability').text.strip()
        
        # Get the link to the book's detail page
        book_url = "https://books.toscrape.com/catalogue/" + book.h3.a['href']
        book_response = requests.get(book_url)
        book_soup = BeautifulSoup(book_response.content, 'html.parser')
        
        # Scrape additional details
        genre = book_soup.select_one('.breadcrumb li:nth-of-type(3) a').text if book_soup.select_one('.breadcrumb li:nth-of-type(3) a') else "Unknown Genre"
        isbn = book_soup.select('table.table-striped tr')[0].select('td')[0].text if book_soup.select('table.table-striped tr') else "Unknown ISBN"
        description = book_soup.select_one('#product_description ~ p').text if book_soup.select_one('#product_description ~ p') else "No description available."
        
        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "genre": genre,
            "ISBN": isbn,
            "description": description
        })

# Create a JSON file with the scraped data
with open('books.json', 'w') as file:
    json.dump(books, file, indent=4)

print("Scraped data saved to books.json")
