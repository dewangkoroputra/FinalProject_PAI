import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# === STEP 1: Load dataset yang sudah diproses ===
df = pd.read_csv("Processed_ZAP_Report.csv")  

# === STEP 2: Tentukan Fitur dan Label untuk Training ===
X = df[['Alert_encoded']]  # Fitur
y = df['Risk_encoded']     # Label

# === STEP 3: Split data menjadi Train dan Test ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === STEP 4: Training menggunakan Random Forest ===
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# === STEP 5: Evaluasi Model ===
y_pred = clf.predict(X_test)

print("Classification Report:")
report = classification_report(y_test, y_pred)
print(report)

# Menyimpan classification report ke file .txt
with open("classification_report.txt", "w") as f:
    f.write(report)

# === STEP 6: Hitung jumlah berdasarkan tingkat risiko ===
risk_counts = df['Risk_encoded'].value_counts()

# Mencetak jumlah risiko berdasarkan kategori
risk_levels = ["Low", "Medium (High)", "High"]  # Sesuaikan dengan encoding yang digunakan
for risk, count in zip(risk_levels, risk_counts):
    print(f"{risk}: {count} kerentanan")

# === STEP 7: Confusion Matrix ===
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()

# === STEP 8: Simpan Model yang sudah dilatih ===
joblib.dump(clf, "rf_model.pkl")  # Menyimpan model
print("Model berhasil disimpan ke file rf_model.pkl")
