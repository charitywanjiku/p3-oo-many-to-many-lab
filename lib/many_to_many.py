class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.__class__.all_books.append(self)


class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.__class__.all_authors.append(self)

    def contracts(self):
        author_contracts = []
        for contract in Contract.all_contracts:
            if contract.author == self:
                author_contracts.append(contract)
        return author_contracts

    def books(self):
        author_books = []
        for contract in self.contracts():
            author_books.append(contract.book)
        return author_books

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book object.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author object.")
        if not isinstance(book, Book):
            raise Exception("Invalid book object.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        contracts_on_date = []
        for contract in cls.all_contracts:
            if contract.date == date:
                contracts_on_date.append(contract)
        return contracts_on_date


# Testing the implementation
if __name__ == "__main__":
    # Create authors
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

    # Create books
    book1 = Book("Python Programming")
    book2 = Book("Machine Learning Basics")

    # Sign contracts
    contract1 = author1.sign_contract(book1, "2023-01-01", 10)
    contract2 = author2.sign_contract(book2, "2023-02-01", 15)

    # Test methods
    print("Author 1's contracts:")
    for contract in author1.contracts():
        print(contract.book.title)

    print("Author 1's books:")
    for book in author1.books():
        print(book.title)

    print("Total royalties for Author 1:", author1.total_royalties())

    print("Contracts signed on 2023-01-01:")
    contracts_on_date = Contract.contracts_by_date("2023-01-01")
    for contract in contracts_on_date:
        print(contract.book.title)
