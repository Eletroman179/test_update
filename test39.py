import subprocess
import os

def update_tool():
    try:
        # Navigate to the directory where your tool is located
        tool_dir = "C:/Users/James/..test/update_tool"  # Use the correct tool path
        os.chdir(tool_dir)

        # Set up the upstream branch if not already set
        subprocess.run(["git", "branch", "--set-upstream-to=origin/main"], check=True)

        # Run git pull command to fetch the latest changes
        result = subprocess.run(["git", "pull", "origin", "main", "--allow-unrelated-histories"], capture_output=True, text=True)
        
        # Print the git pull command output
        print(result.stdout)
        
        # Check if there were any errors
        if result.returncode != 0:
            print(f"Error updating tool: {result.stderr.strip()}")

        else:
            print("Tool updated successfully.")

    except Exception as e:
        print(f"Error updating tool: {e}")

update_tool()
print("done")
