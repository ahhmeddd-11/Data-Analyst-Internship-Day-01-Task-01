import pandas as pd
import os

df = pd.read_csv("medical-dataset.csv")

df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace("-", "_")

df = df.drop_duplicates()

df = df.dropna()

if 'gender' in df.columns:
    df['gender'] = df['gender'].str.upper()

if 'no_show' in df.columns:
    df['no_show'] = df['no_show'].str.upper()

if 'scheduledday' in df.columns:
    df['scheduledday'] = pd.to_datetime(df['scheduledday'], errors='coerce')

if 'appointmentday' in df.columns:
    df['appointmentday'] = pd.to_datetime(df['appointmentday'], errors='coerce')

if 'age' in df.columns:
    df = df[df['age'] >= 0]
    df['age'] = df['age'].astype(int)

os.makedirs("cleaned_data", exist_ok=True)
df.to_csv("cleaned_data/cleaned_medical_appointments.csv", index=False)

print("Cleaning done. Cleaned file saved as cleaned_data/cleaned_medical_appointments.csv")
