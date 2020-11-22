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
    +-- test
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
Les data pipelines sont codés dans le module *pipelines.py*. Il contient 
des pipelines destinées à:

1 - Lire et structurer les données sources dans un dataframe pandas (Les données médicaments et les données d'articles)

2 - Récupérer les mentions des médicaments dans les articles pubmed et clinical_trials

3 - Générer un json représentant le graphe de liaison entre les médicaments, leurs mentions dans les articles et dans les journaux.

Le script principal va contenir donc l'application de la pipeline numéro 3 à partir d'un fichier de configuration.
Puis appliquer la feature de la question 4.

Pour lancer le code :
- Faire un clone du repo depuis git
- Récupérer les datas (je ne les ai pas mis sur le repo ne connaissant pas le niveau de confidentialité).
- Compléter le fichier de configuration global_config_template.yml avec les bons paths
- Dans un IDE, compléter les configurations de Run du code (Ne pas oublier le ou les arguments, en l'occurence ici le fichier de configuration) et lancer le code si toutes les étapes précédentes sont vérifiées.
- Dans une console Windows ou linux, se placer à la racine du repo puis lancer la commande *python python_test_de/main.py --global_config_file_path conf/global_conf.yml*. Sous un virtual env Python, penser à activer le virtual env avec la commande *source activate my_env*.
Autre méthode => Créer à la racine un script shell qui contient la commande d'activation du script python ainsi que la commande Python et qui va prendre en argument également le fichier de configuration puis lancer le script shell => ./myscript.sh conf/global_conf.yml. Ce script et cette commande peuvent être également utilisés pour ordonnancer le traitement avec un BashOperator dans un DAG Airflow.

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



