import pandas as pd  
excel_file_path = 'specialchr.xlsx'
df = pd.read_excel(excel_file_path)
print(df.head(2))

for column in df.columns:
    df[column] = df[column].str.replace(r'\W','') 
print(df)