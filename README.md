# Dispositivo electrónico de información comunitaria
## Introducción
Este proyecto fue ideado con la intención de apoyar a las comunidades a través de un dispositivo capaz de mostrar comunicados oficiales del ayuntamiento, estadísticas metrorológicas (mediante la API OpenWeather) y parámetros importantes de salud (específicamente el ritmo cardiaco y el oxígeno en sangre).
Además, será una introducción para las personas poco familiarizadas con la tecnología mediante el uso de una interfaz gráfica (dashboard), o bien, una fuente de información fidedigna y actualizada para personas que dispongan de un dispositivo capaz de ejecutar la aplicación Telegram.
Para administrar gran parte de la información desplegada en el dashboard se hará uso de un Bot de Telegram; los usuarios a quienes se les asigne el rol de Administrador podrán publicar imágenes y/o texto en opciones como: dónde ir, apoyo a la comunidad, publicaciones a la comunidad, etc.
La implementación se compone de un kiosco ubicado en lugares céntricos o estratégicos para que cualquier persona tenga acceso a este. Este Kiosco contará con el sensor MAX30102 para las lecturas médicas antes mencionadas, y una pantalla táctil en la cual se visualizarán datos como: un esquema rápido pulso cardiaco y niveles de oxigenación en la sangre, información del clima, hora de amanecer local, comunicados para la comunidad, etc.
Se podrán realizar las adecuaciones pertinentes según las necesidades de la comunidad, tales como modificar las opciones a las que tendrá acceso el administrador, agregar los administradores necesarios, limitar la cantidad de comunicados que se podrán visualizar en Telegram, etc.
La información proporcionada en el kiosco ayudará en la toma de decisiones y acciones en beneficio de una persona (salud) o la comunidad (clima), a la par de fungir como cimientos de las comunidades IoT con el uso de este proyecto en su vida cotidiana.


## Software
* Python (BackEnd)
* JavaScript (Node js) (FrontEnd) (Interfaz web) (HTML) (CSS)
* Node-Red (Flujo y Manejo de Datos) (Back End) (Front End)
* API Rest openweather (Para llamada a estado del clima) 
* Sistema operativo Linux Raspbian (RaspberryOS)
* Sistema Operativo Linux (Debian(v 10) Buster)
* Base de datos no relacional (MongoDB)
* Telegram (Envío y recepción de mensajes)
* Cloud computing (Google cloud - IBM cloud - AWS (Opcional))

