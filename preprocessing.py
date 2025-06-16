import pandas as pd
from sklearn.preprocessing import LabelEncoder

# === STEP 1: Load dataset ZAP ===
df = pd.read_csv("Parsed_ZAP_Report.csv") 

# === STEP 2: Bersihkan data ===
df.dropna(inplace=True)

# === STEP 3: Encode kolom kategorikal ke angka ===
alert_encoder = LabelEncoder()
df['Alert_encoded'] = alert_encoder.fit_transform(df['Alert'])

risk_encoder = LabelEncoder()
df['Risk_encoded'] = risk_encoder.fit_transform(df['Risk Level'])

# === STEP 4: Simpan dataset yang sudah diproses ===
df.to_csv("Processed_ZAP_Report.csv", index=False)

# === SIMPAN ENCODER ===
import joblib
joblib.dump(alert_encoder, "alert_encoder.pkl")
joblib.dump(risk_encoder, "risk_encoder.pkl")

print("Preprocessing selesai, file sudah diproses dan disimpan.")