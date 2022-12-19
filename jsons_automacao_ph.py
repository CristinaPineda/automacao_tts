import pandas as pd
import re
import json


def ph_use():
# Coloque como valor das variaveis o seu PH inserido na pasta do script
  ph = "PH-mock0.xlsx"
  aba = "Roteiros"
# Escolha o cenário 
  cenario = 2


#Verifica linha vazia
  df = pd.read_excel(ph, sheet_name=aba)
  t = re.compile(r"rio")
  check = t.findall(df.columns[0])

  if len(check) == 0:
    df = pd.read_excel(ph, sheet_name=aba, header=1)

# Verifica se a cenário específico
  if cenario > 0:
    df2 = df.loc[(df['Cenário']) == cenario].reset_index(drop=True)
  else:
    df2 = df
  
# Array de transtypes
  array_transtypes = []
  df_iterator = 0
  while df_iterator < df2.shape[0]:
    objeto = {
      "cenário": "ph",
      "ação" : "incluir",
      "transtypes": {
        "transtype": df2["Transtype"].iloc[df_iterator],
        "conta débito": str(df2["conta debito"].iloc[df_iterator]),
        "conta crédito": str(df2["conta crédito"].iloc[df_iterator])
      }
    }
    array_transtypes.append(objeto)
    df_iterator += 1

    def json_tts(lista):
      with open('transtypes_arquivo.json', 'w', encoding='utf8') as f:
        json.dump(lista, f, ensure_ascii=False)
    
    json_tts(array_transtypes)
  

ph_use()
