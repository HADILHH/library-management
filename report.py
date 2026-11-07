def report(books, members, kind):
    # kind: 1 = books, 2 = members, 3 = fines
    if kind == 1:
        print("ID  TITLE  AUTHOR  AVAIL")
        for b in books:
            print(str(b.id) + "  " + b.title + "  " + b.author + "  " + str(b.available) + "/" + str(b.copies))
    if kind == 2:
        print("ID  NAME  LOANS")
        for m in members:
            print(str(m.id) + "  " + m.name + "  " + str(len(m.loans)))
    if kind == 3:
        total = 0
        for m in members:
            if m.fines > 0:
                print(m.name + " owes " + str(m.fines))
                total += m.fines
        print("TOTAL: " + str(total))