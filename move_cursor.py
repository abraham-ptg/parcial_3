"""Movimientos del cursor en la pantalla."""
import time

import pyautogui


def move_cursor(data):
    """Provee movimiento al cursor.

    Mueve el cursos a la posición deseada en base a la resolción de la pantalla
    e ingresa información al formulario.
    """
    x_percent = 50
    y_percent = 40


    screen_width, screen_height = pyautogui.size()
    x = int(screen_width * (x_percent / 100))
    y = int(screen_height * (y_percent / 100))

    pyautogui.click(x, y)
    time.sleep(0.5)
    pyautogui.press("enter")
    pyautogui.press("tab")

    for nombre in data["nombres"]:
        pyautogui.typewrite(nombre)
        pyautogui.press("enter")

    pyautogui.press("tab")
    pyautogui.typewrite(str(data["suma"]))
    pyautogui.press("tab")
    pyautogui.press("space")

    pyautogui.press("tab")
    pyautogui.press("enter")
