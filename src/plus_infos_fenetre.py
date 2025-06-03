import sys
from customtkinter import *
from tkinter import messagebox
import mysql.connector

set_appearance_mode("Dark")
set_default_color_theme("blue")

generation = sys.argv[1] if len(sys.argv) > 1 else "Inconnue"
nom = sys.argv[2] if len(sys.argv) > 2 else "Inconnu"

class PlusInfosFenetre(CTk):
    def __init__(self):
        super().__init__()
        self.title("Informations Supplémentaires")
        self.geometry("500x550")
        self.resizable(False, False)

        # Connexion à la base
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="arbre_g"
            )
            self.cursor = self.conn.cursor(dictionary=True)
        except Exception as e:
            messagebox.showerror("Erreur BDD", f"Connexion échouée : {e}")
            self.destroy()
            return

        self.personne_id = self.get_personne_id(nom)
        self.personne_data = self.get_personne_data()

        CTkLabel(self, text=f"Génération : {generation}", font=("Arial", 20, "bold")).pack(pady=(20, 5))
        CTkLabel(self, text=f"Personne : {nom}", font=("Arial", 16)).pack(pady=(0, 20))

        self.frame_boutons = CTkScrollableFrame(self, width=450, height=400)
        self.frame_boutons.pack(pady=10, padx=10)

        boutons_par_generation = {
            "Grand-parents": ["Enfants", "Petit fils", "Mari"],
            "Parents": ["Fils et Fille", "Parents", "Frère et sœur", "Mari"],
            "Enfants": ["Parents", "Grand Parents", "Frère et sœur"]
        }

        boutons = boutons_par_generation.get(generation, [])

        for texte in boutons:
            btn = CTkButton(self.frame_boutons, text=texte, width=400, height=40,
                            fg_color="#3B82F6", hover_color="#2563EB",
                            command=lambda t=texte: self.action_bouton(t))
            btn.pack(pady=8)

    def get_personne_id(self, nom):
        self.cursor.execute("SELECT id_personne FROM personnes WHERE nom = %s", (nom,))
        row = self.cursor.fetchone()
        return row["id_personne"] if row else None

    def get_personne_data(self):
        self.cursor.execute("SELECT * FROM personnes WHERE id_personne = %s", (self.personne_id,))
        return self.cursor.fetchone()

    def action_bouton(self, relation):
        if not self.personne_id:
            messagebox.showerror("Erreur", "Personne introuvable dans la base.")
            return

        try:
            if relation in ["Fils et Fille", "Enfants"]:
                query = "SELECT * FROM personnes WHERE id_pere = %s OR id_mere = %s"
                self.cursor.execute(query, (self.personne_id, self.personne_id))

            elif relation == "Parents":
                pere_id = self.personne_data["id_pere"]
                mere_id = self.personne_data["id_mere"]
                if pere_id and mere_id:
                    self.cursor.execute("SELECT * FROM personnes WHERE id_personne IN (%s, %s)", (pere_id, mere_id))
                elif pere_id:
                    self.cursor.execute("SELECT * FROM personnes WHERE id_personne = %s", (pere_id,))
                elif mere_id:
                    self.cursor.execute("SELECT * FROM personnes WHERE id_personne = %s", (mere_id,))
                else:
                    messagebox.showinfo("Parents", "Aucun parent connu.")
                    return

            elif relation == "Petit fils":
                query = "SELECT * FROM personnes WHERE id_pere IN (SELECT id_personne FROM personnes WHERE id_pere = %s OR id_mere = %s) OR id_mere IN (SELECT id_personne FROM personnes WHERE id_pere = %s OR id_mere = %s)"
                self.cursor.execute(query, (self.personne_id, self.personne_id, self.personne_id, self.personne_id))

            elif relation == "Frère et sœur":
                pere_id = self.personne_data["id_pere"]
                mere_id = self.personne_data["id_mere"]
                query = "SELECT * FROM personnes WHERE id_pere = %s AND id_mere = %s AND id_personne != %s"
                self.cursor.execute(query, (pere_id, mere_id, self.personne_id))

            elif relation == "Grand Parents":
                pere_id = self.personne_data["id_pere"]
                mere_id = self.personne_data["id_mere"]
                ids = []
                if pere_id:
                    self.cursor.execute("SELECT id_pere, id_mere FROM personnes WHERE id_personne = %s", (pere_id,))
                    row = self.cursor.fetchone()
                    if row:
                        ids.extend([row["id_pere"], row["id_mere"]])
                if mere_id:
                    self.cursor.execute("SELECT id_pere, id_mere FROM personnes WHERE id_personne = %s", (mere_id,))
                    row = self.cursor.fetchone()
                    if row:
                        ids.extend([row["id_pere"], row["id_mere"]])
                ids = [i for i in ids if i is not None]
                if not ids:
                    messagebox.showinfo("Grand Parents", "Aucun grand-parent trouvé.")
                    return
                format_ids = ",".join(["%s"] * len(ids))
                self.cursor.execute(f"SELECT * FROM personnes WHERE id_personne IN ({format_ids})", tuple(ids))

            elif relation == "Mari":
                self.cursor.execute("SELECT * FROM personnes WHERE id_conjoint = %s OR id_personne = (SELECT id_conjoint FROM personnes WHERE id_personne = %s)", (self.personne_id, self.personne_id))

            else:
                messagebox.showinfo(relation, "Relation non prise en charge.")
                return

            resultats = self.cursor.fetchall()
            if not resultats:
                messagebox.showinfo(relation, "Aucune personne trouvée.")
            else:
                texte = "\n\n".join(f"{p['nom']} ({p['age']} ans)\n{p['infos']}" for p in resultats)
                messagebox.showinfo(f"{relation} de {nom}", texte)

        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la recherche : {e}")

if __name__ == "__main__":
    app = PlusInfosFenetre()
    app.mainloop()
