# Microservices Project

## Description
Ce projet implémente une architecture basée sur des microservices pour fournir différentes fonctionnalités indépendantes. Chaque microservice est contenu dans son propre dossier avec ses propres dépendances et configurations Docker. Ce projet utilise Docker et Docker Compose pour une orchestration simplifiée.

### Microservices inclus :
- **API Gateway** : Point d'entrée unique pour acheminer les requêtes vers les microservices appropriés.
- **Checksum Service** : Gère la génération et la vérification des checksums pour les fichiers.
- **Database Service** : Fournit un stockage centralisé pour les métadonnées.
---

## Structure du Projet
Voici la structure des fichiers et dossiers du projet :


---

## Prérequis
- **Docker** 
- **Docker Compose** 
- **Python 3.9+** 

---

## Installation et Lancement

### Étape 1 : Cloner le dépôt
```bash
git clone https://github.com/MonDataa/docker_micros.git
cd microservices_project
```

### Étape 2 : Docker compose
```bash
docker-compose up --build
```

### Étape 3 : Test
```bash 
curl -X POST -H "Content-Type: application/json" \
    -d '{"input_string": "test-data", "algorithm": "sha256"}' \
    http://localhost:5001/checksum

curl -X GET http://localhost:5001/list-checksums

curl -X POST -H "Content-Type: application/json" \
     -d '{"string": "test-string", "checksum": "ffe65f1d98fafedea3514adc956c8ada5980c6c5d2552fd61f48401aefd5c00e"}' \
     http://localhost:5006/save-checksum

curl -X POST -H "Content-Type: application/json" -d '{"string": "example", "checksum": "123456"}' http://localhost:5006/save-checksum

curl -X GET http://localhost:5005/list-checksums 
```
