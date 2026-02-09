import tkinter as tk
from tkinter import messagebox

def calculer_total():
    try:
        quantite = int(entry_quantite.get())
        prix = float(entry_prix.get())
        total = quantite * prix
        label_total.config(text=f"Prix Total : {total} FCFA")
    except:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides")

def a_propos():
    messagebox.showinfo("À propos", "Application créée par Drissa Fane\nCandidat formation Simplon Développeur Data IA")

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Application de Gestion des Ventes")
fenetre.geometry("400x300")

# Champs
tk.Label(fenetre, text="Nom du produit").pack()
entry_nom = tk.Entry(fenetre)
entry_nom.pack()

tk.Label(fenetre, text="Quantité").pack()
entry_quantite = tk.Entry(fenetre)
entry_quantite.pack()

tk.Label(fenetre, text="Prix unitaire").pack()
entry_prix = tk.Entry(fenetre)
entry_prix.pack()

tk.Button(fenetre, text="Calculer Total", command=calculer_total).pack(pady=10)

label_total = tk.Label(fenetre, text="Prix Total : ")
label_total.pack()

tk.Button(fenetre, text="À propos", command=a_propos).pack(pady=10)

fenetre.mainloop()
