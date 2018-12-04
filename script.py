import pandas as pd 

#CONSTANTES
arquivo = "PNE-20-00049_GP.xls"

sheet_name = "PAE_B7 E_2H"

arquivo_temp = "temp.xls"

df = pd.read_excel(arquivo, sheet_name = sheet_name)

df.head()

df_filtered = df.filter(items = ['GRUPO','TIPO'])

df_filtered.head()

rows = []
pointer = 0
for index, line in df_filtered.iterrows(): 
    
    record  = str(line['TIPO'])
    if record == 'nan': 
        try:
            rows.append(rows[pointer - 1])
            df_filtered.loc[index, 'TIPO'] = rows[pointer]
        except: 
            print(rows)
            print(pointer)
    else: 
        rows.append(record)
    
    pointer += 1
    
    df_filtered.head()
print(df_filtered)