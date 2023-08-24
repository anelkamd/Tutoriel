from  tkinter import *

def Action():
    N=int(entrynombre1.get())
    N2=2*N
    entrynombre2.delete(0,END)
    entrynombre2.insert(0,N2)
fen=Tk()
fen.geometry("400x300")
lblnombre1= Label(fen,text="Entrer la valeur de N : ")
lblnombre1.place(x=50,y=50)
entrynombre1=Entry(fen)
entrynombre1.place(x=200,y=50)

lblnombre2= Label(fen,text="Voici le double : ")
lblnombre2.place(x=50,y=100)
entrynombre2=Entry(fen)
entrynombre2.place(x=200,y=100)
valider=Button(fen,text="Calculer",font="arial 15",bg="white",bd=3,command=Action)
valider.place(x=200,y=150)


fen.mainloop()