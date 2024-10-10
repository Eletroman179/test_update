import subprocess
import os

def update_tool():
    try:
        # Navigate to the directory where your tool is located
        tool_dir = "C:/Users/James/..test"  # Change this to your actual tool path
        os.chdir(tool_dir)

        # Check if the remote "origin" exists
        result = subprocess.run(["git", "remote"], capture_output=True, text=True)
        
        # If "origin" is not set, add the remote URL
        if "origin" not in result.stdout:
            # Replace this URL with the actual repository URL
            remote_url = "https://github.com/Eletroman179/test_update.git"
            subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
            print(f"Added remote origin: {remote_url}")

        # Check if there is at least one commit
        try:
            subprocess.run(["git", "log"], check=True, capture_output=True)
        except subprocess.CalledProcessError:
            # If there are no commits, create an initial commit
            print("No commits found. Creating an initial commit.")
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)

        # Set upstream branch to 'origin/master' if not already set
        subprocess.run(["git", "branch", "--set-upstream-to=origin/master"], check=True)

        # Run git pull command to fetch the latest changes
        subprocess.run(["git", "pull", "origin", "master"], check=True)
        print("Tool updated successfully.")

    except Exception as e:
        print(f"Error updating tool: {e}")

update_tool()
