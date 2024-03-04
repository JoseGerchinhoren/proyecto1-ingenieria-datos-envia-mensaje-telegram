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