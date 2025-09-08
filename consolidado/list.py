import os
from openpyxl import Workbook

# Pega a pasta onde o script está
script_dir = os.path.dirname(os.path.abspath(__file__))

# Cria a planilha
wb = Workbook()
ws = wb.active
ws.title = "Imagens"

# Cabeçalho
ws.append(["Arquivo"])

# Percorre os arquivos na pasta
for filename in os.listdir(script_dir):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        ws.append([filename])

# Salva o Excel
output_file = os.path.join(script_dir, "lista_imagens.xlsx")
wb.save(output_file)

print(f"✅ Arquivo Excel gerado: {output_file}")