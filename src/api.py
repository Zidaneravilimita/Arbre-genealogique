import mysql.connector

class DatabaseManager:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  
                database="arbre_g"  
            )
            self.cursor = self.conn.cursor(dictionary=True)
            print("Connexion réussie à la base de données")
        except mysql.connector.Error as e:
            print("Erreur de connexion à la base de données:", e)
            self.conn = None
            self.cursor = None

    def recuperer_toutes_les_donnees(self):
        if not self.cursor:
            return []
        tables = [
            "grand_parents",
            "parents",
            "oncle1_tante1",
            "oncle2_tante2",
            "cousine_1_cousin_1",
            "cousine_2_3",
            "moi_et_ma_soeur"
        ]
        toutes_les_donnees = []
        for table in tables:
            try:
                self.cursor.execute(f"SELECT *, '{table}' as table_source FROM {table}")
                donnees = self.cursor.fetchall()
                toutes_les_donnees.extend(donnees)
            except mysql.connector.Error as e:
                print(f"Erreur lors de la récupération depuis la table {table} :", e)
        return toutes_les_donnees
