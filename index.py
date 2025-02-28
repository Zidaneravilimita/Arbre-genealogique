import customtkinter
import tkinter as tk
from PIL import Image, ImageTk
import os

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

        # Données de l'arbre généalogique 
        self.donnees = {
            "Grand-parents": [{"nom": "Alice", "infos": "Mère de Charlie", "avatar": "avatar_mere.png"},
                              {"nom": "Bob", "infos": "Père de Charlie", "avatar": "avatar_homme.png"}],
            "Parents": [{"nom": "Charlie", "infos": "Père de Eve et Frank", "avatar": "avatar_homme.png"},
                        {"nom": "Diana", "infos": "Mère de Eve et Frank", "avatar": "avatar_mere.png"},
                        {"nom": "Eva", "infos": "Mère de Henri et Irene", "avatar": "avatar_mere_2.png"},
                        {"nom": "Georges", "infos": "Père de Henri et Irene", "avatar": "avatar_homme.png"},
                        {"nom": "Julie", "infos": "Mère de Kevin et Laura", "avatar": "avatar_mere.png"},
                        {"nom": "Marc", "infos": "Père de Kevin et Laura", "avatar": "avatar_homme.png"}],
            "Enfants": [{"nom": "Eve", "infos": "Fille de Charlie et Diana", "avatar": "avatar_fille_2.png"},
                        {"nom": "Frank", "infos": "Fils de Charlie et Diana", "avatar": "avatar_boy.png"},
                        {"nom": "Henri", "infos": "Fils de Eva et Georges", "avatar": "avatar_boy.png"},
                        {"nom": "Irene", "infos": "Fille de Eva et Georges", "avatar": "avatar_fille_2.png"},
                        {"nom": "Kevin", "infos": "Fils de Julie et Marc", "avatar": "avatar_boy.png"},
                        {"nom": "Laura", "infos": "Fille de Julie et Marc", "avatar": "avatar_fille_1.png"}]
        }

        self.images = {}  # Stocker les images d'avatar
        self.dessiner_arbre()

    def charger_image(self, chemin):
        try:
            # Assurez-vous que le chemin est correct en ajoutant le dossier "images"
            chemin_complet = os.path.join("images", chemin)
            image = Image.open(chemin_complet)
            image = image.resize((80, 80), Image.LANCZOS) # Modification ici
            return ImageTk.PhotoImage(image)
        except FileNotFoundError:
            print(f"Image non trouvée : {chemin}")
            return None

    def dessiner_arbre(self):
        x_grandparents = 530
        y_grandparents = 100
        x_parents = 250
        y_parents = 310
        x_enfants = 250
        y_enfants = 500

        for personne in self.donnees["Grand-parents"]:
            self.dessiner_personne(personne, x_grandparents, y_grandparents)
            x_grandparents += 200

        for personne in self.donnees["Parents"]:
            self.dessiner_personne(personne, x_parents, y_parents)
            x_parents += 150

        for personne in self.donnees["Enfants"]:
            self.dessiner_personne(personne, x_enfants, y_enfants)
            x_enfants += 150

        # Dessin des lignes dans l'arbre
        self.canvas.create_line(670, 180, 670, 250,
                                fill="black", width=2)
        self.canvas.create_line(620, 180, 700, 180,
                                fill="black", width=2)
        self.canvas.create_line(290, 250, 1040, 250,
                                fill="black", width=2)
        self.canvas.create_line(290, 250, 290, 270,
                                fill="black", width=2)
        self.canvas.create_line(590, 250, 590, 270,
                                fill="black", width=2)
        self.canvas.create_line(1040, 250, 1040, 270,
                                fill="black", width=2)
        
        #ligne horizontale au enfants
        self.canvas.create_line(290, 430, 440, 430,
                                fill="black", width=2)
        self.canvas.create_line(590, 430, 740, 430,
                                fill="black", width=2)
        self.canvas.create_line(890, 430, 1040, 430,
                                fill="black", width=2)
        
       
        self.canvas.create_line(290, 430, 290, 460,
                                fill="black", width=2)
        self.canvas.create_line(440, 430, 440, 460,
                                fill="black", width=2)
        self.canvas.create_line(590, 430, 590, 460,
                                fill="black", width=2)
        self.canvas.create_line(740, 430, 740, 460,
                                fill="black", width=2)
        self.canvas.create_line(890, 430, 890, 460,
                                fill="black", width=2)
        self.canvas.create_line(1040, 430, 1040, 460,
                                fill="black", width=2)

    def dessiner_personne(self, personne, x, y):
        image = self.charger_image(personne["avatar"])
        if image:
            self.images[personne["nom"]] = image
            self.canvas.create_image(x + 40, y, image=image)
            self.canvas.create_text(x + 40, y + 50, text=personne["nom"])
            bouton = customtkinter.CTkButton(self.canvas, text="Infos", command=lambda p=personne: self.afficher_infos(p))
            self.canvas.create_window(x + 40, y + 80, window=bouton)

    def afficher_infos(self, personne):
        tk.messagebox.showinfo(personne["nom"], personne["infos"])

    def rechercher_personne(self):
        nom_recherche = self.search_entry.get().lower()
        for generation in self.donnees.values():
            for personne in generation:
                if nom_recherche in personne["nom"].lower():
                    self.afficher_infos(personne)
                    return
        tk.messagebox.showinfo("Résultat", "Personne non trouvée.")

if __name__ == "__main__":
    app = ArbreGenealogique()
    app.mainloop()