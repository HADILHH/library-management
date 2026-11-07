from storage import *
from members import *
from loans import *
from report import report

BOOKS_FILE = "books.json"
MEMBERS_FILE = "members.json"

def main():
    books = load_books(BOOKS_FILE)
    members = load_members(MEMBERS_FILE)
    while True:
        print("1. borrow  2. return  3. add member  4. report  5. pay fine  0. quit")
        c = input("> ")
        if c == "1":
            mid = int(input("member id: "))
            bid = int(input("book id: "))
            m = find_member(members, mid)
            if m is None:
                print("no such member")
            else:
                borrow(books, m, bid, 14, True, True, False)
        elif c == "2":
            mid = int(input("member id: "))
            bid = int(input("book id: "))
            m = find_member(members, mid)
            if m:
                if give_back(books, m, bid):
                    print("returned")
                else:
                    print("error")
        elif c == "3":
            name = input("name: ")
            email = input("email: ")
            t = int(input("type (1/2/3): "))
            add_member(members, name, email, t)
        elif c == "4":
            k = int(input("1 books, 2 members, 3 fines: "))
            report(books, members, k)
        elif c == "5":
            mid = int(input("member id: "))
            amt = float(input("amount: "))
            m = find_member(members, mid)
            if m:
                paid = pay_fine(m, amt)
                print("paid " + str(paid))
        elif c == "0":
            break
    save_books(BOOKS_FILE, books)
    save_members(MEMBERS_FILE, members)

main()