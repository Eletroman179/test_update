import requests
import json
import os

def view(file_path: str, repo: str = "Eletroman179/test_update", branch: str = "main"):
    url = f"https://raw.githubusercontent.com/{repo}/{branch}/{file_path}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch file: {response.status_code}")
        return None

def download(file_path: str, filename: str = None, repo: str = "Eletroman179/test_update", branch: str = "main"):
    raw_url = f"https://raw.githubusercontent.com/{repo}/{branch}/{file_path}"
    if filename is None:
        filename = os.path.basename(file_path)

    response = requests.get(raw_url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded '{filename}' from '{repo}'")
    else:
        print(f"Failed to download '{file_path}' from '{repo}': {response.status_code}")

# Step 1: Load local config
try:
    with open("config.json", "r") as file:
        local_data = json.load(file)
except FileNotFoundError:
    print("Local config.json not found, assuming version '0.0.0'")
    local_data = {"ver": "0.0.0"}

# Step 2: Load remote config
remote_json_text = view("config.json")
if remote_json_text:
    try:
        remote_data = json.loads(remote_json_text)

        if remote_data["ver"] != local_data["ver"]:
            print(f"Updating script from version {local_data['ver']} to {remote_data['ver']}")
            download("main.py")
            download("config.json")
        else:
            print("Script is up to date.")
    except json.JSONDecodeError:
        print("Remote config.json is not a valid JSON.")
else:
    print("Could not retrieve remote config.")
