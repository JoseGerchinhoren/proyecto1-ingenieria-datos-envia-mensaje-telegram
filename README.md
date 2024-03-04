# README en Español

## Proyecto de Ingeniería de Datos: Alerta de Lluvia por Mensaje de Bot de Telegram

Este proyecto tiene como objetivo enviar alertas de lluvia a través de un bot de Telegram utilizando datos del pronóstico del clima proporcionados por WeatherAPI.

### En este README encontrarás:

- **Funcionamiento del Código:** Detalles sobre cómo funciona el script y las etapas que sigue para enviar alertas de lluvia.
  
- **Automatización del Proceso:** Instrucciones para automatizar el envío de mensajes de alerta de lluvia utilizando una instancia de Ubuntu de EC2 en AWS.
  
- **Notas Adicionales:** Información adicional sobre la configuración del bot de Telegram, la instancia de EC2 y otros detalles importantes.

---

A partir de aquí, puedes continuar con el resto del contenido del README, detallando cada sección según lo especificado.

### Funcionamiento del Código

En este proyecto, se ha desarrollado un script en Python que utiliza la API de WeatherAPI para obtener el pronóstico del clima y enviar alertas de lluvia a través de un bot de Telegram. A continuación, se describe el funcionamiento del código:

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

Con esta descripción, se ofrece una comprensión general del flujo de trabajo del script y cómo se utilizan las diferentes funcionalidades para proporcionar alertas de lluvia a través de un bot de Telegram.

### Automatización del Proceso

Para automatizar el envío de mensajes de alerta de lluvia con una instancia de Ubuntu de EC2 en AWS, se pueden seguir los siguientes pasos:

1. **Clonar el Repositorio:**
   ```bash
   git clone https://github.com/JoseGerchinhoren/proyecto1-ingenieria-datos-envia-pronostico
   cd proyecto1-ingenieria-datos-envia-pronostico
   ```

2. **Editar el Archivo de Configuración:**
   - Editar el archivo `mensaje_telegram.py` para actualizar las claves de API y el token de acceso al bot de Telegram.
   ```bash
   nano mensaje_telegram.py
   ```
   - Modificar las líneas `API_KEY_WAPI` y `TOKEN` con las claves de API y el token proporcionados por WeatherAPI y BotFather respectivamente. Eliminar la importación de `telegram_config`.

3. **Instalar Dependencias:**
   ```bash
   sudo apt update
   sudo apt upgrade
   sudo apt install python3-pip
   pip install -r requirements.txt
   ```

4. **Ejecutar el Script, para prueba:**
   ```bash
   python3 mensaje_telegram.py
   ```

5. **Programar la Ejecución:**
   - Editar el cron job:
   ```bash
   crontab -e
   ```
   - Agregar la siguiente línea para que el script se ejecute diariamente a las 7:30 AM:
   ```bash
   30 7 * * * python3 /home/ubuntu/proyecto1-ingenieria-datos-envia-pronostico/mensaje_telegram.py
   ```

### Notas Adicionales

#### Notas Telegram:

-- Actualizar el archivo `config_telegram_ejemplo.py`, modificar nombre a `config_telegram_.py` con las claves de API y el token propios.
- Crear un bot de Telegram utilizando BotFather y obtener el token de acceso.
- Obtener tu ID de chat utilizando un bot como Userinfobot.

#### Notas EC2:

- Actualizar el archivo `mensaje_telegram.py` con las claves de API y el token proporcionados.
- Ejecutar `crontab -e` para programar la ejecución diaria del script.
- Verificar la configuración de crontab con `crontab -l`.
- Asegurarse de seleccionar ssh.service al actualizar.
- Ejecutar `date` para verificar la fecha y hora del servidor.

Con estos pasos, se automatizará el envío de mensajes de alerta de lluvia a través del bot de Telegram basado en el pronóstico del clima proporcionado por WeatherAPI.


# README in English:

## Data Engineering Project: Rain Alert via Telegram Bot

This project aims to send rain alerts through a Telegram bot using weather forecast data provided by WeatherAPI.

### Table of Contents:

- **Code Operation:** Details on how the script works and the steps it follows to send rain alerts.
  
- **Process Automation:** Instructions for automating the rain alert message sending process using an Ubuntu instance on EC2 in AWS.
  
- **Additional Notes:** Additional information about configuring the Telegram bot, the EC2 instance, and other important details.

---

### Code Operation

In this project, a Python script has been developed that utilizes the WeatherAPI to obtain weather forecasts and send rain alerts via a Telegram bot. Below is a breakdown of how the code operates:

1. **Weather Forecast Retrieval:**
   - The WeatherAPI is utilized to obtain weather forecasts for a specific location. An API key is provided to access weather data.

2. **Processing Forecast Data:**
   - Weather forecast data is processed to extract relevant details such as date, time, weather conditions, temperature, and probability of rain for each hour of the day.

3. **Rain Hour Filtering:**
   - Hours forecasted for rain between 6:00 AM and 11:00 PM are filtered.

4. **Translation of Weather Conditions:**
   - The Googletrans library is used to translate weather conditions into the desired language (in this case, Spanish). This facilitates comprehension of the forecast for users receiving the alert.

5. **Telegram Message Sending:**
   - A message is constructed containing the rain forecast for the current day in the specified location. This message is sent via the Telegram bot using the access token provided by BotFather.

This description provides a general understanding of the script's workflow and how different functionalities are utilized to provide rain alerts via a Telegram bot.

### Process Automation

To automate the sending of rain alert messages using an Ubuntu instance on EC2 in AWS, the following steps can be followed:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/JoseGerchinhoren/proyecto1-ingenieria-datos-envia-pronostico
   cd proyecto1-ingenieria-datos-envia-pronostico
   ```

2. **Edit the Configuration File:**
   - Edit the `mensaje_telegram.py` file to update the API keys and access token for the Telegram bot.
   ```bash
   nano mensaje_telegram.py
   ```
   - Modify the `API_KEY_WAPI` and `TOKEN` lines with the API keys and token provided by WeatherAPI and BotFather respectively. Remove the import of `telegram_config`.

3. **Install Dependencies:**
   ```bash
   sudo apt update
   sudo apt upgrade
   sudo apt install python3-pip
   pip install -r requirements.txt
   ```

4. **Run the Script for Testing:**
   ```bash
   python3 mensaje_telegram.py
   ```

5. **Schedule Execution:**
   - Edit the cron job:
   ```bash
   crontab -e
   ```
   - Add the following line to execute the script daily at 7:30 AM:
   ```bash
   30 7 * * * python3 /home/ubuntu/proyecto1-ingenieria-datos-envia-pronostico/mensaje_telegram.py
   ```

### Additional Notes

#### Telegram Notes:

- Update the `config_telegram_example.py` file, rename it to `config_telegram_.py` with your API keys and token.
- Create a Telegram bot using BotFather and obtain the access token.
- Obtain your chat ID using a bot like Userinfobot.

#### EC2 Notes:

- Update the `mensaje_telegram.py` file with the provided API keys and token.
- Execute `crontab -e` to schedule the daily execution of the script.
- Verify the crontab configuration with `crontab -l`.
- Ensure to select ssh.service when updating.
- Execute `date` to verify the server's date and time.

Following these steps will automate the sending of rain alert messages via the Telegram bot based on the weather forecast provided by WeatherAPI.