from GitHub import *

def menu():
    while True:
        print("\n=== GitHub Repo Manager ===")
        print("1. Add Repo")
        print("2. List Repos")
        print("3. Clone Repo")
        print("4. Update Repo")
        print("5. Delete Repo")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_repo()
        elif choice == "2":
            list_repos()
        elif choice == "3":
            clone_repo()
        elif choice == "4":
            update_repo()
        elif choice == "5":
            delete_repo()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

menu()