import customtkinter
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class ArbreGenealogique(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Arbre Généalogique")
        self.geometry("1000x900")

        # Centrage de la barre de recherche
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Barre de recherche centrée
        self.search_frame = customtkinter.CTkFrame(self)
        self.search_frame.grid(row=0, column=0, pady=10)
        
        self.search_entry = customtkinter.CTkEntry(self.search_frame, width=250)
        self.search_entry.grid(row=0, column=0, padx=10)
        
        self.search_button = customtkinter.CTkButton(self.search_frame, text="Rechercher", command=self.rechercher_personne)
        self.search_button.grid(row=0, column=1, padx=10)

        # Création du canvas pour dessiner l'arbre
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.grid(row=1, column=0, sticky="nsew")

        # Données de l'arbre généalogique
        self.donnees = {
            "Grand-parents": [
                {"nom": "Mariette", "infos": "Mère de Mana", "avatar": "avatar_mere.png"},
                {"nom": "Motherland", "infos": "Père de Mana", "avatar": "avatar_homme.png"}
            ],
            "Parents": [
                {"nom": "Mana Thomas", "infos": "Père de Zidane et Juana", "avatar": "avatar_homme.png"},
                {"nom": "Sidonie", "infos": "Mère de Zidane et Juana", "avatar": "avatar_mere.png"},
                {"nom": "Felana", "infos": "Mère de Echa et Iliman", "avatar": "avatar_mere_2.png"},
                {"nom": "Tambou", "infos": "Père de Echa et Iliman", "avatar": "avatar_homme.png"},
                {"nom": "Niry", "infos": "Mère de Dinot et Cheria", "avatar": "avatar_mere.png"},
                {"nom": "Parally", "infos": "Père de Dinot et Cheria", "avatar": "avatar_homme.png"}
            ],
            "Enfants": [
                {"nom": "Juana", "infos": "Fille de Mana et Sidonie", "avatar": "avatar_fille_2.png"},
                {"nom": "Zidane", "infos": "Fils de Mana et Sidonie", "avatar": "avatar_boy.png"},
                {"nom": "Iliman", "infos": "Fils de Felana et Tambou", "avatar": "avatar_boy.png"},
                {"nom": "Echa", "infos": "Fille de Felana et Tambou", "avatar": "avatar_fille_2.png"},
                {"nom": "Dinot", "infos": "Fils de Niry et Parally", "avatar": "avatar_boy.png"},
                {"nom": "Cheria", "infos": "Fille de Niry et Parally", "avatar": "avatar_fille_1.png"}
            ]
        }

        self.images = {}  # Stocker les images d'avatar
        self.dessiner_arbre()

    def charger_image(self, chemin):
        try:
            chemin_complet = os.path.join("images", chemin)
            image = Image.open(chemin_complet).resize((80, 80), Image.LANCZOS)
            return ImageTk.PhotoImage(image)
        except FileNotFoundError:
            print(f"Image non trouvée : {chemin}")
            return None

    def dessiner_arbre(self):
        coords = {
            "Grand-parents": (530, 100, 200),
            "Parents": (250, 310, 150),
            "Enfants": (250, 500, 150)
        }

        for generation, (x, y, step) in coords.items():
            for personne in self.donnees[generation]:
                self.dessiner_personne(personne, x, y)
                x += step

        # Dessin des lignes de connexion
        self.dessiner_lignes()

    def dessiner_personne(self, personne, x, y):
        image = self.charger_image(personne["avatar"])
        if image:
            self.images[personne["nom"]] = image
            self.canvas.create_image(x + 40, y, image=image)
            self.canvas.create_text(x + 40, y + 50, text=personne["nom"])
            
            bouton = customtkinter.CTkButton(self.canvas, text="Infos", width=60, command=lambda p=personne: self.afficher_infos(p))
            self.canvas.create_window(x + 40, y + 80, window=bouton)

    def dessiner_lignes(self):
        lignes = [
            (670, 180, 670, 250),  # Ligne Grand-parents -> Parents
            (620, 180, 700, 180),
            (290, 250, 1040, 250),
            (290, 250, 290, 270),
            (590, 250, 590, 270),
            (1040, 250, 1040, 270),

            (290, 430, 440, 430),
            (590, 430, 740, 430),
            (890, 430, 1040, 430),

            (290, 430, 290, 460),
            (440, 430, 440, 460),
            (590, 430, 590, 460),
            (740, 430, 740, 460),
            (890, 430, 890, 460),
            (1040, 430, 1040, 460)
        ]

        for x1, y1, x2, y2 in lignes:
            self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2)

    def afficher_infos(self, personne):
        messagebox.showinfo(personne["nom"], personne["infos"])

    def rechercher_personne(self):
        nom_recherche = self.search_entry.get().strip().lower()
        if not nom_recherche:
            messagebox.showinfo("Recherche", "Veuillez entrer un nom.")
            return

        for generation in self.donnees.values():
            for personne in generation:
                if nom_recherche in personne["nom"].lower():
                    self.afficher_infos(personne)
                    return

        messagebox.showinfo("Résultat", "Personne non trouvée.")

if __name__ == "__main__":
    app = ArbreGenealogique()
    app.mainloop()
