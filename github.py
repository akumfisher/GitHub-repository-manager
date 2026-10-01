import json
import os
from colorama import Fore, Style
import requests
from urllib.parse import urlparse, urlsplit

FILE = "repos.json"

# Success message display colour
def success(message):
    print(Fore.GREEN + message + Style.RESET_ALL)

# Error message display colour
def error(message):
    print(Fore.RED + message + Style.RESET_ALL)

# Warning message display colour
def warning(message):
    print(Fore.YELLOW + message + Style.RESET_ALL)

# Load repositories from repos.json
def load():
    
    if not os.path.exists(FILE):
        return []
        
    with open(FILE, "r") as f:
        return json.load(f)
        

# Using the domain to verify whether the URL is valid Github URL   
def parser(url):

    ## Extracting the domain from the parsed URL
    parsed_url = urlparse(url)
    
    if parsed_url.netloc == "github.com":
        return True
    
    else:
        warning("[!] Github URLs only")
        return False
        
# This will help in cleanly naming the repositories with their names only
def name_split(repo):
    split_url = urlsplit(repo)
    path_segment = split_url.path.strip('/').split('/') # Takes out the slashes so we get a tuple with the words separated by them
    return path_segment[-1]
    
# Using boolean to get the state of repos.json (empty or not)    
def non_empty_repo():
    
    repos = load()
    return bool(repos)

# Checking if we can actually get a response from a chosen URL
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

# Save any changes in repos.json
def save(data):
    
    with open(FILE, "w") as f:
        json.dump(data, f)

# Add repository URL to repos.json
def add_repo():

    while True:
        repos = load()
        url = input(Fore.BLUE + "Repository URL: " + Style.RESET_ALL)
        
        if url not in repos and url_checker(url): # If url is a functioning Github URL yet to be saved
            repos.append(url)
            save(repos)
            success("[✓] Repository has been saved.")
            break
        
        elif url in repos: # If the repository url has already been saved
            warning("[!]Repository already exists")
    
        else:
            error("Invalid repository link")

# Display the names of repositories that were previously saved
def list_repos():
    
    if non_empty_repo():
        repos = load()
        
        for i, repo in enumerate(repos, 1):
            repo_name = name_split(repo)
            print(f"{i}. {repo_name}")
            
    else:
        warning("[!]No repository was found!")

# Clone any repository previously saved in repos.json
def clone_repo():
    
    repos = load()
    while True:
        try:
            if non_empty_repo():
                list_repos()
                n = int(input(Fore.BLUE + "Repository number: " + Style.RESET_ALL))
                os.system(f"git clone {repos[n-1]}")
                break
            else:
                warning("[!]No repository was found!")
        except ValueError:
                    warning("[!] Enter a number please!")

# Update previously saved repository in repos.json
def update_repo():

    while True:
        try:
            if non_empty_repo():
                folder = input(Fore.BLUE + "Folder name: " + Style.RESET_ALL)
                os.system(f"cd {folder} && git pull")
                success("[✓]Repository has been updated successfully.")
                break                
            else:
                warning("[!]No repository was found!")
                break
        except ValueError:
            warning("[!] Enter a number please!")

# Delete repository from repos.json
def delete_repo():
    
    repos = load()
    
    if non_empty_repo():
        list_repos()
        not_empty = True
    else:
        not_empty = False
    
    while not_empty:
        try:
            n = int(input(Fore.BLUE + "Repository number: " + Style.RESET_ALL))
            
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
