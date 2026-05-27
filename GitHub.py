import json
import os
from colorama import Fore, Style

FILE = "repos.json"


def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f)


def add_repo():
    repos = load()
    url = input(Fore.BLUE + "Repository URL: ")
    repos.append(url)
    save(repos)
    print(Fore.GREEN + "Repository has been saved." + Style.RESET_ALL)


def list_repos():
    repos = load()
    for i, repo in enumerate(repos, 1):
        print(f"{i}. {repo}")


def clone_repo():
    repos = load()
    list_repos()
    n = int(input(Fore.BLUE + "Repository number: "))
    os.system(f"git clone {repos[n-1]}")


def update_repo():
    folder = input("Folder name: " + Style.RESET_ALL)
    os.system(f"cd {folder} && git pull")
    
    
def delete_repo():
    repos = load()
    list_repos()

    while True:
        try:
            n = int(input(Fore.BLUE + "Repository number: "))
            repo_range = range(1, len(repos)+1)

            if n in repo_range:
                repos.pop(n-1)
                save(repos)
                print(Fore.GREEN + "Repositoty successfully deleted.")
                break
            else:
                print(Fore.YELLOW + "Please enter a valid repository option!")

        except:
            print(Fore.YELLOW + "Enter a number please!")