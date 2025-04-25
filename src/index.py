import customtkinter
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess
from api import DatabaseManager

class ArbreGenealogique(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Arbre Généalogique")
        self.geometry("1000x900")
        
        self.db = DatabaseManager()
        self.donnees = self.recuperer_donnees_bdd()

        self.images = {}

        self.search_frame = customtkinter.CTkFrame(self)
        self.search_frame.pack(pady=10)

        self.search_entry = customtkinter.CTkEntry(self.search_frame, width=250)
        self.search_entry.pack(side=tk.LEFT, padx=10)

        self.search_button = customtkinter.CTkButton(self.search_frame, text="Rechercher", command=self.rechercher_personne)
        self.search_button.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(expand=True, fill="both")

        self.dessiner_arbre()

    def recuperer_donnees_bdd(self):
        toutes_les_donnees = self.db.recuperer_toutes_les_donnees()
        donnees = {"Grand-parents": [], "Parents": [], "Enfants": []}
        for personne in toutes_les_donnees:
            table = personne["table_source"]
            data = {
                "nom": personne["nom"],
                "age": personne["age"],
                "infos": personne.get("infos", ""),
                "avatar": personne.get("avatar", "default.png")
            }
            if table == "grand_parents":
                donnees["Grand-parents"].append(data)
            elif table in ["parents", "oncle1_tante1", "oncle2_tante2"]:
                donnees["Parents"].append(data)
            else:
                donnees["Enfants"].append(data)
        return donnees

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
                self.dessiner_personne(personne, x, y, generation)
                x += step

    def dessiner_personne(self, personne, x, y, generation):
        image = self.charger_image(personne["avatar"])
        if image:
            self.images[personne["nom"]] = image
            self.canvas.create_image(x + 40, y, image=image)
            self.canvas.create_text(x + 40, y + 50, text=f"{personne['nom']} ({personne['age']} ans)")
            
            bouton1 = customtkinter.CTkButton(self.canvas, text="Infos", width=60, command=lambda p=personne: self.afficher_infos(p))
            self.canvas.create_window(x + 5, y + 80, window=bouton1)
            
            bouton2 = customtkinter.CTkButton(self.canvas, text="Plus d'infos", width=80, fg_color="gray", command=lambda p=personne, g=generation: self.afficher_infos_2(p, g))
            self.canvas.create_window(x + 85, y + 80, window=bouton2)

    def afficher_infos(self, personne):
        messagebox.showinfo(personne["nom"], personne["infos"])

    def afficher_infos_2(self, personne, generation):
        subprocess.run(["python", "infos_plus.py", generation])

    def rechercher_personne(self):
        nom_recherche = self.search_entry.get().strip().lower()
        for generation in self.donnees.values():
            for personne in generation:
                if nom_recherche in personne["nom"].lower():
                    self.afficher_infos(personne)
                    return
        messagebox.showinfo("Résultat", "Personne non trouvée.")

if __name__ == "__main__":
    app = ArbreGenealogique()
    app.mainloop()
