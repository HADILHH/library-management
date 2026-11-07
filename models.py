class Book:
    def __init__(self, id, title, author, year, copies):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies
        self.available = copies

class Member:
    def __init__(self, id, name, email, type):
        self.id = id
        self.name = name
        self.email = email
        self.type = type   # 1 = student, 2 = teacher, 3 = external
        self.loans = []
        self.fines = 0