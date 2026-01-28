import requests
from pathlib import Path

ICONS = [
    "check-circle", "x-circle", "square", "check-square", 
    "clipboard", "mail", "smartphone", "package", "printer", 
    "file-text", "bar-chart", "trending-up", "trending-down", 
    "calendar", "map-pin", "paperclip", "crown", "user", 
    "users", "wrench", "factory", "lock", "lock-open", 
    "key", "truck", "car", "circle", "alert-triangle", 
    "info", "lightbulb", "play", "pause", "chevron-down", 
    "chevron-up", "chevron-right", "chevron-left", "clock", 
    "timer", "building-2", "building", "settings", "hammer"
]

ICON_DIR = Path("export/assets/icons")
ICON_DIR.mkdir(parents=True, exist_ok=True)

def download_icons():
    print("Downloading Lucide icons...")
    for icon in ICONS:
        url = f"https://unpkg.com/lucide-static@latest/icons/{icon}.svg"
        response = requests.get(url)
        if response.status_code == 200:
            file_path = ICON_DIR / f"{icon}.svg"
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"✓ Downloaded {icon}.svg")
        else:
            print(f"✗ Failed to download {icon}.svg")

if __name__ == "__main__":
    download_icons()
