# G4_DP1
### Forma de uso del proyecto:


1. Desde la consola, dirígete a la carpeta donde quieras clonar el repositorio y descárgalo:
```console
git clone https://github.com/Enriquebadenas/G4_DP1.git
```
2. Dirígete a la ruta donde se encuentre kafka-zookp-docker y ejecuta:
```
docker-compose -f docker-compose-expose.yml up
```
Si todo ha ido bien, deberás ver un output similar a este:
![img_1.png](imgs/img_1.png)

En este punto se encuentran corriendo tanto kafka como zookeper, por lo que solo es necesario instalar las dependencias de python recogidas en requirements.txt.
3. Abrimos el repositorio en el IDE que utilicemos (visual studio code, pycharm etc.) e instalamos las liberías utilizando:
```
pip install G4_DP1/requirements.txt
```
Si no funciona, copiad la ruta **absoluta** de requirements, en mi caso:
```
pip install r'C:\Users\Cristian\Documents\repos\G4_DP1\requirements.txt'
```
4. A continuación se pueden ejecutar los scripts de producer.py y consumer.py de la carpeta src
#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~


Informar usuarios
Coordenadas GPS en tiempo real de usuarios

Necesario:
Base de datos de usuarios
Definir campos en base de datos
Definir qué base de datos usaremos
Opción menú para decidir qué tipo de interacción quieres?
Tomar algo
Pasear
Running
Radio de acción para los avisos
Big Query + Data Studio para los dashboards y reporting??

¿Hacer match de las coordenadas GPS aleatorias que generará el generador de datos con los usuarios?
¿El generador proporciona los datos de los usuarios y sus coordenadas? ¿Qué proporciona el generador de datos?
Establecer una ciudad (o metaverso) para desarrollarlo. En la explicación nombrar que el modelo sería escalable a n ciudades.
Aplicación en móvil para poder recibir las alertas de proximidad.
Aplicación en móvil con uso de geolocalización para emitir ubicación.

Cuando un usuario entre en el radio de acción de otro, API lanza mensaje a KAFKA???, y el mensaje está disponible para varios consumers (imprescindible). Huella de tiempo, no puede estar siempre el mensaje disponible porque el usuario puede moverse --> cumplir condición de proximidad para poder consumir los mensajes.

Plan de negocio
¿Cómo se gana el dinero? O fidelización, o venta de los datos de usuarios o publicidad en la aplicación para los anunciantes. Anuncios de eventos cercanos, tiendas o locales para consumir cercanos.
