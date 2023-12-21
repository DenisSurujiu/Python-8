
def add(file_path):
    name = input(":")
    surname = input(":")
    Email = input(":")
    Phone = input(":")

    with open(file_path, "a") as file:
        file.write(f"{surname}, {name}, {Email}, {Phone}n")



