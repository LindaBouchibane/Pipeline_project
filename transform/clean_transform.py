import pandas as pd
import os

df = pd.read_csv("data/raw/german_credit_data.csv", index_col=0)

# One-hot encoding + feature engineering
df = pd.get_dummies(df, columns=['Sex', 'Housing', 'Saving accounts', 'Checking account', 'Purpose'], drop_first=True)
df['CreditPerAge'] = df['Credit amount'] / df['Age']

os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/clean_credit_data.csv", index=False)
print("✅ Données nettoyées et enregistrées")

def test_processed_data_exists():
    assert os.path.exists('data/processed/clean_credit_data.csv'), "Fichier transformé manquant."