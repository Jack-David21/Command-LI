from auth import register_user, login_user 

def main():
    while True:
        choice = input(
            "\n1. Register\n2. Login\n3. Exit\nChoose an option: "
        )

        if choice == "1":
            register_user()

        elif choice == "2":
            success = login_user()
            if success:
                print("You are now logged in.")

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()