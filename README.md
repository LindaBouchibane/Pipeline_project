# README.md — Pipeline_Project

![Docker](https://img.shields.io/badge/docker-ready-blue)
![Jenkins](https://img.shields.io/badge/jenkins-ci%2Fcd-green)
![Python](https://img.shields.io/badge/python-3.10-blue)

---

##  Objectif
Ce projet met en œuvre un pipeline de traitement de données financières (crédit) à l’aide des outils suivants :

-  **ETL complet** (Extract → Transform → Load)
-  **Docker** & **Docker Compose**
-  **MinIO** (Data Lake)
-  * MySQL** (stockage structuré)
-  **Jenkins** (CI/CD pipeline)
-  **Pytest** pour les tests automatisés

---

##  Lancement rapide
```bash
git clone https://github.com/ton-utilisateur/Pipeline_Project.git
cd Pipeline_Project
docker-compose up --build
```

- Jenkins : http://localhost:8081  → interface CI
![Jenkins Build](http://localhost:8081/buildStatus/icon?job=Project_pipeline)
- phpMyAdmin : http://localhost:8082  → base MySQL
- Streamlit : http://localhost:8501  → tableau de bord

---

##  Tests automatisés avec Jenkins
Dans Jenkins :
1. Créer un Pipeline
2. Ajouter le repo GitHub
3. Associer le `Jenkinsfile`
4. Jenkins exécute automatiquement :
   -  Extraction Kaggle
   -  Nettoyage Pandas
   -  Tests (`pytest`)
   -  Chargement PostgreSQL / MySQL

Extrait dans `Jenkinsfile` :
```groovy
stage('Test') {
  steps {
    sh 'docker-compose run --rm app pytest tests/test_pipeline.py'
  }
}
```

---


Done
---
