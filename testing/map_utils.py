from datetime import datetime
import pandas as pd
import folium
import random

from faker import Faker
import altair
from IPython.display import display

faker = Faker('es_ES')
vehicles=["Bike","Train","Car", "Walking"]
USERS_TOTAL=100
users={}
for i in range(0,USERS_TOTAL):
        user={}
        user["id"]=faker.ssn()
        user["name"]=faker.first_name()
        user["last_name"]=faker.last_name()
        user["friends"]=[]
        user["position"]={"lat":random.uniform(39.4, 39.5),"lon":random.uniform(-0.3, -0.4)}
        user["transport"]=random.choice(vehicles)
        user["age"]=random.uniform(16, 85)
        user["gender"]=random.choice(["man","woman"])
        user["weight"]=random.uniform(60, 110)
        user["height"]=random.uniform(150, 210)
        user["bodyfat"]=random.uniform(3, 45)
        user["bloodpressure_sist"]=random.uniform(120, 180)
        user["bloodpressure_diast"]=random.uniform(70, 120)
        user["cholesterol"]=random.uniform(150, 300)
        user["smoker"]=random.choice(["0","1"])
        user["drinking"]=random.uniform(0,7)
        user["disability"]=random.choice(["0","1"])
        user["previouspatology"]=random.choice(["0","1"])
        user["time"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        users[user["id"]]=user

def get_df():
        #Generamos una lista con las claves del diccionario para pode iterar
        claves =users.keys()
        listaclaves=list(claves)

        #Creamos un DataFrame para poder iterar en la función folium

        df = pd.DataFrame()
        df['lat'] = None
        df['lon'] = None
        df['name'] = None

        for i in range (0,USERS_TOTAL):
                a=listaclaves[i]
                df.loc[i+1]=[users[a]['position']['lat'], users[a]['position']['lon'],users[a]['name']]

        return df