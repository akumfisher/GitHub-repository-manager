import json
import os

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
    url = input("Repo URL: ")
    repos.append(url)
    save(repos)
    print("Saved.")


def list_repos():
    repos = load()
    for i, repo in enumerate(repos, 1):
        print(f"{i}. {repo}")


def clone_repo():
    repos = load()
    list_repos()
    n = int(input("Repo number: "))
    os.system(f"git clone {repos[n-1]}")


def update_repo():
    folder = input("Folder name: ")
    os.system(f"cd {folder} && git pull")
    
    
def delete_repo():
    repos = load()
    list_repos()

    while True:
        try:
            n = int(input("Repo number: "))
            repo_range = range(1, len(repos)+1)

            if n in repo_range:
                repos.pop(n-1)
                save(repos)
                print("Repo deleted.")
                break
            else:
                print("Invalid option")

        except:
            print("Enter a number.")