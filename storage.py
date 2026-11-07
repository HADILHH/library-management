import json
from models import Book, Member
def load(f):
    file = open(f, "r")
    data = json.load(file)
    file.close()
    return data

def save(f, data):
    file = open(f, "w")
    json.dump(data, file)
    file.close()

def load_books(path):
    d = load(path)
    books = []
    for x in d:
        b = Book(x["id"], x["title"], x["author"], x["year"], x["copies"])
        b.available = x["available"]
        books.append(b)
    return books

def save_books(path, books):
    d = []
    for b in books:
        d.append({"id": b.id, "title": b.title, "author": b.author,
                  "year": b.year, "copies": b.copies, "available": b.available})
    save(path, d)

def load_members(path):
    d = load(path)
    members = []
    for x in d:
        m = Member(x["id"], x["name"], x["email"], x["type"])
        m.loans = x["loans"]
        m.fines = x["fines"]
        members.append(m)
    return members

def save_members(path, members):
    d = []
    for m in members:
        d.append({"id": m.id, "name": m.name, "email": m.email,
                  "type": m.type, "loans": m.loans, "fines": m.fines})
    save(path, d)