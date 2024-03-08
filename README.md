# README en Español

## Proyecto de Ingeniería de Datos: Alerta de Lluvia y Valor del Dólar por Mensaje de Bot de Telegram

Este proyecto tiene como objetivo enviar un mensaje por telegram de las horas que va a llover durante el día y el valor de compra y venta del dólar blue en Argentina, utilizando una API de pronóstico del clima y una API de cotización de dólar.

### En este README encontrarás:

- **Funcionamiento del Código:** Detalles sobre cómo funciona el script `lluvia_telegram.py` y `dolar_telegram.py`, y las etapas que sigue cada uno para enviar alertas de lluvia y cotizaciones del dólar.
  
- **Automatización del Proceso:** Instrucciones para automatizar el envío de mensajes de alerta de lluvia y cotizaciones del dólar utilizando una instancia de Ubuntu de EC2 en AWS y Cron Job.
  
- **Notas Adicionales:** Información adicional sobre la configuración del bot de Telegram, la instancia de EC2 y otros detalles importantes.

---

A partir de aquí, puedes continuar con el resto del contenido del README, detallando cada sección según lo especificado.

### Funcionamiento del Código

En este proyecto, se han desarrollado dos scripts en Python: uno para enviar alertas de lluvia (`lluvia_telegram.py`) y otro para enviar el valor del dólar blue en Argentina (`dolar_telegram.py`). A continuación, se describe el funcionamiento de cada uno de estos códigos:

### lluvia_telegram.py

1. **Obtención del Pronóstico del Clima:**
   - Se utiliza la API de WeatherAPI para obtener el pronóstico del clima para una ubicación específica. Se proporciona una clave de API para acceder a los datos del clima.

2. **Procesamiento de los Datos del Pronóstico:**
   - Los datos del pronóstico del clima se procesan y se extraen detalles relevantes como la fecha, la hora, la condición climática, la temperatura, y la probabilidad de lluvia para cada hora del día.

3. **Filtrado de Horas de Lluvia:**
   - Se filtran las horas en las que se pronostica lluvia entre las 6:00 y las 23:00 horas.

4. **Traducción de Condiciones Climáticas:**
   - Se utiliza la biblioteca Googletrans para traducir las condiciones climáticas al idioma deseado (en este caso, español). Esto facilita la comprensión del pronóstico para los usuarios que reciben la alerta.

5. **Envío de Mensajes de Telegram:**
   - Se construye un mensaje que incluye el pronóstico de lluvia para el día actual en la ubicación especificada. Este mensaje se envía a través del bot de Telegram utilizando el token de acceso proporcionado por BotFather.

### dolar_telegram.py

1. **Obtención del Precio del Dólar Blue:**
   - Se realiza una solicitud a una API para obtener el precio actualizado del dólar blue en Argentina.

2. **Formateo de la Información:**
   - Se formatea la información obtenida para incluir la fecha, el precio de compra y el precio de venta del dólar blue.

3. **Envío de Mensajes de Telegram:**
   - Se construye un mensaje que incluye la información del valor del dólar blue y se envía a través del bot de Telegram a los usuarios especificados.

### Automatización del Proceso

Para automatizar el envío de mensajes de alerta de lluvia y cotizaciones del dólar con una instancia de Ubuntu de EC2 en AWS, se pueden seguir los siguientes pasos:

1. **Clonar el Repositorio:**
   ```bash
   git clone https://github.com/JoseGerchinhoren/proyecto1-ingenieria-datos-envia-mensaje-telegram
   cd proyecto1-ingenieria-datos-envia-mensaje-telegram
   ```

2. **Editar el Archivo de Configuración:**
   - Para el script `lluvia_telegram.py`, editar el archivo `lluvia_telegram.py` para actualizar las claves de API (opcional), el token de acceso al bot de Telegram.
   - Para el script `dolar_telegram.py`, editar el archivo `dolar_telegram.py` para actualizar el token de acceso al bot de Telegram.
   ```bash
   nano lluvia_telegram.py
   nano dolar_telegram.py
   ```
   - Modificar las líneas necesarias con las claves de API y el token proporcionados por WeatherAPI y BotFather respectivamente.

3. **Instalar Dependencias:**
   ```bash
   sudo apt update
   sudo apt upgrade
   sudo apt install python3-pip
   pip install -r requirements.txt
   ```

4. **Ejecutar el Script, para prueba:**
   ```bash
   python3 lluvia_telegram.py
   python3 dolar_telegram.py
   ```

5. **Programar la Ejecución:**
   - Editar el cron job:
   ```bash
   crontab -e
   ```
   - Agregar la siguiente línea para que los scripts se ejecuten diariamente a las horas deseadas:
   ```bash
   30 10 * * * python3 /home/ubuntu/proyecto1-ingenieria-datos-envia-mensaje-telegram/lluvia_telegram.py
   30 10 * * * python3 /home/ubuntu/proyecto1-ingenieria-datos-envia-mensaje-telegram/dolar_telegram.py
   ```

### Notas Adicionales

#### Notas Telegram:

-- Actualizar los archivos de configuración correspondientes, modificando los nombres a `telegram_config_ejemplo.py` a `telegram_config.py`,  con las claves de API y el token propios.
- Crear un bot de Telegram utilizando BotFather y obtener el token de acceso.
- Obtener tu ID de chat utilizando un bot como Userinfobot.

