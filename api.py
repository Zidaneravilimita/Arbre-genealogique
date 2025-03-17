import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self, host="localhost", user="root", password="", database="arbre_genealogique"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = self.connecter()

    def connecter(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            conn.commit()
            conn.close()
            
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if conn.is_connected():
                print("Connexion réussie à la base de données")
            return conn
        except Error as e:
            print(f"Erreur de connexion à la base de données: {e}")
            return None

    def ajouter_personne(self, nom, infos, avatar, generation):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO personnes (nom, infos, avatar, generation) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nom, infos, avatar, generation))
            self.connection.commit()
            print("Personne ajoutée avec succès")
        except Error as e:
            print(f"Erreur lors de l'ajout : {e}")

    def rechercher_personne(self, nom):
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM personnes WHERE nom LIKE %s"
            cursor.execute(query, ("%" + nom + "%",))
            return cursor.fetchall()
        except Error as e:
            print(f"Erreur lors de la recherche : {e}")
            return []

    def supprimer_personne(self, nom):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM personnes WHERE nom = %s"
            cursor.execute(query, (nom,))
            self.connection.commit()
            print("Personne supprimée avec succès")
        except Error as e:
            print(f"Erreur lors de la suppression : {e}")

    def recuperer_donnees(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM personnes"
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Erreur lors de la récupération : {e}")
            return []

    def fermer_connexion(self):
        if self.connection:
            self.connection.close()
            print("Connexion fermée")

# Exemple d'utilisation
if __name__ == "__main__":
    db = DatabaseManager()
    db.ajouter_personne("Test Nom", "Test Infos", "avatar_test.png", "Enfants")
    personnes = db.rechercher_personne("Test")
    print(personnes)
    db.fermer_connexion()
