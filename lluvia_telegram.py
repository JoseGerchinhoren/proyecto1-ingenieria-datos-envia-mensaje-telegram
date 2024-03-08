import pandas as pd
import requests
import telegram_config
from googletrans import Translator

# Query para la ubicación
query = 'Salta'
# Clave de API de WeatherAPI
api_key = telegram_config.API_KEY_WAPI

# URL para obtener el pronóstico del clima
url_clima = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={query}&days=1&aqi=no&alerts=no'

# Obtener la respuesta de la API del clima en formato JSON
response = requests.get(url_clima).json()

# Función para obtener los detalles del pronóstico del clima para una hora específica
def get_forecast(response, i):
    fecha = response['forecast']['forecastday'][0]['hour'][i]['time'].split()[0] # Fecha
    hora = int(response['forecast']['forecastday'][0]['hour'][i]['time'].split()[1].split(':')[0]) # Hora
    condicion = response['forecast']['forecastday'][0]['hour'][i]['condition']['text'] # Condicion
    tempe = response['forecast']['forecastday'][0]['hour'][i]['temp_c'] # Temperatura
    rain = response['forecast']['forecastday'][0]['hour'][i]['will_it_rain'] # Llovera o no, 0 para no, 1 para si
    prob_rain = response['forecast']['forecastday'][0]['hour'][i]['chance_of_rain'] # Posibilidad de lluvia
    return fecha, hora, condicion, tempe, rain, prob_rain

# Lista para almacenar los detalles del pronóstico del clima
datos = []

# Iterar sobre las horas en el pronóstico y obtener los detalles
for i in range(len(response['forecast']['forecastday'][0]['hour'])):
    datos.append(get_forecast(response, i))

# Definir los nombres de las columnas del DataFrame
col = ['Fecha', 'Hora', 'Condicion', 'Temperatura', 'Lluvia', 'prob_lluvia']

# Crear un DataFrame con los detalles del pronóstico del clima
df = pd.DataFrame(datos, columns=col)

# Filtrar las horas de lluvia entre las 6:00 y las 23:00
df_rain = df[(df['Lluvia'] == 1) & (df['Hora'] > 6) & (df['Hora'] < 23)]

# Seleccionar las columnas relevantes
df_rain = df_rain[['Hora', 'Condicion']]

# Establecer la hora como índice
df_rain.set_index('Hora', inplace=True)

# Configuración del archivo de registro
log_file = "registro.log"

# Función para escribir en el archivo de registro
def escribir_log(mensaje):
    with open(log_file, "a") as log:
        log.write(mensaje + "\n")

# Función para enviar el mensaje al telegram
def enviar_mensaje_telegram():
    # Token de acceso al bot de Telegram
    token = telegram_config.TOKEN
    # URL para enviar el mensaje
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    # Convertir la columna 'Fecha' al formato de fecha deseado (si aún no está en ese formato)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    # Modificar el formato de fecha a 'dd/mm/aaaa'
    df['Fecha'] = df['Fecha'].dt.strftime('%d/%m/%Y')

    # Crear una instancia del traductor
    translator = Translator()

    # Verificar si hay horas de lluvia
    if not df_rain.empty:
        # Iterar sobre cada fila del DataFrame y traducir el texto en la columna "Condicion"
        for index, row in df_rain.iterrows():
            # Obtener el texto en la columna "Condicion"
            texto_a_traducir = row['Condicion']

            # Verificar si el texto no está vacío
            if texto_a_traducir.strip():  # Verifica si el texto no está vacío
                # Intentar traducir el texto al idioma deseado, por ejemplo, al español ('es')
                try:
                    texto_traducido = translator.translate(texto_a_traducir, dest='es').text
                except Exception as e:
                    error = f"Error al traducir el texto: {str(e)}"
                    print(error)
                    escribir_log(error)
                    texto_traducido = texto_a_traducir  # En caso de error, mantener el texto original
            else:
                texto_traducido = texto_a_traducir  # Si el texto está vacío, mantenerlo como está

            # Actualizar el valor en la columna "Condicion" con el texto traducido o el original
            df_rain.at[index, 'Condicion'] = texto_traducido

        # Construcción del mensaje mejorado
        mensaje = f"""
        El pronóstico de lluvia para hoy {df['Fecha'][0]} en {query} es el siguiente:

        {df_rain.to_string()}
        """

    else:
        # Construir mensaje indicando que no va a llover en ninguna hora
        mensaje = f"No hay pronóstico de lluvia para hoy en {query}."

    parametros = {
        'chat_id': 5410219790,
        'text': mensaje
    }
    
    try:
        respuesta = requests.post(url, data=parametros)
        datos_respuesta = respuesta.json()
        if datos_respuesta['ok']:
            print("Mensaje enviado exitosamente.")
            escribir_log("Mensaje enviado exitosamente.")
        else:
            mensaje_error = f"No se pudo enviar el mensaje: {datos_respuesta['descripcion']}"
            print(mensaje_error)
            escribir_log(mensaje_error)
    except Exception as e:
        error = f"Error al enviar el mensaje: {str(e)}"
        print(error)
        escribir_log(error)

# Envío del mensaje
enviar_mensaje_telegram()