# python-test-de
Repository pour le Python-test-DE project 

## Partie 1 : Python and Data Engineering
Ci-dessous l'arborescence détaillée du projet Python qui répond
aux questions 1 à 5 de la partie 1.
```
python-test-de
+-- conf
    +--global_conf_template.yml
+-- python_test_de
    +-- __init__.py
    +-- constant.py
    +-- main.py
    +-- pipelines.py
    +-- utils.py
+-- sql
    +-- requests.sql
+-- .gitignore
+-- README.md
+-- requirements.txt
```

Question 6 :

Afin de gérer un plus grosse volumétrie de donnée, on peut considérer
le fait d'utiliser le MultiThreading ou MultiProcessing en Python
ou passer sur un framework Hadoop/Spark avec suffisament d'espace de stockage et de RAM pour le 
stockage et le traitement des données ce qui nécessite un recodage en 
Pyspark et la manipulation des Dataset[Row] en lieu et place des
pandas DataFrame.

## Partie 2 : SQL

Les deux requêtes SQL pour cette partie sont contenues
dans le fichier *request.sql* du dossier *sql* du repo.



