import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

df = pd.read_csv("data/processed/clean_credit_data.csv")

conn = mysql.connector.connect(

   # host="mysql",
    host="localhost",
    port=3306,
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS credit_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Age FLOAT,
    Job INT,
    Credit_amount FLOAT,
    Duration INT,
    CreditPerAge FLOAT
)
""")

for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO credit_data (Age, Job, Credit_amount, Duration, CreditPerAge) VALUES (%s, %s, %s, %s, %s)",
        (row['Age'], row['Job'], row['Credit amount'], row['Duration'], row['CreditPerAge'])
    )

conn.commit()
cursor.close()
conn.close()
print("✅ Données chargées dans MySQL")

import mysql.connector

def test_mysql_loaded():
    conn = mysql.connector.connect(
        host="localhost",
        user="credituser",
        password="creditpass",
        database="creditdb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM credit_data")
    count = cursor.fetchone()[0]
    assert count > 0, "Aucune donnée insérée dans MySQL"