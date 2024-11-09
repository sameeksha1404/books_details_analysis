This uses web scraping and data analysis to design and  gather comprehensive book details from a specified website and store them in MongoDB for in-depth analysis. This project leverages Python’s BeautifulSoup and Requests libraries to efficiently scrape data such as book titles, availablity, genres, isbn, description, and prices. Once collected, the data is organized and stored in MongoDB, a NoSQL database that supports flexible schema designs ideal for handling diverse book attributes.

Using MongoDB's aggregation framework, it enables detailed analytics, uncovering insights like popular genres,  price trends over time. These analytics can provide valuable information for readers, researchers, and online bookstores to understand reading trends and preferences. 


The source data is web content scraped from the website Books to Scrape. Specifically, the script targets the book catalog pages on this site. 
1.	Base URL: The script uses https://books.toscrape.com/catalogue/page-{}.html as the base URL pattern to access different pages of the book catalog. Each page URL is formed by replacing {} with the page number (from 1 to 5 in this case).

2.	Book Listings: On each catalog page, the script looks for HTML elements with the class product_pod, which represents individual book entries. Each entry includes:
o	Title: Extracted from the title attribute of the <a> tag within the <h3> tag.
o	Price: Extracted from the price_color class.
o	Availability: Extracted from the availability class.

3.	Book Detail Pages: The script follows links to each book's detail page to gather additional information. The detail page includes:
o	Genre: Extracted from the third breadcrumb link.
o	ISBN: Extracted from the first <td> in the same table.
o	Description: Extracted from the <p> tag that follows the #product_description id.

4.	Scraped Data: The script collects the following data fields for each book:
o	Title
o	Price
o	Availability
o	Genre
o	ISBN
o	Description
This data is then saved into a JSON file (books.json) for further use or analysis.
