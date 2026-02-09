from auth import register_user, login_user 
from to_dos import add_todo, list_todos, toggle_todo, delete_todo, update_todo

current_user = None

def main():
    global current_user

    while True:
        if current_user is None:
            choice = input(
            "\n1. Register\n2. Login\n3. Exit\nChoose an option: "
        )

            if choice == "1":
                register_user()

            elif choice == "2":
                user = login_user()
                if user is not None:
                    current_user = user
                    print("You are now logged in.")

            elif choice == "3":
                print("Thank you!")
                break

            else:
                print("Invalid option.")

        else:
            print(f"\nLogged in as {current_user}\n")
            print("1. Add task\n" \
                  "2. View tasks\n" \
                  "3. Mark task as complete / incomplete\n" \
                  "4. Edit task\n" \
                  "5. Delete task\n" \
                  "6. Logout\n" \
                  "7. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                title = input("Enter the title of the task: ")
                add_todo(current_user, title)

            elif choice == "2":
                list_todos(current_user)
                input("\nPress Enter to continue...")

            elif choice == "3":
                try:
                    todo_id = int(input("Enter the task ID: "))
                    toggle_todo(current_user, todo_id)
                except ValueError:
                    print("Invalid input. Please enter a valid integer ID.")


            elif choice == "4":
                try:
                    todo_id = int(input("Enter the task ID: "))
                    new_title = input("Enter the new title: ")
                    update_todo(current_user, todo_id, new_title)
                except ValueError:
                    print("Invalid input. Please enter a valid integer ID.")

            elif choice == "5":
                try:
                    todo_id = int(input("Enter the task ID: "))
                    delete_todo(current_user, todo_id)
                except ValueError:
                    print("Invalid input. Please enter a valid integer ID.")

            elif choice == "6":
                current_user = None
                print("You have been logged out.")

            elif choice == "7":
                print("Thank you!")
                break

            else:
                print("Invalid option.")

if __name__ == "__main__":
    main()
