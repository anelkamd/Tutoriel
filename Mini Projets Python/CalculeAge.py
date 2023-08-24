from tkinter import *
from datetime import date

root = Tk()
root.geometry("450x300")

def calulatriceAge():
    today = date.today()
    birth_date = date(int(Annee_entry.get()), int(Mois_entry.get()), int(Jour_entry.get()))
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    Label(text=f"Salut {Nom_value.get()}! vous avez: {age}ans", font=("arial", 15, "bold")).grid(row=6, column=1)

Label(text="Nom :", font=("arial", 15, "bold")).grid(row=1, column=0, padx=50)
Label(text="Jour :", font=("arial", 15, "bold")).grid(row=2, column=0)
Label(text="Mois :", font=("arial", 15, "bold")).grid(row=3, column=0)
Label(text="Annee :", font=("arial", 15, "bold")).grid(row=4, column=0)

Nom_value = StringVar()
Jour_value = StringVar()
Mois_value = StringVar()
Annee_value = StringVar()

Nom_entry = Entry(root, textvariable=Nom_value)
Jour_entry = Entry(root, textvariable=Jour_value)
Mois_entry = Entry(root, textvariable=Mois_value)
Annee_entry = Entry(root, textvariable=Annee_value)

Nom_entry.grid(row=1, column=1, pady=5)
Jour_entry.grid(row=2, column=1, pady=5)
Mois_entry.grid(row="3", column=1, pady=5)
Annee_entry.grid(row="4", column=1, pady=5)

button = Button(text="Calculer l'age", font=("arial", 15, "bold"), fg="black", bg="#f0f8ff", command=calulatriceAge)
button.grid(row=5, column=1, pady=5)



root.mainloop()