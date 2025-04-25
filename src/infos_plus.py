import sys
import tkinter as tk
from customtkinter import *
from tkinter import messagebox

generation = sys.argv[1] if len(sys.argv) > 1 else ""

root = CTk()
root.title("Informations Supplémentaires")
root.geometry("500x550")
root.resizable(False, False)

label = tk.Label(root, text=f"Génération : {generation}", font=("Arial", 16))
label.pack(pady=10)

boutons_par_generation = {
    "Grand-parents": ["Mari", "Enfants", "Petit fils"],
    "Parents": ["Soeur et frère", "Fils et Fille", "Niece", "Parents", "Mari"],
    "Enfants": ["Parents", "Cousine et cousin", "Tantes", "Oncles", "Grand Parents"]
}

boutons = boutons_par_generation.get(generation, [])

for texte in boutons:
    b = tk.Button(root, text=texte, width=25)
    b.pack(pady=5)

root.mainloop()
