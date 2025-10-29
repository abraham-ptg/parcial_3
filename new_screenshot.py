from datetime import datetime,timezone
from pathlib import Path
import pyautogui

def take_screenshot(name):
    out = Path("out")
    out.mkdir(exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = out / f"{name}_{ts}.png"
    img = pyautogui.screenshot()
    img.save(path)
    return path