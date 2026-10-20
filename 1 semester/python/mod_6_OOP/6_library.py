class Book:
    """Класс для представления книги с приватными атрибутами."""
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        """Возвращает название книги."""
        return self.__title

    def get_author(self):
        """Возвращает автора книги."""
        return self.__author

    def __str__(self):
        """Возвращает строковое представление книги."""
        return f'"{self.__title}" автора {self.__author}'

class Library:
    """Класс для управления коллекцией книг."""
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Добавляет книгу в библиотеку."""
        if not isinstance(book, Book):
            raise TypeError("В библиотеку можно добавлять только объекты класса Book.")
        self._books.append(book)

    def find_book_by_title(self, title):
        """Ищет книгу по названию."""
        for book in self._books:
            if book.get_title() == title:
                return book
        return None

    def __len__(self):
        """Возвращает количество книг в библиотеке."""
        return len(self._books)