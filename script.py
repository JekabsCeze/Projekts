import pandas as pd
import numpy as np

excel_file_path = 'ediens.xlsx'
df = pd.read_excel(excel_file_path)
atlautas_kat = ['Baked Foods', 'Snacks', 'Sweets', 'American Indian', 'Restaurant Foods', 'Meats', 'Fruits']
izv_katego = np.random.choice(atlautas_kat)
izv_katego_df = df[df['Food Group'] == izv_katego]

if izv_katego_df.empty:
    print(f"Kļūda: Nav datu par kategoriju '{izv_katego}'.")
else:

    randomizēts_ēdienu_nosaukums = np.random.choice(izv_katego_df['name'])
    ediena_nosaukums = df[df['name'] == randomizēts_ēdienu_nosaukums]
    nosaukums = ediena_nosaukums['name'].values[0]
    Kalorijas = ediena_nosaukums['Calories'].values[0]
    Proteīns = ediena_nosaukums['Protein (g)'].values[0]
    Cukurs = ediena_nosaukums['Sugars (g)'].values[0]

    print(f"\nIzvēlētais ēdiens: {nosaukums}")
    print(f"Kategorija: {izv_katego}")
    print(f"Kalorijas: {Kalorijas} kcal")
    print(f"Proteīni: {Proteīns} g")
    print(f"Cukurs: {Cukurs} g")
