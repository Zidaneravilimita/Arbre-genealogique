from api import DatabaseManager

# Connexion à la base
db = DatabaseManager()

# Vérifie la connexion
if not db.cursor:
    print("Impossible de se connecter à la base.")
    exit()

# Données par table
donnees = {
    "grand_parents": [
        ("Mariette", 78, "Mère de Mana", "avatar_mere.png"),
        ("Motherland", 80, "Père de Mana", "avatar_homme.png")
    ],
    "parents": [
        ("Mana Thomas", 52, "Père de Zidane et Juana", "avatar_homme.png"),
        ("Sidonie", 48, "Mère de Zidane et Juana", "avatar_mere.png")
    ],
    "oncle1_tante1": [
        ("Tambou", 47, "Père de Echa et Iliman", "avatar_homme.png"),
        ("Felana", 45, "Mère de Echa et Iliman", "avatar_mere_2.png")
    ],
    "oncle2_tante2": [
        ("Parally", 53, "Père de Dinot et Cheria", "avatar_homme.png"),
        ("Niry", 50, "Mère de Dinot et Cheria", "avatar_mere.png")
    ],
    "cousine_2_3": [
        ("Echa", 12, "Fille de Felana et Tambou", "avatar_fille_2.png"),
        ("Iliman", 6, "Fils de Felana et Tambou", "avatar_boy.png")
    ],
    "cousine_1_cousin_1": [
        ("Dinot", 18, "Fils de Niry et Parally", "avatar_boy.png"),
        ("Cheria", 21, "Fille de Niry et Parally", "avatar_fille_1.png")
    ],
    "moi_et_ma_soeur": [
        ("Zidane", 22, "Fils de Mana et Sidonie", "avatar_boy.png"),
        ("Juana", 18, "Fille de Mana et Sidonie", "avatar_fille_2.png")
    ]
}

# Insertion des données
for table, personnes in donnees.items():
    for nom, age, infos, avatar in personnes:
        try:
            requete = f"INSERT INTO {table} (nom, age, infos, avatar) VALUES (%s, %s, %s, %s)"
            db.cursor.execute(requete, (nom, age, infos, avatar))
            db.conn.commit()
            print(f"{nom} ajouté dans {table}")
        except Exception as e:
            print(f"Erreur pour {nom} dans {table} :", e)

print("Ajout terminé.")
