import tkinter as tk
from customtkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess
import os


 # Initialisation des thèmes graphique GUI
set_appearance_mode("light")
set_default_color_theme("blue")
root = CTk()
root.title("Connexion")
root.geometry("500x550")
root.resizable(False, False)

 ## Fonction de connexion à la base de donnés
def verifier_identifiants():
    nom = entry1.get()
    prenom = entry2.get()
    mot_de_passe = entry3.get()

    if not nom or not prenom or not mot_de_passe:
        messagebox.showerror("Erreur", "Tous les champs sont requis.")
        return

    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",  
            password = "",  
            database = "utilisateurs"
        )
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE nom=%s AND prenom=%s AND mot_de_passe=%s"
        cursor.execute(query, (nom, prenom, mot_de_passe))
        result = cursor.fetchone()

        if result:
             messagebox.showinfo("Succès", f"Bienvenue {prenom} !")
             root.destroy()
             chemin_index = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "index.py"))
             subprocess.run(["python", chemin_index])
        else:
            messagebox.showerror("Erreur", "Identifiants incorrects.")
        
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Erreur de connexion : {err}")

def aller_signup():
    root.destroy()
    chemin_signup = os.path.join(os.path.dirname(__file__), "signup.py")
    subprocess.run(["python", chemin_signup])


  ### Affichage et masque du mot de passe
def toggle_password():
    entry3.configure(show="" if switch.get() else "*")

  ## Interface graphique
frame = CTkFrame(root, fg_color="#FFCC70", height=400, width=350, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label1 = CTkLabel(frame, text="Se connecter", font=("Arial", 20, "bold"), text_color="#333")
label1.pack(pady=(30, 20))

entry1 = CTkEntry(frame, placeholder_text="Nom", width=220)
entry1.pack(pady=10)

entry2 = CTkEntry(frame, placeholder_text="Prénom", width=220)
entry2.pack(pady=10)

entry3 = CTkEntry(frame, placeholder_text="Mot de passe", width=220, show="*")
entry3.pack(pady=10)

switch_frame = CTkFrame(frame, fg_color="transparent")
switch_frame.pack(pady=(5, 10))
switch = CTkSwitch(switch_frame, text="Afficher le mot de passe", command=toggle_password)
switch.pack()

btn = CTkButton(frame, text="Entrer", corner_radius=20, hover_color="#C500C0", width=150, command=verifier_identifiants)
btn.pack(pady=(10, 20))

btn2 = CTkButton(frame, text="S'inscrire", width=150, fg_color="transparent", border_color="blue", border_width=1, text_color="blue", command=aller_signup)
btn2.pack()

root.mainloop()
