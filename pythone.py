
import pandas as pd
import re

def ph_use():
  ph = "PH-mock0.xlsx"
  aba = "Roteiros"
  cenario = 4


  df = pd.read_excel(ph, sheet_name=aba)
  t = re.compile(r'rio')
  check = t.findall(df.columns[0])

  if len(check) == 0:
    df = pd.read_excel(ph, sheet_name=aba, header=1)

  if cenario > 0:
    df = df.loc[(df['Cenário']) == cenario] 
  
  print(df)


ph_use()
