import pandas as pd

def test_credit_data_valid():
    df = pd.read_csv("data/processed/clean_credit_data.csv")
    assert not df.isnull().values.any(), "❌ Null values trouvés"
    assert 'CreditPerAge' in df.columns, "❌ Colonne CreditPerAge manquante"
    assert len(df) > 0, "❌ DataFrame vide"


import os
def test_raw_file_exists():
    assert os.path.exists('./data/raw/raw_data.csv'), "raw_data.csv introuvable"
def test_processed_file_exists():
    assert os.path.exists('./data/processed/clean_credit_data.csv'), "clean_credit_data.csv introuvable"