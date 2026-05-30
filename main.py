from github import *
from colorama import Fore, Back, Style, init

init()

def menu():
    while True:
        print(Fore.LIGHTBLUE_EX + "\n=== GitHub Repo Manager ===")
        print(Fore.MAGENTA + "[1] Add Repo")
        print("[2] List Repos")
        print("[3] Clone Repo")
        print("[4] Update Repo")
        print("[5] Delete Repo")
        print("[6] Exit" )
        choice = input(Fore.BLUE + "Choose: " + Style.RESET_ALL)

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
            print(Fore.RED + "Invalid choice.")

menu()
