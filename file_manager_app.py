from file import File

def display_menu():
    print("==========================")
    print("=    File Manager        =")
    print("==========================")
    print("= [1] Create             =")
    print("= [2] Search             =")
    print("= [3] Update             =")
    print("= [4] Delete             =")
    print("= [5] Exit               =")
    print("==========================")

def process_file(choice, filename="Test.txt"):
    file = File (filename)
    match choice:
        case "1":
            print(f"You enter choice {choice}")
            print(file.create())
            return True
        case "2":
            print(f"You enter choice {choice}")
            print(file.search())
            return True
        case "3":
            print(f"You enter choice {choice}")
            name = input("Name: ")
            username = input("Username: ")
            password = input("Password: ")
            new_row = f"| {name} | {username} | {password} |"
            print(file.update(new_row))
            return True
        case "4":
            print(f"You enter choice {choice}")
            print(file.delete())
            return True
        case "5":
            print(f"You enter choice {choice}")
            return False
        case _:
            print(f"Please enter valid choice")
            return True
                
def main():
    is_working = True

    while is_working:
        display_menu()
        choice = input("Enter your choice: ")
        is_working = process_file(choice)


if __name__ == "__main__":
    main()