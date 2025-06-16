import json
import pandas as pd

# Load file JSON ZAP
with open("zap-report.json") as f:
    data = json.load(f)

# Ambil alert-item
alerts = data.get('site', [])[0].get('alerts', [])

# Parse jadi list
records = []
for alert in alerts:
    for instance in alert.get('instances', []):
        records.append({
            'Alert': alert.get('name'),
            'Risk Level': alert.get('riskdesc'),
            'CWE ID': alert.get('cweid'),
            'URL': instance.get('uri')
        })

# Simpan ke CSV
df = pd.DataFrame(records)
df.to_csv("Parsed_ZAP_Report.csv", index=False)

print("Data berhasil diproses dan disimpan ke 'Parsed_ZAP_Report.csv'")
