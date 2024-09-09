import json

from mongoengine import connect

from models import Author, Quote

connect(
    "book_db",
    host="mongodb+srv://harley029:8lyrMibko@cluster0.b6lozo9.mongodb.net/?retryWrites=true&w=majority",
)
# Читання файлу авторів
with open("authors.json") as f:
    authors_data = json.load(f)

# Читання файлу цитат
with open("quotes.json") as f:
    quotes_data = json.load(f)

# Збереження авторів у базі даних
for author_data in authors_data:
    author = Author(**author_data)
    author.save()

# Збереження цитат у базі даних
for quote_data in quotes_data:
    author_name = quote_data["author"]
    author = Author.objects(fullname=author_name).first()
    if author:
        quote_data["author"] = author
        quote = Quote(**quote_data)
        quote.save()
