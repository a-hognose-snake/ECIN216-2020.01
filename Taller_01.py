import pandas as pd
import pathlib
"""
ADVERTENCIA: LAS REGIONES EMPIEZAN DEL 0
"""
"""
HEADER
"""
print("_______________________________________________________")
print("_______________________________________________________")
print("TALLER 01 - ALGORITMOS Y PROGRAMACIÓN")
print("PROCESAMIENTO DE DATOS DE OBSERVACIÓN ASTRONÓMICA")
print("_______________________________________________________")
print("_______________________________________________________")
print("")
"""
VALIDAR NOMBRE ARCHIVO
"""
exist = True
while exist:
    try:
        datos_cielo = pathlib.Path(input("Nombre del archivo: "))
        if datos_cielo.exists():
            exist = False
        else:
            print("El archivo no existe, intenta nuevamente...")
            print("")
    except:
        pass
"""
USAR PANDAS PARA LEER ARCHIVO
"""
df = pd.read_csv(datos_cielo, header=None)
rp = open("Resultados.txt", "w+")
"""
FECHAS
"""
df['fecha'] = pd.to_datetime(dict(day=df[0], year=df[2], month=df[1]))
"""
REGIONES
"""
df.drop(columns=[0, 1, 2], inplace=True)
regiones = list(df.columns)
regiones.remove('fecha')
"""
VARIABLES PARA RANGE
"""
ancho_data = len(df.index)  # fechas
num_ancho = int(ancho_data)
largo_data = len(regiones)  # regiones
"""
VALIDAR REGIONES
"""
valido2 = True
while valido2:
    try:
        largo_input = int(input("Regiones en el archivo: "))
        if largo_input >= 1:
            valido1 = False
            if largo_input == largo_data:
                valido2 = False
            else:
                valido2 = True
                print("Los datos del archivo no son los mismos, intenta nuevamente...")
                print("")
        else:
            valido2 = True
            print("La cantidad de regiones se expresan en números naturales, intenta nuevamente...")
            print("")
    except ValueError:
        valido2 = True
        print("La cantidad de regiones se expresan en números naturales, intenta nuevamente...")
        print("")
"""
VALIDAR DÍAS
"""
valido1 = True
while valido1:
    try:
        ancho_input = int(input("Días en el archivo: "))
        if ancho_input >= 1:
            valido1 = False
            if ancho_input == ancho_data:
                valido1 = False
            else:
                valido1 = True
                print("Los datos del archivo no son los mismos, intenta nuevamente...")
                print("")
        else:
            valido1 = True
            print("La cantidad de días se expresan en números naturales, intenta nuevamente...")
            print("")
    except ValueError:
        valido1 = True
        print("La cantidad de días se expresan en números naturales, intenta nuevamente...")
        print("")
"""
FENÓMENOS ASTRONÓMICOS
"""
"""
    EXPLOSIÓN DE SUPERNOVA
"""
count_explosion = 0
def detectar_explosion_supernova(series):
    counterES = 0
    conservaLuz = 0
    date_SU = []
    date_ES = []
    for i in range(0, len(series) - 2):
        old_value, value = series[i], series[i + 1]
        if old_value > 70 and value == old_value:
            conservaLuz = conservaLuz + 1
            date_SU.append(df.fecha[i])
            if conservaLuz >= 9 and series[i + 2] == 0:
                counterES = counterES + 1
                date_ES.append(df.fecha[i + 1])
        else:
            conservaLuz = 0
    if date_ES:
        return f"Se detectó 1 supernova el día {date_SU[0]}\n y esta explotó el día {date_ES[-1]}"
"""
    PULSAR
"""
def detectar_pulsar(series):
    pLuzAlta = 0
    for i in range(0, len(series) - 2):
        # old_value, value = series[i], series[i + 1]
        if series[i] > 80 and series[i] == series[i + 1]:
            if series[i + 1] > series[i + 2]:
                pLuzAlta = pLuzAlta + 1
    if pLuzAlta > 1:
        return pLuzAlta
"""
    NUEVO PLANETA
"""
def detectar_nuevo_planeta(series):
    counterNP = 0
    dark = 0
    for i in range(0, len(series) - 2):
        # old_value, value = series[i], series[i+1]
        if series[i] == 0 and series[i + 1] == 0 and series[i + 2] > 0:
            dark = dark + 1
            if dark >= 2:
                counterNP = counterNP + 1
    if counterNP >= 1:
        return True
    return False
