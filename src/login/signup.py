import tkinter as tk
from customtkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess
import os


set_appearance_mode("light")
set_default_color_theme("blue")

root = CTk()
root.title("Inscription")
root.geometry("500x550")
root.resizable(False, False)

def inscrire_utilisateur():
    nom = entry1.get()
    prenom = entry2.get()
    mot_de_passe = entry3.get()

    if not nom or not prenom or not mot_de_passe:
        messagebox.showwarning("Champs manquants", "Tous les champs sont requis.")
        return

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="arbre_g"
        )
        cursor = conn.cursor()

        query = "INSERT INTO users (nom, prenom, mot_de_passe) VALUES (%s, %s, %s)"
        cursor.execute(query, (nom, prenom, mot_de_passe))
        conn.commit()

        messagebox.showinfo("Succès", f"{prenom}, vous êtes inscrit avec succès !")
        cursor.close()
        conn.close()
        root.destroy()  
        chemin_index = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "index.py"))
        subprocess.run(["python", chemin_index])

    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Erreur de base de données : {err}")

frame = CTkFrame(root, fg_color="#91C8E4", height=400, width=350, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label1 = CTkLabel(frame, text="S'inscrire", font=("Arial", 20, "bold"), text_color="#222")
label1.pack(pady=(30, 20))

entry1 = CTkEntry(frame, placeholder_text="Nom", width=220)
entry1.pack(pady=10)

entry2 = CTkEntry(frame, placeholder_text="Prénom", width=220)
entry2.pack(pady=10)

entry3 = CTkEntry(frame, placeholder_text="Mot de passe", width=220, show="*")
entry3.pack(pady=10)

btn = CTkButton(frame, text="Valider", corner_radius=20, hover_color="#1877F2", width=150, command=inscrire_utilisateur)
btn.pack(pady=25)

root.mainloop()
