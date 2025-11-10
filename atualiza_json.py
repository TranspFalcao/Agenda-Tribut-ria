import pandas as pd
import json

df = pd.read_excel("vencimentos_icms_reinf_novembro_2025.xlsx", engine="openpyxl")
filtered_df = df[(df["Obrigação"].str.contains("ICMS Normal")) & (df["Estado / Tipo"].str.contains("Paraná"))]
vencimentos = filtered_df.apply(lambda row: f"{row['Data de Vencimento']} - {row['Obrigação']} - {row['Estado / Tipo']}", axis=1).tolist()

json_data = {
    "estado": "Paraná",
    "mes": "Novembro",
    "ano": "2025",
    "vencimentos_icms_normal": vencimentos
}

with open("vencimentos_icms_pr_novembro_2025.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)
