import customtkinter
import tkinter as tk
from PIL import Image, ImageTk
import os
import mysql.connector

class ArbreGenealogique(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Arbre Généalogique")
        self.geometry("1000x900")

        # Configuration des grilles
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Barre de recherche
        self.search_frame = customtkinter.CTkFrame(self)
        self.search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.search_entry = customtkinter.CTkEntry(self.search_frame, width=180)
        self.search_entry.grid(row=0, column=0, padx=10, pady=5)
        self.search_button = customtkinter.CTkButton(self.search_frame, text="Rechercher", command=self.rechercher_personne)
        self.search_button.grid(row=0, column=1, padx=10, pady=5)
        
        # Création du canvas pour dessiner l'arbre
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.grid(row=1, column=0, sticky="nsew")

        # Connexion à la base de données
        self.conn = mysql.connector.connect(
            host="votre_hote",
            user="votre_utilisateur",
            password="votre_mot_de_passe",
            database="arbre_genealogique"
        )
        self.cursor = self.conn.cursor()

        self.images = {}  # Stocker les images d'avatar
        self.charger_donnees_depuis_bdd()
        self.dessiner_arbre()

    def charger_donnees_depuis_bdd(self):
        self.donnees = {"Grand-parents": [], "Parents": [], "Enfants": []}
        self.cursor.execute("SELECT nom, infos, avatar, generation FROM personnes")
        resultats = self.cursor.fetchall()
        for resultat in resultats:
            nom, infos, avatar, generation = resultat
            self.donnees[generation].append({"nom": nom, "infos": infos, "avatar": avatar})

    # ... (le reste du code reste similaire)
    
    #Connexion à la base de données : Remplacez "votre_hote",
    # "votre_utilisateur" et "votre_mot_de_passe" par les informations de connexion de votre base de données.
    #Chargement des données : La fonction charger_donnees_depuis_bdd récupère les données de la table personnes et 
    #les organise dans le dictionnaire self.donnees.
    #Dessin de l'arbre : La fonction dessiner_arbre utilise maintenant les données chargées depuis la base de données.
    #
    #
    
    #ajoute de nouveau personnage
    def ajouter_personne(self, nom, infos, avatar, generation):
        sql = "INSERT INTO personnes (nom, infos, avatar, generation) VALUES (%s, %s, %s, %s)"
        val = (nom, infos, avatar, generation)
        self.cursor.execute(sql, val)
        self.conn.commit()
        self.charger_donnees_depuis_bdd()
        self.dessiner_arbre()

if __name__ == "__main__":
    app = ArbreGenealogique()
    app.mainloop()