![Arquitectura ejemplo de una implementación en cloud, con un backup implementado en otra nube](https://github.com/r4gm/Proyecto-CAPSTONE-Dispositivo-electronico-de-informacion-comunitaria/blob/main/Figuras_referencia/Arquitectura_ejemplo.jpg)


## Hardware
* Raspberry Pi 4 (8 GB de RAM)
* Sensor MAX30102
* Protoboard
* GPIO Extension Board
* Adaptador GPIO a Protoboard para Raspberry Pi
* Pantalla o Tablet para presentación de Dashboard informativo
* Dispositivo que soporte app de Telegram


## Circuito
| Raspberry Pi 4 | MAX30102 |
| :-------------: | :-------------: |
| 3.3 V (pin 1)  | VIN  |
| I2C_SDA 1 (pin 3)  | SDA  |
| I2C_SCL 1 (pin 5)  | SCL  |
| GND (pin 9)  | GND  |

![Circuito a realizar](https://github.com/r4gm/Proyecto-CAPSTONE-Dispositivo-electronico-de-informacion-comunitaria/blob/main/Figuras_referencia/Circuito.png)


## Código del sensor MAX30102 en Visual Studio Code
1. Acceder al [repositorio](https://github.com/r4gm/Proyecto-CAPSTONE-Dispositivo-electronico-de-informacion-comunitaria/tree/main/python_code) de Python en Github.
2. Importar los archivos: 
	* [hrcalc.py](https://github.com/r4gm/Proyecto-CAPSTONE-Dispositivo-electronico-de-informacion-comunitaria/blob/main/python_code/hrcalc.py)
	* [hrdump.py](https://github.com/r4gm/Proyecto-CAPSTONE-Dispositivo-electronico-de-informacion-comunitaria/blob/main/python_code/hrdump.py)
	* [max30102.py](https://github.com/r4gm/Proyecto-CAPSTONE-Dispositivo-electronico-de-informacion-comunitaria/blob/main/python_code/max30102.py)
	* [MAX30102_GUI.py](https://github.com/r4gm/Proyecto-CAPSTONE-Dispositivo-electronico-de-informacion-comunitaria/blob/main/python_code/MAX30102_GUI.py)
	* [prueba01.py](https://github.com/r4gm/Proyecto-CAPSTONE-Dispositivo-electronico-de-informacion-comunitaria/blob/main/python_code/prueba01.py) - Archivo con el cual se realizará la simulación.
	2.1. Para cada uno de los archivos, seleccionar la opción _Raw_
	2.2. Se abrirá una ventana en la cual estará el código "en limpio", se debe copiar todo el código y pegarlo en un archivo nuevo en el IDE de preferencia.
	_Se usó Visual Studio Code para el manejo de los archivos del sensor._
	2.3. Guardar  los archivos con su respectivo nombre en GitHub, ya que estos se importaran después y se usaran para poder identificarlos entre sí.
3. Ejecutar el archivo _prueba01_ (encargado de iniciar el sensor).
	_Dicho archivo ya tiene la conexión por medio de MQTT al broker.hivemq.com (línea 9), así como la publicación en el topic "Max30102G4GRG/heartrate" que corresponderá al ritmo cardiaco y "Max30102G4GRG/blood" que es el Oxigeno en la sangre (líneas 33 y 35 respectivamente)._
4. Se podrá visualizar los valores obtenidos por el sensor MAX30102.


## Configurar Servidor de Node-Red

### Bot de Telegram
**Importar Bot de Telegram**
Librerías requeridas para el funcionamiento de la aplicación:
* node-red-contrib-telegrambot
* node-red-node-openweathermap
* node-red-node-mongodb
* node-red-contrib-image-tools
* node-red-dashboard

_Pasos para instalar la librería_
```
-> Menú Hamburguesa 
-> Manage Palette 
-> Install 
-> Ingresar la clave de la librería 
-> Clic Install
```

_Una vez instaladas las librerías, se debe importar el [código](https://github.com/r4gm/Proyecto-CAPSTONE-Dispositivo-electronico-de-informacion-comunitaria/blob/main/node-red_code/Bot_Telegram.json) referente al bot de Telegram:_
```
-> Menú Hamburguesa 
-> Import
-> Ingresar el código JSON 
-> e importar
```

Una vez importado, se visualizarán los nodos de node-red.
![nodos de node-red para el Bot de Telegram](https://github.com/r4gm/Proyecto-CAPSTONE-Dispositivo-electronico-de-informacion-comunitaria/blob/main/Figuras_referencia/Flow_Bot_Telegram.png).

**Configuración del Bot de Telegram**

Realizar las siguientes configuraciones en el Flow del Bot de Telegram:
1. Acceder al nodo _/start_.
2. Dar clic en el ícono del lápiz.
3. Ingrese el Token adquirido desde Telegram @BotFather y salve el dato dando clic en Update y después en Done.
	_Más información y creación de bot en bot father: https://core.telegram.org/bots_
	_Una vez validado el Token, se actualizará este dato en todos los nodos referentes a Telegram._
4. En los 2 nodos _Clima Estados_ del Flow
	4.1. Hacer clic en _Clima Estados_.
	4.2. Registrarse en openweathermap.
	4.3. Ingresar el [API key](https://home.openweathermap.org/api_keys).
5. Hacer clic en cualquier nodo mongo (ej. _Mongo Insert Texto_).
6. Cambiar los campos
	6.1. Host (URL del servidor de mongo).
	6.2. Username y Password.
		_Debe crear su usuario y contraseña para acceso a la base de datos._
		_Se obtienen desde el servidor implementado de mongodb._
	6.3. Clic en Update y Done.
		_Se actualizarán todos los nodos de Mongo._
		_Servidor montado en MongoDB Atlas [https://www.mongodb.com/atlas/database]_
7. Realizar un deploy al flow.

Realizar las siguientes configuraciones para agregar el rol administrador a un usuario:
1. Ingresar al bot de telegram creado y dar clic en _/start_.
2. Regresar al flow de node-red y verificar el debug.
	_A este llega su ID de Telegram_
3. Autorizar a un usuario acceder al menú administrador.
	3.1. Copiar el ID del usuario.
	3.2. Ir al nodo _User Detect_ (se encuentran 2 activos en el nodo, se deben actualizar ambos).
	3.3. Ingresar su ChatID de Telegram.
4. Verificar el cambio de rol.
	4.1. Vuelva a escribir _/start_ en el chat bot de Telegram.
	4.2. Ahora se debe visualizar un botón adicional para las opciones de administrador.
	_La fase del bot del proyecto estará conectada y se podrá agregar datos a MongoDB_


### Dashboard
**Importar Dashboard**
_Primero, se debe importar el [código](https://github.com/r4gm/Proyecto-CAPSTONE-Dispositivo-electronico-de-informacion-comunitaria/blob/main/node-red_code/Dashboard.json) referente al Dashboard, tal y como se realizó para el Bot de Telegram._

Una vez importado, se visualizarán los nodos de node-red.
![nodos de node-red para el Dashboard](https://github.com/r4gm/Proyecto-CAPSTONE-Dispositivo-electronico-de-informacion-comunitaria/blob/main/Figuras_referencia/Flow_Dashboard.png).

**Configuración del Dashboard**
1. En los nodos MQTT de _MQTTHeartRate_ y _MQTTBlood_ se debe poner el topic que asignó desde el programa de Python.
	_Ejemplo de topic:_
	_mitopic/blood y mitopic/heartrate y done_
2. En el nodo _clima_, ingresar su APIKey.
3. Dar clic en Deploy.

Se podrá visualizar el [dashboard](https://github.com/r4gm/Proyecto-CAPSTONE-Dispositivo-electronico-de-informacion-comunitaria/blob/main/Figuras_referencia/Dashboard.png) ingresando a la dirección http://<IP-Dirección>:1880/ui/
_Recuerde que debe tener datos cargados en la base de datos de MongoDB con el bot previamente configurado._


## Instrucciones de Operación
### Uso correcto del Sensor MAX30102
El usuario deberá colocar la yema del dedo sobre el cuadro infrarrojo del lector del sensor 
Para esto se emplea un pulsioxímetro, que es un dispositivo que integra emisores de luz y el sensor que mide la cantidad de luz reflejada por el dedo del usuario. La luz detectada por el sensor varía de acuerdo a la concentración de oxígeno en la sangre, la sangre oxigenada absorbe mayor cantidad de luz infrarroja, mientras que la sangre poco oxigenada absorbe mayor luz roja.

### Interactuar con el bot de telegram “Información Comunitaria”
Para consultar las opciones disponibles se debe usar el comando _/start_.

**Opciones para el usuario**
```
* Clima: Se desplegan datos como Ciudad en la que se encuentra, Temperatura Actual, Nubosidad , Temperatura Máxima/Mínima , Humedad, Velocidad del viento, Dirección del viento , Hora del Amanecer y Hora del Anochecer.
* Dónde Ir: Desplega una serie de lugares y establecimientos en función a recomendaciones de usuarios. 
* Apoyo a la Comunidad: Se visualizan comunicados en beneficio de la comunidad.
* Publicaciones a la comunidad: Aquí se mostrarán avisos del ayuntamiento para la comunidad.
* Medios de contacto Ayuntamiento: Información importante como Teléfono , Correo y Ubicación del propio Ayuntamiento.
* Información Pública: Se verán diversos comunicados generales (por ejemplo, información estatal o nacional) de interés para la comunidad.
```

**Opciones para el administrador**
```
* Información.
* Donde Ir.
* Apoyo a la Comunidad.
* Publicaciones a la Comunidad.
```
_Cada que se seleccione una opción se desplegará un texto con las instrucciones para realizar la respectiva publicación._


## Colaboradores
* Rafael González Martínez
* Germán Pacheco Castillo
* Grecia Nefertari Flores Martínez