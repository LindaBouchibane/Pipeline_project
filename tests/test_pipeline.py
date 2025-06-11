import pandas as pd

def test_credit_data_valid():
    df = pd.read_csv("data/processed/clean_credit_data.csv")
    assert not df.isnull().values.any(), "❌ Null values trouvés"
    assert 'CreditPerAge' in df.columns, "❌ Colonne CreditPerAge manquante"
    assert len(df) > 0, "❌ DataFrame vide"