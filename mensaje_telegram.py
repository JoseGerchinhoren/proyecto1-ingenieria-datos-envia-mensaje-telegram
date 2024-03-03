import pandas as pd
import requests
import telegram_config
from googletrans import Translator

query = 'Salta'
api_key = telegram_config.API_KEY_WAPI

url_clima = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={query}&days=1&aqi=no&alerts=no'

response = requests.get(url_clima).json()

def get_forecast(response, i):
    fecha = response['forecast']['forecastday'][0]['hour'][i]['time'].split()[0] # Fecha
    hora = int(response['forecast']['forecastday'][0]['hour'][i]['time'].split()[1].split(':')[0]) # Hora
    condicion = response['forecast']['forecastday'][0]['hour'][i]['condition']['text'] # Condicion
    tempe = response['forecast']['forecastday'][0]['hour'][i]['temp_c'] # Temperatura
    rain = response['forecast']['forecastday'][0]['hour'][i]['will_it_rain'] # Llovera o no, 0 para no, 1 para si
    prob_rain = response['forecast']['forecastday'][0]['hour'][i]['chance_of_rain'] # Posibilidad de lluvia
    return fecha, hora, condicion, tempe, rain, prob_rain

datos = []

for i in range(len(response['forecast']['forecastday'][0]['hour'])):
    datos.append(get_forecast(response, i))

col = ['Fecha', 'Hora', 'Condicion', 'Temperatura', 'Lluvia', 'prob_lluvia']
df = pd.DataFrame(datos, columns=col)

df_rain = df[(df['Lluvia'] == 1) & (df['Hora'] > 6) & (df['Hora'] < 23)]
df_rain = df_rain[['Hora', 'Condicion']]
df_rain.set_index('Hora', inplace=True)

def enviar_mensaje_telegram():
    token = telegram_config.TOKEN
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    # Convertir la columna 'Fecha' al formato de fecha deseado (si aún no está en ese formato)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    # Modificar el formato de fecha a 'dd/mm/aaaa'
    df['Fecha'] = df['Fecha'].dt.strftime('%d/%m/%Y')

    # Crear una instancia del traductor
    translator = Translator()

    # Iterar sobre cada fila del DataFrame y traducir el texto en la columna "Condicion"
    for index, row in df_rain.iterrows():
        # Obtener el texto en la columna "Condicion"
        texto_a_traducir = row['Condicion']

        # Traducir el texto al idioma deseado, por ejemplo, al español ('es')
        texto_traducido = translator.translate(texto_a_traducir, dest='es').text

        # Actualizar el valor en la columna "Condicion" con el texto traducido
        df_rain.at[index, 'Condicion'] = texto_traducido

    # Construcción del mensaje mejorado
    mensaje = f"""
    Hola!
    El pronóstico de lluvia para hoy {df['Fecha'][0]} en {query} es el siguiente:

    {df_rain.to_string()}
    """

    parametros = {
        'chat_id': 5410219790,
        'text': mensaje
    }
    
    try:
        respuesta = requests.post(url, data=parametros)
        datos_respuesta = respuesta.json()
        if datos_respuesta['ok']:
            print("Mensaje enviado exitosamente.")
        else:
            print(f"No se pudo enviar el mensaje: {datos_respuesta['descripcion']}")
    except Exception as e:
        print(f"Error al enviar el mensaje: {str(e)}")

# Envío del mensaje
enviar_mensaje_telegram()