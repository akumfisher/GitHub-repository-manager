import json
import os
from colorama import Fore, Style
import requests

FILE = "repos.json"


def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)
        
def url_checker(url):
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=5,
            allow_redirects=True
        )

        return response.status_code == 200

    except requests.RequestException:
        return False


def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f)


def add_repo():
    repos = load()
    url = input(Fore.BLUE + "Repository URL: ")
    if url_checker(url):
        repos.append(url)
        save(repos)
        print(Fore.GREEN + "Repository has been saved." + Style.RESET_ALL)
    else:
        print("Invalid repository link")
      


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
    
    if repos == []:
        print(Fore.YELLOW + "No repository was found!" + Style.RESET_ALL)
        not_empty = False
    else:
        not_empty = True

    while not_empty:
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
