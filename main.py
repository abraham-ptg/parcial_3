"""Orquesta la lógica para llenar formulario."""
import logging
import time
from subprocess import CalledProcessError, TimeoutExpired

from get_input import main_input
from invoke_msedge import invoke_msedge
from move_cursor import move_cursor
from new_screenshot import new_screenshot


def main():
    """Abre msedge, mueve el cursor y llena el formulario."""
    logging.basicConfig(filename="run.log", level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s", encoding="utf-8")
    logger = logging.getLogger(__name__)
    logger.info("Inicio del examen")

    data = main_input()

    if not data:
        return

    try:
        new_screenshot("before")
    except RuntimeError:
        return

    try:
        invoke_msedge()

    except (
        FileNotFoundError,
          PermissionError,
          CalledProcessError,
          TimeoutExpired,
          OSError,
          )  as e:
        msg = f"Unable to run msedge: {e}"
        logger.exception(msg)

    time.sleep(2)

    try:
        move_cursor(data)
        new_screenshot("during")
    except (OSError, ImportError) as e:
        msg = f"Failed to execute cursor movement: {e}"
        logger.exception(msg)
    except RuntimeError:
        return

    time.sleep(5)

    try:
        new_screenshot("after")
    except RuntimeError:
        return

    logger.info("Fin del examen")

if __name__ == "__main__":
    main()