#### Notas EC2:

- Actualizar los archivos de script correspondientes con las claves de API y el token proporcionados.
- Ejecutar `crontab -e` para programar la ejecución diaria de los scripts.
- Verificar la configuración de crontab con `crontab -l`.
- Ejecutar `date` para verificar la fecha y hora del servidor.

Con estos pasos, se automatizará el envío de mensajes de alerta de lluvia y cotizaciones del dólar a través del bot de Telegram basado en el pronóstico del clima proporcionado por WeatherAPI y en la cotización del dólar blue proporcionada por una API externa.

---

# README in English

## Data Engineering Project: Rain Alert and Dollar Value via Telegram Bot Message

This project aims to send a message via Telegram regarding the hours when it will rain during the day and the buying and selling price of the blue dollar in Argentina, utilizing a weather forecast API and a dollar quoting API.

### In this README you will find:

- **Code Operation:** Details on how the `lluvia_telegram.py` and `dolar_telegram.py` scripts work, and the stages each one follows to send rain alerts and dollar quotes.
  
- **Process Automation:** Instructions to automate the sending of rain alert messages and dollar quotes using an Ubuntu instance on EC2 in AWS and Cron Job.
  
- **Additional Notes:** Additional information about configuring the Telegram bot, EC2 instance, and other important details.

---

From here, you can continue with the rest of the README content, detailing each section as specified.

### Code Operation

In this project, two Python scripts have been developed: one to send rain alerts (`lluvia_telegram.py`) and another to send the value of the blue dollar in Argentina (`dolar_telegram.py`). Here's how each of these codes works:

### lluvia_telegram.py

1. **Weather Forecast Retrieval:**
   - WeatherAPI is used to obtain the weather forecast for a specific location. An API key is provided to access the weather data.

2. **Processing Weather Forecast Data:**
   - Weather forecast data is processed, and relevant details such as date, time, weather condition, temperature, and probability of rain for each hour of the day are extracted.

3. **Filtering Rainy Hours:**
   - Hours with forecasted rain between 6:00 and 23:00 are filtered.

4. **Translation of Weather Conditions:**
   - The Googletrans library is used to translate weather conditions into the desired language (in this case, Spanish). This facilitates understanding of the forecast for users receiving the alert.

5. **Telegram Message Sending:**
   - A message containing the rain forecast for the current day in the specified location is constructed. This message is sent via the Telegram bot using the access token provided by BotFather.

### dolar_telegram.py

1. **Blue Dollar Price Retrieval:**
   - A request is made to an API to obtain the updated price of the blue dollar in Argentina.

2. **Information Formatting:**
   - The obtained information is formatted to include the date, buying price, and selling price of the blue dollar.

3. **Telegram Message Sending:**
   - A message containing the blue dollar value information is constructed and sent via the Telegram bot to the specified users.

### Process Automation

To automate the sending of rain alert messages and dollar quotes with an Ubuntu instance on EC2 in AWS, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/JoseGerchinhoren/proyecto1-ingenieria-datos-envia-mensaje-telegram
   cd proyecto1-ingenieria-datos-envia-mensaje-telegram
   ```

2. **Edit the Configuration File:**
   - For the `lluvia_telegram.py` script, edit the `lluvia_telegram.py` file to update the API keys (optional) and the Telegram bot access token.
   - For the `dolar_telegram.py` script, edit the `dolar_telegram.py` file to update the Telegram bot access token.
   ```bash
   nano lluvia_telegram.py
   nano dolar_telegram.py
   ```
   - Modify the necessary lines with the API keys and the token provided by WeatherAPI and BotFather respectively.

3. **Install Dependencies:**
   ```bash
   sudo apt update
   sudo apt upgrade
   sudo apt install python3-pip
   pip install -r requirements.txt
   ```

4. **Run the Script, for Testing:**
   ```bash
   python3 lluvia_telegram.py
   python3 dolar_telegram.py
   ```

5. **Schedule Execution:**
   - Edit the cron job:
   ```bash
   crontab -e
   ```
   - Add the following line to have the scripts run daily at desired hours:
   ```bash
   30 10 * * * python3 /home/ubuntu/proyecto1-ingenieria-datos-envia-mensaje-telegram/lluvia_telegram.py
   30 10 * * * python3 /home/ubuntu/proyecto1-ingenieria-datos-envia-mensaje-telegram/dolar_telegram.py
   ```

### Additional Notes

#### Telegram Notes:

-- Update the corresponding configuration files, renaming them from `telegram_config_example.py` to `telegram_config.py`, with your API keys and token.
- Create a Telegram bot using BotFather and obtain the access token.
- Obtain your chat ID using a bot like Userinfobot.

#### EC2 Notes:

- Update the corresponding script files with the provided API keys and token.
- Run `crontab -e` to schedule the daily execution of the scripts.
- Verify the crontab configuration with `crontab -l`.
- Run `date` to check the server's date and time.

Following these steps will automate the sending of rain alert messages and dollar quotes via Telegram based on the weather forecast provided by WeatherAPI and the blue dollar quote provided by an external API.