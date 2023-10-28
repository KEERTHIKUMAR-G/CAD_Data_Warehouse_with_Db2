import pandas as pd
df= pd.read_csv('C:\Program Files\db\diabetes_dataset.csv')
df.dropna(inplace=True)
import mysql.connector

conn = mysql.connector.connect(
    host='local',
    user='root',
    password='Rasika@2004',
    database='diabetes_data'
)

cursor = conn.cursor()


create_table_query = "CREATE TABLE diabetes_pred (Pregnancies INT,Glucose INT,BloodPressure INT,SkinThickness INT,Insulin INT,BMI float,DiabetesPedigreeFunction float,Age INT,Outcome BINARY);"


cursor.execute(create_table_query)


for index, row in df.iterrows():
    cursor.execute("INSERT INTO diabetes_pred (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction,Age,Outcome) VALUES (%s, %s, %s, %s,%s, %s,%s, %s,%s);"
    ,(row['Pregnancies'], row['Glucose'], row['BloodPressure'], row['SkinThickness'], row['Insulin'], row['BMI'], row['DiabetesPedigreeFunction'], row['Age'], row['Outcome']))


conn.commit()
conn.close()


