import json
import os
from colorama import Fore, Style
import requests
from urllib.parse import urlparse

FILE = "repos.json"


def load():
    
    if not os.path.exists(FILE):
        return []
        
    with open(FILE, "r") as f:
        return json.load(f)
        
#not_empty = False

def parser(url):
    
    parsed_url = urlparse(url)
    
    if parsed_url.netloc == "github.com":
        return True
    
    else:
        print(Fore.YELLOW + "[!] Github URLs only" + Style.RESET_ALL)
        return False
        
        
def non_empty_repo():
    
    repos = load()
    return bool(repos)
        
def url_checker(url):
    
    headers = {"User-Agent": "Mozilla/5.0"}
    
    if parser(urla):
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
    
    if url not in repos and url_checker(url):
        repos.append(url)
        save(repos)
        print(Fore.GREEN + "[✓] Repository has been saved." + Style.RESET_ALL)
    
    elif url in repos:
        print(Fore.YELLOW + "[!]Repository already exists")
 
    else:
        print(Fore.RED + "Invalid repository link" + Style.RESET_ALL)
      


def list_repos():
    
    if non_empty_repo():
        repos = load()
        for i, repo in enumerate(repos, 1):
            print(f"{i}. {repo}")
            
    else:
        print(Fore.YELLOW + "[!]No repository was found!")


def clone_repo():
    
    repos = load()
   
    if non_empty_repo():
        list_repos()
        n = int(input(Fore.BLUE + "Repository number: "))
        os.system(f"git clone {repos[n-1]}")
    else:
        print(Fore.YELLOW + "[!]No repository was found!" + Style.RESET_ALL)


def update_repo():
    
    if non_empty_repo():
        folder = input(Fore.BLUE + "Folder name: " + Style.RESET_ALL)
        os.system(f"cd {folder} && git pull")
        
    else:
        print(Fore.YELLOW + "[!]No repository was found!" + Style.RESET_ALL)
    
    
def delete_repo():
    
    repos = load()
    
    if non_empty_repo():
        list_repos()
        not_empty = True
    else:
        not_empty = False
    
    while not_empty:
        try:
            n = int(input(Fore.BLUE + "Repository number: "))
            
            repo_range = range(1, len(repos)+1)

            if n in repo_range:
                repos.pop(n-1)
                save(repos)
                print(Fore.GREEN + "[✓] Repository successfully deleted.")
                break
          
            else:
                print(Fore.YELLOW + "[!] Please enter a valid repository option!")

        except ValueError:
            print(Fore.YELLOW + "[!] Enter a number please!" + Style.RESET_ALL)
