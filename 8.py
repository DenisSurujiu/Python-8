
def add(file_path):
    name = input("Введите имя:")
    surname = input("Введите фамилию:")
    Email = input("Введите почту:")
    Phone = input("Введите номер телефона:")

    with open(file_path, "a") as file:
        file.write(f"{surname}, {name}, {Email}, {Phone}n")

def load(file_path):
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())

def search(file_path):
    search = input("Введите имя фамилию или почту для поиска контакта")

    with open(file_path, "r") as file:
        for line in file:
            if search.lower() in line.lower():
                print(line.strip())

def update(file_path):
    name = input("Введите имя контакта, которую нужна изменить: ")
    surname = input("Введите фамилию контакта, которую нужна изменить:")

    new_name = input("Введите новое имя:")
    new_surname = input("Введите новою фамилию:")
    new_Email = input("Введите новую почту:")
    new_Phone = input("Введите новый контакт:")

    with open(file_path, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if name.lower() in line.lower() and surname.lower() in line.lower():
                file.write(f"{new_name}, {new_surname}, {new_Email}, {new_Phone}n")
            else:
                file.write(line)
        file.truncate()

def delete(file_path):
    name = input("Введите имя контакта, которую нужна удалить: ")
    surname = input("Введите фамилию контакта, которую нужна удалить:")

    with open(file_path, "r+") as file:
        lines = file.readlines()
        file.seek(0)
    for line in lines:
        if name.lower() in line.lower() and surname.lower() in line.lower():
            file.write(line)
        file.truncate()

def imports(file_path):
    imports_file_path = input(":")

    with open(imports_file_path, "r") as imports_file:
       with open(file_path, "a") as file:
        for line in imports_file:
            file.write(line)
            
        





