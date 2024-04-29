# Weather Data Collection Visualization
Un projet réalisé lors de mon Master 1 - Data Engineer avec l'école PMN : Utilisant Flask, MongoDB, Docker et Dash pour visualiser les données météorologiques à partir d'une ApiREST.
Un travail de groupe avec Kemet Bouka Tchamba et Olaf Zannou

![MongoDB logo](https://databasejoe.com/wp-content/uploads/2019/08/mongo-db-logo.png)
![Docker logo](https://www.extraordy.com/wp-content/uploads/2014/08/docker.png)
![Dash logo](https://i0.wp.com/lifewithdata.com/wp-content/uploads/2022/02/plotly_logo-1.jpeg?resize=300%2C95&ssl=1)
![Flask logo](https://th.bing.com/th/id/OIP.p1xsgNl4drd6kZpaHkRNRQAAAA?w=118&h=128&c=7&r=0&o=5&pid=1.7)


## Fichiers
### app 1.py : 
Ce fichier contient le script Python principal qui interroge l'API OpenWeather pour récupérer les données météorologiques d'une ville spécifique. Les données sont ensuite stockées dans une base de données MongoDB.
### weather_rest.py : 
Ce fichier contient un script Python qui utilise Flask pour créer une API REST qui expose les données météorologiques stockées dans la base de données MongoDB. Les utilisateurs peuvent interroger cette API pour obtenir des données météorologiques via des requêtes HTTP.
### weather_dash.py : 
Ce fichier contient un script Python qui utilise Dash pour créer une application de datavisualisation interactive. Les données météorologiques stockées dans la base de données MongoDB sont utilisées pour créer des graphiques et des tableaux de bord interactifs.
### Dockerfile : 
Ce fichier Docker permet de construire une image Docker pour exécuter l'application Python. Il spécifie les dépendances et l'environnement nécessaires pour exécuter l'application.
### docker-compose.yml : 
Ce fichier Docker Compose définit les services nécessaires pour exécuter l'ensemble de l'application, y compris les services Python, MongoDB. 
Il gère également la configuration des conteneurs Docker et des réseaux.
### requirements.txt : 
Ce fichier spécifie les dépendances Python nécessaires pour exécuter l'application.

## Fonctionement : 
### Partie I
1) Assurez-vous d'avoir Docker et Docker Compose et MongoDB installés sur votre système.
2) Clonez ce dépôt sur votre machine locale.
3) Allez sur https://openweathermap.org/ et creéz un compte
4) Allez sur l'onglet "API" : https://openweathermap.org/api et générez une clé API pour ensuite l'insérer à la place de "YOUR API KEY" dans le fichier "app 1.py"
5) Lancez MongoDB Dekstop avec le localhost et le port correspondant
6) Lancez Docker et entrer dans le shell le chemin d'accès correspondant à l'emplacement du dépôt cloné sur vôtre ordinateur :
   ```
   cd /chemin/vers/votre/projet
   ```
   Si il y a des espaces dans le chemin d'accès, mettre des guillemets
   (exemple : "/C/Users/Thomas Dupont/mon_projet_data/")
   Créer l'image avec docker qui va utiliser le fichier docker-compose.yml
   ```
   docker-compose --build
   ```
   Pour vérifier la présence de l'image, entrer dans le shell :
   ```
   docker images
   ```
   
8) Lancer "app 1.py" via le shell ou un IDE (Jupyter Notebook, Pycharm, Visual Studio Code)
9) En allant sur MongoDB vous devez voir apparaître deux dossier : weather et city 

### Partie II
