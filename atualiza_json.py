import pandas as pd
import json

df = pd.read_excel("vencimentos_icms_reinf_novembro_2025.xlsx", engine="openpyxl")

df_pr = df[(df["Obrigação"].str.contains("ICMS Normal", na=False)) &
           (df["Estado / Tipo"].str.contains("Paraná", na=False))]

vencimentos_pr = df_pr.apply(
    lambda linha: f"{linha['Data de Vencimento']} - {linha['Obrigação']} - {linha['Estado / Tipo']}",
    axis=1
).tolist()

dados_json = {
    "estado": "Paraná",
    "mes": "Novembro",
    "ano": "2025",
    "vencimentos_icms_normal": vencimentos_pr
}

with open("vencimentos_icms_pr_novembro_2025.json", "w", encoding="utf-8") as f:
    json.dump(dados_json, f, ensure_ascii=False, indent=2)
