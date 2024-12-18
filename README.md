# Microservices Project

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

### Étape 1 : Docker compose
```bash
docker-compose up --build
```

### Étape 2 : Test
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

## Result volume : 
<!-- Persistence doesn't work.
     If you delete the pods and keep the volume the data is still missing
     Probably some issue with the app itself.
 -->
```bash ─$ sudo docker volume ls     
[sudo] password for momoo: 
DRIVER    VOLUME NAME
local     data
local     microservices_project_chunk_data
local     todos_data
```
```bash
sudo cat /var/lib/docker/volumes/microservices_project_chunk_data/_data/checksums.json  

[sudo] password for momoo: 
[{"input": "test-data", "algorithm": "sha256", "checksum": "a186000422feab857329c684e9fe91412b1a5db084100b37a98cfc95b62aa867"}, {"input": "test-data", "algorithm": "sha256", "checksum": "a186000422feab857329c684e9fe91412b1a5db084100b37a98cfc95b62aa867"}, {"input": "test-data", "algorithm": "sha256", "checksum": "a186000422feab857329c684e9fe91412b1a5db084100b37a98cfc95b62aa867"}]  
``` 
## Pousser l'Image Docker vers GHCR

```bash ┌──(momoo㉿momoo)-[~/Downloads/microservices_project]
└─$ docker push ghcr.io/mondataa/docker-micros:latest

The push refers to repository [ghcr.io/mondataa/docker-micros]
ed8c59133961: Pushed 
6f7b2c706857: Pushed 
4794d08a470f: Pushed 
a3fbd0155aea: Pushed 
fe5bbd4f8a42: Pushed 
24f0c2413cd7: Pushed 
8f9a13bfb118: Pushed 
0aeeeb7c293d: Pushed 
c81d4fdb67fc: Pushed 
0e82d78b3ea1: Pushed 
301c1bb42cc0: Pushed 
latest: digest: sha256:60999f5001fdaf61316956a13c4c5500dcb0266bcaba3a4a9264183a31cabc59 size: 2628
```
