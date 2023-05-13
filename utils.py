import tkinter.messagebox as messagebox
import urllib.request
import json

VERSION = "1.0.0"
GITHUB_RELEASES_API = "https://api.github.com/repos/your-username/your-repo/releases/latest"

def get_version():
    return VERSION

def check_for_updates():
    try:
        with urllib.request.urlopen(GITHUB_RELEASES_API) as url:
            data = json.loads(url.read().decode())
            latest_version = data["tag_name"]
            if latest_version != VERSION:
                message = f"A new version ({latest_version}) is available! Please update the program."
                messagebox.showinfo("Update Available", message)
    except Exception as e:
        print("Error checking for updates:", str(e))
