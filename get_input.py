def alumno():
    return (input("Ingresa el nombre del alumno: "), int(input("Ingresa matricula del alumno: ")))

def suma_mat(datos_integrantes):
    suma = 0
    for alumno in datos_integrantes:
        suma += alumno[1]
    return suma

def main_input()-> dict:
    datos_integrantes = []
    while True:
        datos_integrantes.append(alumno())
        if input("Desea agregar otro alumno [n para salir]: ") == "n":
            datos = {
                "nombres":[nombre[0] for nombre in datos_integrantes],
                "suma":suma_mat(datos_integrantes)
            }
            return datos
