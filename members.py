from models import Member

def add_member(members, name, email, type):
    # check email
    if "@" not in email:
        print("invalid email")
        return None
    for m in members:
        if m.email == email:
            print("email already used")
            return None
    new_id = len(members) + 1
    m = Member(new_id, name, email, type)
    members.append(m)
    return m

def find_member(members, id):
    for m in members:
        if m.id == id:
            return m
    return None

def max_loans(m):
    if m.type == 1:
        return 3
    elif m.type == 2:
        return 10
    else:
        return 1

def pay_fine(m, amount):
    if amount > m.fines:
        amount = m.fines
    m.fines = m.fines - amount
    return amount