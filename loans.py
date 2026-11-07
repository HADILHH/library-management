import datetime
from members import max_loans

def borrow(books, member, book_id, days, notify, log, force):
    # find book
    b = None
    for x in books:
        if x.id == book_id:
            b = x
    if b == None:
        if log:
            print("book not found")
        return False
    if b.available > 0:
        if len(member.loans) < max_loans(member):
            if member.fines < 50 or force == True:
                b.available -= 1
                today = datetime.date.today()
                due = today + datetime.timedelta(days=days)
                member.loans.append({"book": book_id, "due": str(due)})
                if notify:
                    print("Mail sent to " + member.email + ": due " + str(due))
                if log:
                    print(member.name + " borrowed " + b.title)
                return True
            else:
                if log:
                    print("fines too high")
                return False
        else:
            if log:
                print("too many loans")
            return False
    else:
        if log:
            print("not available")
        return False

def give_back(books, member, book_id):
    for l in member.loans:
        if l["book"] == book_id:
            member.loans.remove(l)
            for b in books:
                if b.id == book_id:
                    b.available += 1
            due = datetime.datetime.strptime(l["due"], "%Y-%m-%d").date()
            late = (datetime.date.today() - due).days
            if late > 0:
                if member.type == 1:
                    member.fines += late * 2
                elif member.type == 2:
                    member.fines += late * 1
                else:
                    member.fines += late * 5
            return True
    return False