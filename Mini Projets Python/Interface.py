from tkinter import *

fenetre = Tk()
fenetre.title("interface")
fenetre.iconbitmap("md243.jpg")
fenetre.geometry("300x440")
fenetre.minsize(200, 300)
fenetre.maxsize(400, 500)

titre = Label(fenetre, text ="Mon Interface")
titre.pack()

champ = Entry(fenetre)
champ.pack()

check = Checkbutton(text="checker")
check.pack()


fenetre.mainloop()