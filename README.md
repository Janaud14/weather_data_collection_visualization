# Weather Data Collection Visualization
Un projet réalisé lors de mon Master 1 - Data Engineer avec l'école PMN : Utilisant Flask, MongoDB, Docker et Dash pour visualiser les données météorologiques à partir d'une ApiREST.
Un travail de groupe avec Kemet Bouka Tchamba et Olaf Zannou

## Fonctionnement
### App.py : 
Ce fichier contient le script Python principal qui interroge l'API OpenWeather pour récupérer les données météorologiques d'une ville spécifique. Les données sont ensuite stockées dans une base de données MongoDB.
### weather_rest.py : 
Ce fichier contient un script Python qui utilise Flask pour créer une API REST qui expose les données météorologiques stockées dans la base de données MongoDB. Les utilisateurs peuvent interroger cette API pour obtenir des données météorologiques via des requêtes HTTP.
### weather_dash : 
Ce fichier contient un script Python qui utilise Dash pour créer une application de datavisualisation interactive. Les données météorologiques stockées dans la base de données MongoDB sont utilisées pour créer des graphiques et des tableaux de bord interactifs.
### Dockerfile : 
Ce fichier Docker permet de construire une image Docker pour exécuter l'application Python. Il spécifie les dépendances et l'environnement nécessaires pour exécuter l'application.
### docker-compose.yml : 
Ce fichier Docker Compose définit les services nécessaires pour exécuter l'ensemble de l'application, y compris les services Python, MongoDB. 
Il gère également la configuration des conteneurs Docker et des réseaux.
### requirements.txt : 
Ce fichier spécifie les dépendances Python nécessaires pour exécuter l'application.
