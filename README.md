# README - Final Project PAI: Implementasi Machine Learning untuk Klasifikasi Risiko Kerentanan Otomatis dari Hasil Pemindaian OWASP ZAP

## Deskripsi Singkat:
Proyek ini bertujuan untuk **mengotomatisasi klasifikasi tingkat risiko** dari hasil pemindaian keamanan web menggunakan **OWASP ZAP** dengan pendekatan **Machine Learning berbasis Random Forest**. Dataset yang digunakan merupakan hasil **export laporan scanning OWASP Juice Shop**, yang telah diproses dan diklasifikasikan secara otomatis menggunakan model **supervised learning**. Dengan menggunakan pendekatan ini, diharapkan proses **klasifikasi risiko** dapat dilakukan secara lebih cepat, efisien, dan mengurangi ketergantungan pada proses **manual** dalam **penetration testing** aplikasi web.

---

## Struktur Folder & Penjelasan File:


### 1. **Dataset/**
- **`Parsed_ZAP_Report.csv`**  
  → Dataset hasil export dari ZAP report (.json) yang telah diparsing dan siap digunakan untuk training model.

### 2. **Script/**
- **`convert_json.py`**  
  → Script untuk **mengonversi hasil pemindaian ZAP (JSON)** menjadi format **CSV** yang lebih mudah diproses dan digunakan dalam model.
  
- **`preprocessing.py`**  
  → Script untuk **preprocessing** data, termasuk **membersihkan data**, **label encoding** kolom `Alert` dan `Risk Level`, serta menyimpan dataset yang sudah diproses ke file **`Processed_ZAP_Report.csv`**.

- **`model_training.py`**  
  → Script untuk **training model Random Forest Classifier**, evaluasi model (classification report, confusion matrix), dan **menyimpan model** (`rf_model.pkl`) yang telah dilatih.

- **`classification_report.txt`**  
  → Output **evaluasi model** yang berisi **classification report** (precision, recall, f1-score).

- **`rf_model.pkl`**  
  → Model Machine Learning yang sudah dilatih dan disimpan agar bisa digunakan ulang untuk prediksi baru.

### 3. **Gambar/**
- **`Figure_1.png`**  
  → **Confusion matrix** hasil visualisasi performa model terhadap data testing.

### 4. **Dokumentasi Tools/**
- **`Screenshots Terminal Tools`**  
  → Bukti bahwa semua tools seperti **Python**, **pip**, **Jupyter**, **Docker**, dll sudah terinstal di **host lokal** untuk menjalankan proyek ini.

---

## 🛠️ Cara Menjalankan:

### 1. **Jalankan Docker + Juice Shop:**
- Pastikan Docker Desktop berjalan, lalu jalankan perintah di terminal:
  ```bash
  docker run -d -p 3000:3000 bkimminich/juice-shop
  ```
  Ini akan menjalankan OWASP Juice Shop di http://localhost:3000. Kemudian lakukan pemindaian menggunakan aplikasi ZAP, export reportnya dengan format json, dan jalankan `convert_json.py`.

### 2. **Preprocessing Data:**
Setelah itu, jalankan script `preprocessing.py` untuk memproses data hasil pemindaian ZAP:
```bash
python preprocessing.py
```
Data yang sudah diproses akan disimpan dalam `Processed_ZAP_Report.csv` dan encoder akan disimpan sebagai `alert_encoder.pkl` dan `risk_encoder.pkl`.

### 3. **Training Model:**
Setelah data diproses, jalankan `model_training.py` untuk melatih model:
```bash
python model_training.py
```
Model Random Forest akan dilatih, dan hasil evaluasi akan disimpan dalam `classification_report.txt` serta confusion matrix disimpan dalam `Figure_1.png`.

### Contoh Output:
- **`classification_report.txt`**: Berisi hasil evaluasi model seperti precision, recall, f1-score, dan accuracy.
- **`Figure_1.png`**: Visualisasi confusion matrix.
- **`rf_model.pkl`**: File model yang sudah dilatih, siap digunakan untuk prediksi selanjutnya.
