import mysql.connector
from tkinter import *


conn = mysql.connector.connect(
    host="localhost",
    user='root',
    password="Restepro-3",
    database="boutique"
)

cursor = conn.cursor()


root = Tk()
root.geometry("600x400")
root.title("Liste des produits")


table = Frame(root)
table.pack(pady=10, padx=10)


nom_label = Label(table, text="Nom")
nom_label.grid(row=0, column=0)

description_label = Label(table, text="Description")
description_label.grid(row=0, column=1)

prix_label = Label(table, text="Prix")
prix_label.grid(row=0, column=2)

quantite_label = Label(table, text="Quantité")
quantite_label.grid(row=0, column=3)

categorie_label = Label(table, text="Catégorie")
categorie_label.grid(row=0, column=4)


row_number = 1
cursor.execute("SELECT produit.nom, produit.description, produit.prix, produit.quantite, categorie.nom FROM produit INNER JOIN categorie ON produit.id_categorie = categorie.id")
for row in cursor.fetchall():
    nom = Label(table, text=row[0])
    nom.grid(row=row_number, column=0)

    description = Label(table, text=row[1])
    description.grid(row=row_number, column=1)

    prix = Label(table, text=row[2])
    prix.grid(row=row_number, column=2)

    quantite = Label(table, text=row[3])
    quantite.grid(row=row_number, column=3)

    categorie = Label(table, text=row[4])
    categorie.grid(row=row_number, column=4)

    row_number += 1


cursor.close()
conn.close()

root.mainloop()


# Je n'ai pas réussi mettre des bouton ajouter, supprimer ou modifer a mon code enfin si mais 
# Ils ne fonctionnait pas.