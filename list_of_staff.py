def list_staff(staff):
    print("Inventory: ")
    values = 0
    for name in staff:
        print(str(staff[name]) + ' ' + name)
        values += staff[name]

    print('Total number of items is: ' + str(values))

staff = {
    'rope': 1, 'torch': 6, 'gold coin': 2, 'arrow': 42
}

list_staff(staff)