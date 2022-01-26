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
```
docker-compose -f docker-compose-expose.yml up
```
Si todo ha ido bien, deberás ver un output similar a este:
![img_1.png](images/img_1.png)

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

### Conectar con base de datos (provisional):

1. Nos dirigimos a la carpeta postgres_docker_3/pg_data
```
cd /G4_DP1/docker/postgres_docker_v3/pg_data
```

2.Ejecutamos el contenedor creando la base de datos: 
````
docker run -p 5432:5432 -d -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="metaverso" -e POSTGRES_DB="metaverso" -v ${PWD}/pg-data:/var/lib/postgresql/data --name pg-container postgres
````

3.En este punto ya tenemos acceso desde la clase "bbdd" del script connection/db_postgres.py (Actualmente no cuenta con ninguna tabla, ver más adelante como crearla desde el inicio). Podemos comprobar su comportamiento accediendo al contenedor. Para ello, buscamos el id del contenedor:
````
docker ps
````
4. Localizamos el identificador del contenedor (con los tres primeros dígitos es suficiente) y ejecutamos:
```
docker exec -it 3id bin/bash
```
5. Solo nos queda acceder a la base de datos ejecutando:
```
psql -U root -d metaverso
```
