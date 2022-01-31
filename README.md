Data Project 1 - Master Data Analytics EDEM

Grupo 4 - Caso 1 - Metaverso

Equipo:
- Enrique Badenas Cazorla
- Ramón Casans Camp
- Cristian Medina Azorín
- Hermán Redondo Lázaro
- Galo Valle GarcÍa

![logo.png](images/logopng.png)

### Forma de uso del proyecto:


1. Desde la consola, dirígete a la carpeta donde quieras clonar el repositorio y descárgalo:
```console
git clone https://github.com/Enriquebadenas/G4_DP1.git
```
2. Dirígete a la ruta donde se encuentre kafka-zookp-docker y ejecuta:
![image](https://user-images.githubusercontent.com/90957463/151770262-a91fa6ca-78d5-48df-a357-cb5e0e6249be.png)
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

### Visualizaciones:

1. Dashboard conexiones, abrir navegador y acceder a:
localhost:3000

2. Mapa con los usuarios real-time, abrir navegador y acceder a:
localhost:5001
