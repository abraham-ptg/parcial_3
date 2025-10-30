"""Module to take screenshots and save them to a specified location."""
import logging
from datetime import datetime, timezone
from pathlib import Path

import pyautogui


def new_screenshot(name):
    """Try to take screenshot with OS tool with a given prefix."""
    logger = logging.getLogger(__name__)
    try:
        out = Path("out")
        out.mkdir(exist_ok=True)
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        path = out / f"{name}_{ts}.png"
        img = pyautogui.screenshot()
        img.save(path)
        msg = f"Screenshot {name} exitosa"
        logger.info(msg)


    except (OSError, ImportError, ValueError) as e:
        msg = f"Imposible tomar screenshot en {name}: {e}"
        logger.exception(msg)
        raise RuntimeError from e

    return path
