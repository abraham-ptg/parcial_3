"""Información a ingresar."""


def main_input()-> dict:
    """Crea diccionario con información a utilizar."""
    matriculas = [2225457, 2225388, 2153884]
    return {
            "nombres":["Julio Abraham Puente Guerrero", "Sebastián Aligheri Ramírez",
                        "Alberto Jessier Lucio Sital"],
            "suma":sum(matriculas),
    }
