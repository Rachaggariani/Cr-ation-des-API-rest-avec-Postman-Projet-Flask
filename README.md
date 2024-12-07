Instructions pour exécuter le projet: Pour faire fonctionner ce projet Flask, veuillez suivre les étapes suivantes :
1. Créer un environnement virtuel
Exécutez la commande suivante pour créer un environnement virtuel Python : python -m venv monenvapp2
2. Activer l'environnement virtuel
Une fois l'environnement créé, activez-le avec la commande suivante : .monenvapp2\Scripts\activate
3. Installer : pip install -r requirements.txt
4. Installer les bibliothèques nécessaires
Installez les dépendances du projet en exécutant les commandes suivantes :
  pip install Flask
  pip install flask_migrate
  pip install passlib
  pip install jinja2
  pip install flask-bootstrap
  pip install bcrypt
  pip install flask-restful
Remarque :
-Si l'une des bibliothèques rencontre un problème d'installation, essayez d'abord de la désinstaller puis de la réinstaller :

  pip uninstall monenvapp3
  python -m venv monenvapp3

-Si vous rencontrez une erreur de permission lors de l'installation de la bibliothèque "  pip install flask-bootstrap
", suivez les étapes ci-dessous :
1. Purgez le cache de pip avec la commande : pip cache purge
2. Ensuite, réinstallez la bibliothèque en spécifiant le répertoire du cache :
pip install Flask-Bootstrap --cache-dir <chemin_vers_votre_répertoire_de_cache-flask_bootstrap>
-Si vous rencontrez une erreur lors du l'installation de ce fihcier requirements.txt
tu peut installer le contenu de ce fichier un par un :
pip install flask-SqlAlchemy 
pip install flask-Migrate
pip install flask-pymysql
pip install passlib
Pour démarrer le projet, utilisez l'une des commandes suivantes :
flask run ou bien app.py

Ce projet implémente les méthodes HTTP suivantes : GET, POST, PUT, PATCH, et DELETE, permettant de gérer les opérations CRUD (Create, Read, Update, Delete).

