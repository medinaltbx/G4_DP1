Data Project 1 - Master Data Analytics EDEM

Grupo 4 - Caso 1 - Metaverso

Equipo:
- Enrique Badenas Cazorla
- Ramón Casans Camp
- Cristian Medina Azorín
- Hermán Redondo Lázaro
- Galo Valle GarcÍa

![logo.png](images/logopng.png)

```bash
G4_DP1/
├─ connection/
│  ├─ pycache__/
│  ├─ index.js
│  ├─ db_postgres.py
│  ├─ docker-postgres.txt
├─ docker/
│  ├─ docker-grafana/  #Visualizaciones dashboard
│  │  ├─ docker-compose.yml
│  │  ├─ info.txt
│  ├─ docker_postgres_with_data/  #Contenedor base de datos
│  │  ├─ sql/
│  │  │  ├─ create_tables.sql                
│  │  ├─ docker-compose.yml
│  ├─ docker-kafka-zookp/  #Contenedor kafka y zookeeper 
├─ images/
│  ├─ Costes.xlsx
├─ src/
│  ├─ leaflet_map_app/
│  │  ├─ templates/
│  │  │  ├─ index.html
│  │  │  ├─ logo.png
│  │  │  ├─ logo_con_fondo.png
│  │  │  ├─ matches.html
│  │  │  ├─ white_logo.png
│  │  ├─ app.py  
│  │  ├─ web_info
│  │  ├─ white_logo.png
│  ├─ consumer.py  #Lógica de matches
│  ├─ producer.py  #Generador de datos
│  ├─ upload_match.py #Capta matches, transforma y sube datos
│  ├─ upload_raw_data.py #Transforma y almacena datos
├─ testing/
│  ├─ folium_tests/
│  ├─ leaflet_test_1/
│  ├─ Arquitectura v2.pptx
├─ README.md
├─ requirements.txt
```


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
![img_1.png](images/zookeper_running.png)

En este punto se encuentran corriendo tanto kafka como zookeper, por lo que solo es necesario instalar las dependencias de python recogidas en requirements.txt.

3. Abrimos el repositorio en el IDE que utilicemos (visual studio code, pycharm etc.) e instalamos las liberías utilizando:
```
pip install -r G4_DP1/requirements.txt
```
Si no funciona, copiad la ruta **absoluta** de requirements, en mi caso:
```
pip install r'C:\Users\Cristian\Documents\repos\G4_DP1\requirements.txt'
```
4. A continuación se pueden ejecutar los scripts de producer.py y consumer.py de la carpeta src

### Conectar con base de datos:

1. Nos dirigimos a la carpeta G4_DP1\docker\docker_postgres_with_data
```
cd G4_DP1\docker\docker_postgres_with_data
```

2.Ejecutamos el siguiente comando para levantar el contenedor de base de datos: 
````
docker-compose up
````
El contenedor se inicializa automáticamente creando las dos tablas PostgreSQL, raw_data y matches.

3.En este punto ya tenemos acceso desde la clase "bbdd" del script connection/db_postgres.py (Actualmente no cuenta con ninguna tabla, ver más adelante como crearla desde el inicio). Podemos comprobar su comportamiento accediendo al contenedor. Para ello, buscamos el id del contenedor:
````
docker ps
````
4. **Localizamos el identificador del contenedor** (con los tres primeros dígitos es suficiente) y ejecutamos:
```
docker exec -it 3id bin/bash
```
5. Solo nos queda acceder a la base de datos ejecutando:
```
psql -U root -d metaverso
```
6. Podemos realizar consultas sobre la base de datos para comprobar que todo se está subiendo correctamente.

### Ejecutar el proyecto:

Una vez que contamos con los contenedores referentes a kafka y a PostgreSQL corriendo, podemos pasar a ejecutar las partes del proyecto.

1. En primer lugar, ejcutamos el script producer. El objetivo de este script es generar los datos y enviarlos a un topic de Kafka llamado _generator_. Podemos ejecutar el script mediante el IDE que estemos utilizando o bien mediante consola. Para ello, nos situamos en la carpeta _src_ y ejecutamos:

```
python producer.py
```

Una vez que se encuentre bajo ejecución, observaremos un output similar al siguiente:
![img.png](images/datagenerator.png)

2. En segundo lugar, ejecutaremos el script upload_raw_data.py, el cual leerá del topic _generator_, transformará los mensajes a formato tabular y los almacernará en la tabla _raw_data_.

3. Tras esto, podemos ejecutar el script _consumer.py_, el cual contiene toda la lógica para calcular los matches entre amigos. Lee los datos del topic _generator_, calcula los matches y transmite el resultado al topic _matches_

4. Por último, ejecutamos el script _upload_match.py_, el cual se encarga de captar todos los mensajes del topic _matches_, tranformar los datos y subirlos a su tabla correspondiente en base de datos _matches_

5. Para comprobar que todo ha funcionado, accedemos a base de datos siguiendo los pasos explicados en el apartado anterior. Ejecutamos los comandos:
```
SELECT * FROM raw_data;
```
![img.png](images/raw_data.png)

````
SELECT * FROM matches;
````
![img_1.png](images/matches.png)

### Visualización del mapa en tiempo real:

Una vez que todas las partes anteriores se encuentren en ejecución, podemos pasar a visualizar el mapa con los diferentes usuarios. Para ello, necesitamos ejecutar el script _app.py_ ubicado en:

```
src/leaflet_map_app/app.py
```
y abrir el navegador introduciendo la siguiente ruta:
```
localhost:5001
```
### Visualización web:
Tenemos dos opciones de visualización: 
* Visualización de usuarios activos.
* Visualización de matches.

Para poder generar ambas vistas, es necesario completar los pasos previos de ejecución del proyecto. Ejecutamos el archivo indistintamente por consola o mediante el IDE:
```
src/leaflet_map_app/src.py
```

En este punto ambas páginas se encuentran operativas, y podemos acceder a ellas para observar la visualización en tiempo real con:

* Visualización de usuarios activos:
```
http://127.0.0.1:5001/
```
![img.png](images/usuarios_activos.png)
* Visualización de matches:
```
http://127.0.0.1:5001/matches
```
![img.png](images/matches_map.png)
### Grafana:
1. Para correr grafana, en primer lugar debemos descargarnos la imagen:
````
docker run -d --name=grafana -p 3000:3000 grafana/grafana
````
2. Una vez que el contenedor este corriendo, podemos acceder a grafana introduciendo en el navegador la siguiente ruta:
```
localhost:3000
```
3. Para acceder por primera vez, debemos introducir _admin_ tanto en usuario como en contraseña. Posteriormente, se nos pedirá que cambiemos la contraseña.

4. A continuación, debemos conectar grafana a la base de datos. Para ello, rellenaremos los datos de la siguiente forma:
* Host:  host.docker.internal:5432
* Databse: metaverso
* User: grafana
* Password: metaverso
* TLS/SSL Mode: disable
* Version: 10
![img.png](images/conexion_grafana.png)
Presionamos en **Save & Test**. Si todo ha funcionado correctamente, veremos el siguiente mensaje:
![img.png](images/connection_ok.png)
5. En este punto ya podemos realizar las visualizaciones que deseemos en la pestaña **dashboard**:
![img_3.png](images/create_dashboard.png)
