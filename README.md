# G4_DP1
*G4 DP1 API para Metaverso*

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
