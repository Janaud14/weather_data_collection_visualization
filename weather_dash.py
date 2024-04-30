import dash
from dash import dcc
from dash import html
import requests

# Instancier l'application Dash
app = dash.Dash(__name__)

# Consommer l'API REST pour récupérer les données
response = requests.get('http://localhost:8080/weather')
weather_data = response.json()

# Extraction des noms des villes et de la température associée
cities = [data['ville'] for data in weather_data]
temperatures = [data['temperature'] for data in weather_data]

# Mise en page de l'application
app.layout = html.Div(children=[
    html.H1('Visualisation des données météorologiques'),

    dcc.Graph(
        id='weather-graph',
        figure={
            'data': [
                {'x': cities, 'y': temperatures, 'type': 'bar', 'name': 'Température'},
            ],
            'layout': {
                'title': 'Températures par ville'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
