import requests
import json

def view(
    file_path: str,
    filename: str = None,
    repo: str = "Eletroman179/test_update",
    branch: str = "main"):
    url = f"https://raw.githubusercontent.com/{repo}/{branch}/{file_path}"
    
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch file: {response.status_code}")
        return None

def download(
    file_path: str,
    filename: str = None,
    repo: str = "Eletroman179/test_update",
    branch: str = "main"
):
    raw_url = f"https://raw.githubusercontent.com/{repo}/{branch}/{file_path}"
    if filename is None:
        filename = file_path.split("/")[-1]

    response = requests.get(raw_url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded '{filename}' from '{repo}'")
    else:
        print(f"Failed to download '{file_path}' from '{repo}': {response.status_code}")

json_text = view("config.json")
if json_text:
    git_data = json.loads(json_text)

with open("config.json") as file:
    data = json.load(file)

if git_data["ver"] != data["ver"]:
    print("updating script")
    download("main.py")     # updates main script
    download("config.json") # updates json file
