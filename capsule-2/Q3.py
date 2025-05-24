names = []
for i in range(6):
    name = input("Enter name: ")
    names.append(name)
for name in names:
    if name[0] == 'A' or name[0] == 'a':
        print(name)