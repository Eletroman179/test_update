import requests
import subprocess
import os

def check_for_updates():
    try:
        repo_owner = "Eletroman179"  # Replace with your GitHub username or organization
        repo_name = "test_update"    # Replace with your repository name
        
        # Fetch the latest release information from GitHub
        api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
        response = requests.get(api_url)
        response.raise_for_status()
        latest_release = response.json()

        # Get the tag name of the latest release
        latest_version = latest_release['tag_name']

        # Check if a local version file exists to compare with
        version_file = "version.txt"  # Assuming a file where you store the current version
        if os.path.exists(version_file):
            with open(version_file, 'r') as f:
                current_version = f.read().strip()
        else:
            current_version = ""

        # Compare versions and decide whether to update
        if current_version != latest_version:
            print(f"New version available: {latest_version}")
            return True
        else:
            print("Tool is up to date.")
            return False

    except Exception as e:
        print(f"Failed to check for updates: {e}")
        return False

def update_tool():
    try:
        tool_dir = "C:/Users/James/..test/update_tool"  # Adjust this to your tool's directory
        os.chdir(tool_dir)

        # Fetch updates from the remote repository
        subprocess.run(["git", "pull", "origin", "main", "--allow-unrelated-histories"], check=True)

        # Optionally, update the version file with the latest version
        with open("version.txt", 'w') as f:
            f.write(latest_version)  # Assuming 'latest_version' is defined or retrieved

        print("Tool updated successfully.")

    except Exception as e:
        print(f"Error updating tool: {e}")

# Main execution
if __name__ == "__main__":
    if check_for_updates():
        update_tool()
