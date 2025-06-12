from tkinter import messagebox
from PIL import Image, ImageTk
from api import DatabaseManager
import tkinter as tk
import customtkinter
import subprocess
import os

class ArbreGenealogique(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Arbre Généalogique")
        self.geometry("1000x900")

        self.db = DatabaseManager()
        self.donnees = self.recuperer_donnees_bdd()
        self.images = {}
        self.positions_par_nom = {}
        self.positions_y = {}

        self.search_frame = customtkinter.CTkFrame(self)
        self.search_frame.pack(pady=10)

        self.search_entry = customtkinter.CTkEntry(self.search_frame, width=250)
        self.search_entry.pack(side=tk.LEFT, padx=10)

        self.search_button = customtkinter.CTkButton(self.search_frame, text="Rechercher", command=self.rechercher_personne)
        self.search_button.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(self, bg="white", width=1000, height=900)
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
                "avatar": personne.get("avatar", "default.png"),
                "id_pere": personne.get("id_pere"),
                "id_mere": personne.get("id_mere")
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

    def match_parents(self, infos, nom_p1, nom_p2):
        infos = infos.lower()
        return (nom_p1.lower() in infos or nom_p1.split()[0].lower() in infos) and \
               (nom_p2.lower() in infos or nom_p2.split()[0].lower() in infos)

    def dessiner_arbre(self):
        coords = {
            "Grand-parents": (550, 100, 200),
            "Parents": (200, 300, 160),
            "Enfants": (200, 550, 140)
        }

        # Grand-parents centrés
        x, y, step = coords["Grand-parents"]
        for i, personne in enumerate(self.donnees["Grand-parents"]):
            self.dessiner_personne(personne, x, y, "Grand-parents")
            self.positions_par_nom[personne["nom"]] = x
            self.positions_y[personne["nom"]] = y
            if i % 2 == 1:
                x1 = self.positions_par_nom[self.donnees["Grand-parents"][i - 1]["nom"]] + 60
                x2 = x + 10
                self.canvas.create_line(x1, y, x2, y, fill="red", width=2)
            x += step

        # Parents
        x, y, step = coords["Parents"]
        couples = []
        for i, personne in enumerate(self.donnees["Parents"]):
            self.dessiner_personne(personne, x, y, "Parents")
            self.positions_par_nom[personne["nom"]] = x
            self.positions_y[personne["nom"]] = y
            if i % 2 == 1:
                couples.append((self.donnees["Parents"][i - 1]["nom"], personne["nom"]))
                x1 = self.positions_par_nom[self.donnees["Parents"][i - 1]["nom"]] + 60
                x2 = x + 10
                self.canvas.create_line(x1, y, x2, y, fill="red", width=2)
            x += step

        #  Lignes verticales au-dessus des enfants directs des grands-parents
        enfants_gp = ["Mana Thomas", "Felana", "Parally"]
        for nom in enfants_gp:
            if nom in self.positions_par_nom and nom in self.positions_y:
                x_p = self.positions_par_nom[nom] + 40
                y_p = self.positions_y[nom]
                self.canvas.create_line(x_p, y_p - 60, x_p, y_p - 30, fill="blue", width=2)

        # Lignes descendantes des grands-parents vers ligne horizontale
        y_parents = coords["Parents"][1]
        y_line_gp = y_parents - 60
        parents_x = [self.positions_par_nom[p["nom"]] + 40 for p in self.donnees["Parents"]]
        if parents_x:
            x_start = min(parents_x)
            x_end = max(parents_x)
            self.canvas.create_line(x_start, y_line_gp, x_end, y_line_gp, fill="blue", width=2)
            for gp in self.donnees["Grand-parents"]:
                gp_nom = gp["nom"]
                x_gp = self.positions_par_nom[gp_nom] + 40
                y_gp = self.positions_y[gp_nom] + 90
                self.canvas.create_line(x_gp, y_gp, x_gp, y_line_gp, fill="blue", width=2)

        # Enfants
        y_enfant = coords["Enfants"][1]
        deja_affiches = set()
        for nom_p1, nom_p2 in couples:
            enfants = []
            for enfant in self.donnees["Enfants"]:
                if enfant["nom"] in deja_affiches:
                    continue
                if self.match_parents(enfant.get("infos", ""), nom_p1, nom_p2):
                    enfants.append(enfant)
                    deja_affiches.add(enfant["nom"])

            if not enfants:
                continue

            x1 = self.positions_par_nom[nom_p1]
            x2 = self.positions_par_nom[nom_p2]
            x_center = (x1 + x2) // 2

            total_width = (len(enfants) - 1) * coords["Enfants"][2]
            start_x = x_center - total_width // 2

            for i, enfant in enumerate(enfants):
                x_enfant = start_x + i * coords["Enfants"][2]
                self.dessiner_personne(enfant, x_enfant, y_enfant, "Enfants")

            self.canvas.create_line(x_center + 40, self.positions_y[nom_p1] + 90, x_center + 40, y_enfant, fill="green", width=2)

    def dessiner_personne(self, personne, x, y, generation):
        image = self.charger_image(personne["avatar"])
        if image:
            key = f"{personne['nom']}_{x}_{y}"
            if key not in self.images:
                self.images[key] = image
                self.canvas.create_image(x + 40, y, image=image)
                self.canvas.create_text(x + 40, y + 50, text=f"{personne['nom']} ({personne['age']} ans)")
                bouton1 = customtkinter.CTkButton(self.canvas, fg_color="MediumTurquoise", text="Infos", width=60, command=lambda p=personne: self.afficher_infos(p))
                self.canvas.create_window(x + 5, y + 80, window=bouton1)
                bouton2 = customtkinter.CTkButton(self.canvas, text="Plus d'infos", width=80, fg_color="gray", command=lambda p=personne, g=generation: self.afficher_infos_2(p, g))
                self.canvas.create_window(x + 85, y + 80, window=bouton2)

    def afficher_infos(self, personne):
        messagebox.showinfo(personne["nom"], personne["infos"])

    def afficher_infos_2(self, personne, generation):
        try:
            dossier_script = os.path.dirname(os.path.abspath(__file__))
            chemin_fenetre = os.path.join(dossier_script, "plus_infos_fenetre.py")
            subprocess.Popen(["python", chemin_fenetre, generation, personne["nom"]])
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir la fenêtre : {e}")

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
