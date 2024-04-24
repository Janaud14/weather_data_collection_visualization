import json
import requests
import pymongo
import os
import time
import logging

API_KEY = 'e5229b3cc815b96126e9db4b7710d755'

def ingest_weather_data():
    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client["meteo_db"]
        collection = db["weather"]

        with open(os.path.join(os.getcwd(), 'city.json'), 'r', encoding='utf-8') as f:
            data = json.load(f)

        villes_fr = [ville for ville in data if ville['country'] == 'FR']
        villes_top100 = sorted(villes_fr, key=lambda x: x['stat']['population'], reverse=True)[:100]

        for ville in villes_top100:
            id_ville = ville['id']
            url = f'http://api.openweathermap.org/data/2.5/weather?id={id_ville}&appid={API_KEY}&units=metric&lang=fr'
            response = requests.get(url)
            data = response.json()
            
            info_ville = {
                "ville": ville['name'],
                "temperature": data['main']['temp'],
                "temperature min": data["main"]["temp_min"],
                "temperature max": data["main"]["temp_max"],
                "description": data['weather'][0]['description'],
                "precipitation": data['rain']['1h'] if 'rain' in data else 0,
                "humidite": data['main']['humidity']
            }
            collection.insert_one(info_ville)
            print(f"{ville['name']} - Succès dans la collecte de données")
            time.sleep(5)

    except Exception as e:
        logging.error(f"Erreur lors de l'ingestion des données : {str(e)}")
    finally:
        if client:
            client.close()

if __name__ == '__main__':
    ingest_weather_data()
