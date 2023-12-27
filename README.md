# LinkedInAutoConnectBot

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-3.141.0-brightgreen)

## Table de Matière

- [Introduction](#introduction)
- [Installation](#installation)
- [Technologies](#technologies)
- [Utilisation](#utilisation)
- [Contributions](#contributions)
- [Licence](#licence)

Prérequis
Avant d'exécuter ce script, assurez-vous d'avoir installé les dépendances suivantes :

Python (version recommandée : Python 3.x)
Selenium (pour automatiser le navigateur web)
Chromedriver (pour contrôler Google Chrome)
Configuration
Créez un fichier personal_infos.py contenant vos informations personnelles, comme suit :

email = "votre_email@gmail.com"
password = "votre_mot_de_passe"
phone_number = "votre_numéro_de_téléphone"
Assurez-vous d'avoir Google Chrome installé sur votre système.

Utilisation
Exécutez le script en utilisant la commande suivante :

python main.py
Le script ouvrira un navigateur Chrome, se connectera à votre compte LinkedIn, effectuera une recherche d'emplois, et postulera automatiquement à ces emplois.

Si un CAPTCHA est présenté, résolvez-le manuellement dans le navigateur, puis appuyez sur "Enter" dans la console pour continuer.

Le script continuera à parcourir les offres d'emploi et à postuler automatiquement jusqu'à ce qu'il n'y ait plus d'offres correspondant aux critères.

Remarques
Pour des raisons de sécurité, assurez-vous que vos informations de connexion LinkedIn sont correctes et que vous utilisez ce script conformément aux politiques de LinkedIn.

Vous pouvez personnaliser les critères de recherche en modifiant l'URL dans la section driver.get() du script.

Ce script a été conçu à des fins éducatives et de démonstration. L'utilisation abusive de l'automatisation sur LinkedIn peut entraîner la suspension de votre compte.

 ## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request pour des améliorations ou des corrections.

## Licence

Ce projet est sous licence [MIT](LICENSE).
