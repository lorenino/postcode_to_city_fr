import pandas as pd
import requests

# Fonction pour obtenir la ville à partir du code postal via l'API
def get_city_from_postal_code(postal_code):
    try:
        response = requests.get(f"https://api.zippopotam.us/fr/{postal_code}")
        if response.status_code == 200:
            data = response.json()
            if data['places']:
                return data['places'][0]['place name']
        return "Unknown"
    except Exception as e:
        return "Unknown"

# Charger le fichier Excel fourni
file_path = 'chemin/vers/votre/fichier/import_prospect.xlsx'
df = pd.read_excel(file_path)

# Assurer que la colonne 'Bureau distributeur' existe
if 'Bureau distributeur' not in df.columns:
    df['Bureau distributeur'] = ''

# Appliquer la fonction pour obtenir les villes à partir des codes postaux
df['Bureau distributeur'] = df['Code postal'].apply(get_city_from_postal_code)

# Sauvegarder le résultat dans un nouveau fichier Excel
output_path = 'chemin/vers/votre/fichier/import_prospect_villes.xlsx'
df.to_excel(output_path, index=False)

print(f"Le fichier avec les villes a été créé : {output_path}")
