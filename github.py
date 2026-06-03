import json
import os
from colorama import Fore, Style
import requests
from urllib.parse import urlparse

FILE = "repos.json"

def success(message):
    print(Fore.GREEN + message + Style.RESET_ALL)

def error(message):
    print(Fore.RED + message + Style.RESET_ALL)

def warning(message):
    print(Fore.YELLOW + message + Style.RESET_ALL)


def load():
    
    if not os.path.exists(FILE):
        return []
        
    with open(FILE, "r") as f:
        return json.load(f)
        
        
def parser(url):
    
    parsed_url = urlparse(url)
    
    if parsed_url.netloc == "github.com":
        return True
    
    else:
        warnind("[!] Github URLs only")
        return False
        
        
def non_empty_repo():
    
    repos = load()
    return bool(repos)
        
def url_checker(url):
    
    headers = {"User-Agent": "Mozilla/5.0"}
    
    if parser(url):
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
        success("[✓] Repository has been saved.")
    
    elif url in repos:
        warning("[!]Repository already exists")
 
    else:
        error("Invalid repository link")


def list_repos():
    
    if non_empty_repo():
        repos = load()
        for i, repo in enumerate(repos, 1):
            print(f"{i}. {repo}")
            
    else:
        warning("[!]No repository was found!")


def clone_repo():
    
    repos = load()
   
    if non_empty_repo():
        list_repos()
        n = int(input(Fore.BLUE + "Repository number: "))
        os.system(f"git clone {repos[n-1]}")
    else:
        warning("[!]No repository was found!")



def update_repo():
    
    if non_empty_repo():
        folder = input(Fore.BLUE + "Folder name: " + Style.RESET_ALL)
        os.system(f"cd {folder} && git pull")
        
    else:
        warning("[!]No repository was found!")
    
    
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
                success("[✓] Repository successfully deleted.")
                break
          
            else:
                warning("[!] Please enter a valid repository option!")

        except ValueError:
            warning("[!] Enter a number please!")
