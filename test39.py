import os
import sys
import subprocess

def update_script():
    """
    Pull the latest changes from the GitHub repository
    and restart the script.
    """
    try:
        # Run `git pull` to fetch updates
        subprocess.run(['git', 'pull'], check=True)
        print("Successfully updated the script. Restarting...")

        # Restart the script with updated code
        os.execv(sys.executable, ['python'] + sys.argv)

    except subprocess.CalledProcessError as e:
        print(f"Error while updating: {e}")
        sys.exit(1)  # Exit if git pull fails


# Usage: check if the script should update
if __name__ == '__main__':
    # Call the update function to update the script
    update_script()

    # Your main script logic here
    print("Running the updated script...")
