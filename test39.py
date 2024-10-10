import os
import requests
import zipfile
import shutil
import sys

# 1. Check for updates
def check_for_update(current_version):
    repo = "username/repo"  # Replace with your GitHub repo
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        latest_release = response.json()

        latest_version = latest_release['tag_name']

        if current_version != latest_version:
            print(f"Update available: {latest_version}")
            return True, latest_release['zipball_url']  # Or tarball_url for tar.gz
        else:
            print("No update available.")
            return False, None
    except requests.RequestException as e:
        print(f"Failed to check for updates: {e}")
        return False, None

# 2. Download the update
def download_update(url, save_path):
    try:
        print("Downloading the update...")
        response = requests.get(url)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            file.write(response.content)

        # Unzip the update
        with zipfile.ZipFile(save_path, 'r') as zip_ref:
            zip_ref.extractall("update_folder")  # Replace with the desired extraction folder

        print("Update downloaded and extracted.")
        return True
    except requests.RequestException as e:
        print(f"Failed to download the update: {e}")
        return False

# 3. Install the update
def install_update():
    try:
        # Replace current files with those from the update
        update_folder = "update_folder"
        current_folder = os.getcwd()

        for item in os.listdir(update_folder):
            source = os.path.join(update_folder, item)
            destination = os.path.join(current_folder, item)
            if os.path.isdir(source):
                shutil.copytree(source, destination, dirs_exist_ok=True)
            else:
                shutil.copy2(source, destination)

        print("Update installed successfully.")
        return True
    except Exception as e:
        print(f"Failed to install update: {e}")
        return False

# 4. Restart the application
def restart_application():
    try:
        print("Restarting application...")
        os.execv(sys.executable, ['python'] + sys.argv)
    except Exception as e:
        print(f"Failed to restart the application: {e}")

# Main function to manage update process
def update_application(current_version):
    update_needed, download_url = check_for_update(current_version)
    
    if update_needed:
        # Path to save the downloaded zip file
        download_path = "latest_update.zip"

        if download_update(download_url, download_path):
            if install_update():
                restart_application()

# Example usage
if __name__ == "__main__":
    current_version = "v1.0.0"  # Replace with the current version of your application
    update_application(current_version)
