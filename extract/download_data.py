import os
from dotenv import load_dotenv

load_dotenv()

# Authentification Kaggle via variables d’environnement
os.environ['KAGGLE_USERNAME'] = os.getenv("KAGGLE_USERNAME")
os.environ['KAGGLE_KEY'] = os.getenv("KAGGLE_KEY")

os.system("kaggle datasets download -d uciml/german-credit -p data/raw --unzip")
print(" Dataset téléchargé dans data/raw/")