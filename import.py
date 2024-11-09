import json
from pymongo import MongoClient

# Step 2: Read the JSON file
with open('books.json', 'r') as file:
    books = json.load(file)

# Step 3: Connect to MongoDB
client = MongoClient('localhost', 27017)  
db = client['books_database']  #  database name
collection = db['books_collection']  # collection name

# Step 4: Insert the data into MongoDB
collection.insert_many(books)

print("Data imported successfully into MongoDB.")
