
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





