from flask import Flask, jsonify
import pymongo

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_all_weather():
    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client["meteo_db"]
        collection = db["weather"]
        weather_data = list(collection.find({}))
        for elem in weather_data:
            elem['_id'] = str(elem['_id'])
        return jsonify(weather_data)
    except Exception as e:
        return jsonify({'message': f'Erreur : {str(e)}'}), 500
    finally:
        if client:
            client.close()

@app.route('/weather/<ville>', methods=['GET'])
def get_weather_by_ville(ville):
    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client["meteo_db"]
        collection = db["weather"]
        weather_data = collection.find_one({'ville': ville})
        if weather_data:
            weather_data['_id'] = str(weather_data['_id'])
            return jsonify(weather_data)
        else:
            return jsonify({'message': 'Ville non trouvée'}), 404
    except Exception as e:
        return jsonify({'message': f'Erreur : {str(e)}'}), 500
    finally:
        if client:
            client.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