"""
    QUAZAR
"""
def detectar_quazar(series):
    counterQ = 0
    date = []
    for i in range(0, len(series) - 1):
        old_value, value = series[i], series[i + 1]
        if 80 > old_value > 70 and value == old_value:
            date.append(df.fecha[i])
            counterQ = counterQ + 1
        else:
            counterQ = 0
            date = []
    if date:
        date = date[0]
    return date
"""
VALIDAR FECHAS
"""
for i in range(1):
    # print(df.fecha)
    for j in range(0, num_ancho - 1):
        # print(df.fecha[j])
        delta = df.fecha[j] - df.fecha[j + 1]
        # print(delta.days)
        if delta.days == -1:
            pass
        else:
            print("El orden de los datos astronómicos no es correcto.")
            print("")
            print("FIN.")
            print("")
            print("-----------------------------------------------------------------")
            print("GRUPO: JOSEFINA, SEBASTIAN Y SAVKA")
            print("-----------------------------------------------------------------\n")
            exit()
"""
RESULTADOS.TXT
"""
rp.write("-----------------------------------------------------------------\n")
rp.write("-----------------------------------------------------------------\n")
rp.write("TALLER 01 - ALGORITMOS Y PROGRAMACIÓN\n")
rp.write("REPORTE DE PROCESAMIENTO DE DATOS DE OBSERVACIÓN ASTRONÓMICA\n")
rp.write("-----------------------------------------------------------------\n")
rp.write("-----------------------------------------------------------------\n")
rp.write("\n")
rp.write("-----------------------------------------------------------------\n")
rp.write(" EXPLOSIONES DE SUPERNOVA\n")
rp.write("-----------------------------------------------------------------\n")
rp.write("\n")
for region in regiones:
    ES = detectar_explosion_supernova(df[region])
    if ES:
        rp.write(f" Región {region - 3}\n {ES}\n")
        rp.write("\n")
        count_explosion = count_explosion + 1
rp.write(f" Explosiones Encontradas: {count_explosion}\n")
rp.write("\n")
rp.write("-----------------------------------------------------------------\n")
rp.write(" PULSARES\n")
rp.write("-----------------------------------------------------------------\n")
for region in regiones:
    pulsar = detectar_pulsar(df[region])
    if pulsar:
        rp.write(f" Región {region - 3}\n El pulsar tiene una periodicidad de {pulsar * 2} días\n")
rp.write("\n")
rp.write("-----------------------------------------------------------------\n")
rp.write(" NUEVOS PLANETAS\n")
rp.write("-----------------------------------------------------------------\n")
NPE = 0
for region in regiones:
    NP = detectar_nuevo_planeta(df[region])
    if NP:
        rp.write(f" Región {region - 3}\n Se encontró un nuevo planeta\n")
        NPE = NPE + 1
        rp.write("\n")
rp.write(f" Nuevos Planetas Encontrados: {NPE}\n")
rp.write("\n")
rp.write("-----------------------------------------------------------------\n")
rp.write(" CUÁSAR\n")
rp.write("-----------------------------------------------------------------\n")
for region in regiones:
    quazar = detectar_quazar(df[region])
    if quazar:
        rp.write(f" Región {region - 3}\n Se detectó un cuásar el día {quazar}\n")
rp.write("\n")
rp.write("-----------------------------------------------------------------\n")
rp.write("GRUPO: JOSEFINA, SEBASTIAN Y SAVKA\n")
rp.write("-----------------------------------------------------------------\n")
"""
CONSOLA
"""
print("")
print("ESTADÍSTICAS DEL PROCESO")
print(f"Datos Procesados: {len(regiones) * len(df.index)} datos astronómicos")
print(f"Fecha de Inicio:  {df.fecha[0]}")
print(f"Fecha de Término: {df.fecha[num_ancho - 1]}")
print("")
print("_______________________________________________________")
print("REPORTE DEL PROCESO EN Resultados.txt")
print("-------------------------------------------------------")
"""
CERRAR ARCHIVOS
"""
rp.close()
"""
df.close()
AttributeError: 'DataFrame' object has no attribute 'close'
"""
