from mongoengine import connect
from mongoengine.queryset.visitor import Q

from models import Author, Quote

connect(
    "book_db",
    host="mongodb+srv://harley029:8lyrMibko@cluster0.b6lozo9.mongodb.net/?retryWrites=true&w=majority",
)


def search_quotes():
    while True:
        command = input(
            "Enter command (tag:<tag>, name:<author_name>, tags:<tag1>,<tag2>, exit): "
        ).strip()

        if command.startswith("tag:"):
            tag_name = command.split(":")[1].strip()
            if len(tag_name) <= 2:  # Перевірка на скорочений тег
                quotes = Quote.objects(tags__istartswith=tag_name).all()
            else:
                quotes = Quote.objects(tags=tag_name).all()
            print_quotes(quotes)
        elif command.startswith("name:"):
            author_name = command.split(":")[1].strip()
            if len(author_name) <= 2:  # Перевірка на скорочене ім'я
                authors = Author.objects(fullname__istartswith=author_name).all()
            else:
                authors = Author.objects(fullname__icontains=author_name).all()
            if authors:
                quotes = Quote.objects(author__in=authors).all()
                print_quotes(quotes)
            else:
                print("Author not found.")
        elif command.startswith("tags:"):
            tags = command.split(":")[1].strip().split(",")
            # Формуємо складний запит за тегами
            query = Q()
            for tag in tags:
                query |= Q(tags=tag.strip())
            quotes = Quote.objects(query).all()
            print_quotes(quotes)
        elif command == "exit":
            print("Exiting script...")
            break
        else:
            print("Invalid command. Please try again.")


def print_quotes(quotes):
    for quote in quotes:
        print(f"{quote.author.fullname}: {quote.quote}")


if __name__ == "__main__":
    search_quotes()
