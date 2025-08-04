def contacts(queries):
    contact = []
    for i in queries:
        first,second = i
        if first == 'add':
            contact.append(second)
        elif first == 'find':
            count = sum(1 for j in contact if j.startswith(second))
            print(count)
    return contact