# Microservices Project

## Description
Ce projet implémente une architecture basée sur des microservices pour fournir différentes fonctionnalités indépendantes. Chaque microservice est contenu dans son propre dossier avec ses propres dépendances et configurations Docker. Ce projet utilise Docker et Docker Compose pour une orchestration simplifiée.

### Microservices inclus :
- **API Gateway** : Point d'entrée unique pour acheminer les requêtes vers les microservices appropriés.
- **Checksum Service** : Gère la génération et la vérification des checksums pour les fichiers.
- **Database Service** : Fournit un stockage centralisé pour les métadonnées.
- **Chunks Service** : Gère la division et l'agrégation des fragments de fichiers.

---

## Structure du Projet
Voici la structure des fichiers et dossiers du projet :


---

## Prérequis
Avant de commencer, assurez-vous d'avoir les outils suivants installés sur votre machine :
- **Docker** : [Télécharger Docker](https://www.docker.com/get-started)
- **Docker Compose** : [Documentation Docker Compose](https://docs.docker.com/compose/install/)
- **Python 3.9+** : Requis si vous souhaitez exécuter localement certains services.

---

## Installation et Lancement

### Étape 1 : Cloner le dépôt
```bash
git clone https://github.com/MonDataa/docker_micros.git
cd microservices_project ```
