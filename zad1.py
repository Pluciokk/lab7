import pandas as pd

data = {'Imie': ['Anna','Jan''Katarzya','Tomasz'],
        'Nazwisko': ['Kowalska', 'Nowak','Ungabunga','Krach'],
        'Nr_albumu': ['w66897','w12345','w66669','w10000'],
        'Wiek': [20,19,21,25],
        'Ocena': [4.5,5.0,3.5,4.0]}
df = pd.DataFrame(data)
#print(df)

print(df[df['Ocena']>4.0])

#b
sort = df.sort_values(by='Wiek')
print(sort)
#c
grupa = df.groupby('Ocena')['Wiek'].mean()
print(grupa)
#d
poprawa = {
    'Nr_albumu': ["w66897", "266669", "w10000"],
    'Oceny_Poprawione': [5.0, 4.5, 5.0]
}

df_poprawa = pd.DataFrame(poprawa)
dff = pd.merge(df, df_poprawa, on='Nr_albumu', how='left')
print(dff)
#e

plik = 'C:\Zadania\lab7\zad.csv'
dff.to_csv(plik, index=False)
df3 = pd.read_csv(plik)
#f
nowy_student = {'Nr_albumu': "w66444", 'Imie': 'Szymon', 'Nazwisko': 'Ząb', 'oceny': 4.0, 'Wiek': 20}
df4 = df.append(nowy_student, ignore_index=True)
print(df3)
#g
oceny = df['Ocena'].unique()
print(oceny)
#h
studenci5 = df[df['Ocena'] == 5].shape[0]
print(studenci5)
