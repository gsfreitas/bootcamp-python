from typing import Dict, Any

books: Dict[str, Any] = {
    "book_1": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925
    },
    "book_2": {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    }
}

print(f"Books: {books['book_2']}")