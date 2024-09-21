import pandas as pd
from datetime import datetime
from plyer import notification
import configparser
import requests

# Leer el archivo de configuración
config = configparser.ConfigParser(comment_prefixes=('#', '//'))
config.read('token.ini')
# Obtener el token y el chat ID del archivo de configuración
TOKEN = config['DEFAULT']['TOKEN']
CHAT_ID = config['DEFAULT']['CHAT_ID']

# Cargar el cronograma desde el archivo Excel
file_path = "cronograma_medicamentos.xlsx"

# Obtener la fecha actual
today = datetime.today().date()

# Mensaje a enviar a Telegram
mensaje = "¡Hola! Soy tu asistente personal de medicamentos. 🤖"

# URL de la API de Telegram
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Datos a enviar vía POST a la API de Telegram
data = {
    "chat_id": CHAT_ID,
    "text": mensaje
}

# MEDICAMENTOS A NO TOMAR
# Recorrer el cronograma para verificar alarmas
# Especificar el nombre de la hoja de cálculo y pestaña
sheet_name = 'notomar'
df = pd.read_excel(file_path, sheet_name=sheet_name)
for index, row in df.iterrows():
    medicamento = row['Medicamento']
    #print(f"Verificando {medicamento}...")
    fecha_inicio = row['Fecha de inicio']
    #print(f"Fecha de inicio 1: {fecha_inicio}")
    fecha_inicio = fecha_inicio.date()
    #print(f"Fecha de inicio 2: {fecha_inicio}")
    fecha_fin = row['Fecha de fin']
    #print(f"Fecha de fin 1: {fecha_fin}")
    fecha_fin = fecha_fin.date()
    #print(f"Fecha de fin 2: {fecha_fin}")

    # Verificar si la fecha actual coincide con la fecha de inicio
    if today == fecha_inicio:
        # Mostrar notificación en el sistema
        """
        notification.notify(
            title=f"Inicio de suspensión: {medicamento}",
            message=f"Hoy comienza la suspensión de {medicamento}.",
            timeout=10
        )
        """
        # Enviar mensaje a Telegram
        mensaje = f"Hoy comienza la suspensión de {medicamento}."
        # Guardar mensaje en data.text
        data['text'] = mensaje
        response = requests.post(url, data=data)
        # Verificar si el mensaje fue enviado correctamente
        if response.status_code == 200:
            print("Mensaje enviado correctamente.")
        else:
            print("Error al enviar el mensaje.")
            print(response.json())

    # Verificar si la fecha está entre la fecha de inicio y la fecha de finalización
    if fecha_inicio < today < fecha_fin:
        # Mostrar notificación en el sistema
        """
        notification.notify(
            title=f"Suspensión en curso: {medicamento}",
            message=f"Hoy no debes tomar {medicamento}.",
            timeout=10
        )
        """
        # Enviar mensaje a Telegram
        mensaje = f"Hoy no debes tomar {medicamento}."
        # Guardar mensaje en data.text
        data['text'] = mensaje
        response = requests.post(url, data=data)
        # Verificar si el mensaje fue enviado correctamente
        if response.status_code == 200:
            print("Mensaje enviado correctamente.")
        else:
            print("Error al enviar el mensaje.")
            print(response.json())

    # Verificar si la fecha actual coincide con la fecha de finalización
    if today == fecha_fin:
        # Mostrar notificación en el sistema
        """
        notification.notify(
            title=f"Fin de suspensión: {medicamento}",
            message=f"Hoy finaliza la suspensión de {medicamento}.",
            timeout=10
        )
        """
        # Enviar mensaje a Telegram
        mensaje = f"Hoy finaliza la suspensión de {medicamento}."
        # Guardar mensaje en data.text
        data['text'] = mensaje
        response = requests.post(url, data=data)
        # Verificar si el mensaje fue enviado correctamente
        if response.status_code == 200:
            print("Mensaje enviado correctamente.")
        else:
            print("Error al enviar el mensaje.")
            print(response.json())

# MEDICAMENTOS A
# Recorrer el cronograma para verificar alarmas
# Especificar el nombre de la hoja de cálculo y pestaña
sheet_name = 'tomar'
df = pd.read_excel(file_path, sheet_name=sheet_name)
for index, row in df.iterrows():
    medicamento = row['Medicamento']
    #print(f"Verificando {medicamento}...")
    fecha_toma = row['Fecha de toma']
    #print(f"Fecha de toma 1: {fecha_inicio}")
    fecha_toma = fecha_toma.date()
    #print(f"Fecha de toma 2: {fecha_inicio}")

    # Verificar si la fecha actual coincide con la fecha de inicio
    if today == fecha_toma:
        # Mostrar notificación en el sistema
        """
        notification.notify(
            title=f"Toma de Medicamento: {medicamento}",
            message=f"Hoy te toca tomar {medicamento}.",
            timeout=10
        )
        """
        # Enviar mensaje a Telegram
        mensaje = f"Hoy te toca tomar {medicamento}."
        # Guardar mensaje en data.text
        data['text'] = mensaje
        response = requests.post(url, data=data)
        # Verificar si el mensaje fue enviado correctamente
        if response.status_code == 200:
            print("Mensaje enviado correctamente.")
        else:
            print("Error al enviar el mensaje.")
            print(response.json())
