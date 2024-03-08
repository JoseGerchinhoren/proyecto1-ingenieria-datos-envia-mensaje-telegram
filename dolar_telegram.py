import requests
import telegram_config
from datetime import datetime

# Función para obtener el precio del dólar blue
def obtener_precio_dolar():
    try:
        response = requests.get("https://dolarapi.com/v1/dolares/blue")
        data = response.json()
        return data
    except Exception as e:
        print("Error al obtener el precio del dólar:", str(e))
        return None

# Función para formatear la fecha al formato dd/mm/aaaa
def formatear_fecha(fecha_str):
    fecha = datetime.strptime(fecha_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    return fecha.strftime("%d/%m/%Y")

# Función para escribir en el archivo de registro
def escribir_log(mensaje):
    with open("registro_dolar.log", "a") as log:
        log.write(mensaje + "\n")

# Función para enviar el mensaje al Telegram
def enviar_mensaje_telegram(mensaje):
    token = telegram_config.TOKEN_DOLAR
    url = f"https://api.telegram.org/bot{token}/sendMessage"
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
            print("No se pudo enviar el mensaje:", datos_respuesta['description'])
            escribir_log(f"No se pudo enviar el mensaje: {datos_respuesta['description']}")
    except Exception as e:
        print("Error al enviar el mensaje:", str(e))
        escribir_log(f"Error al enviar el mensaje: {str(e)}")

# Obtener el precio del dólar blue
data_dolar = obtener_precio_dolar()

# Verificar si se pudo obtener el precio del dólar
if data_dolar is not None:
    fecha_actualizacion = formatear_fecha(data_dolar['fechaActualizacion'])
    compra = data_dolar['compra']
    venta = data_dolar['venta']
    mensaje = f"El precio del dolar blue hoy {fecha_actualizacion} es:\nCompra: {compra}\nVenta: {venta}"
else:
    mensaje = "No se pudo obtener el precio del dólar en este momento."

# Envío del mensaje
enviar_mensaje_telegram(mensaje)
