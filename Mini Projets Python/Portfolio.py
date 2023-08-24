from tkinter import *
import webbrowser

def open_graver_channel():
    webbrowser.open_new("https://twitter.com/Anelka_Dev")

#creer une premier fenetre
window = Tk()

#personnaliser cette application
window.title("Mon Portfoloi")
window.geometry("720x480")
window.minsize(480,360)
window.config(background='#add8e6')
#creer le frame
frame=Frame(window, bg='#add8e6')
#ajouter un premier text
Label_title= Label(frame, text="Bienvenue dans mon Monde des Dev's",font=("corrier",30),bg="#add8e6", fg='black')
Label_title.pack()
#Ajouter un second text
Label_title= Label(frame, text="Salut a tous moi c'est Anelka Dev",font=("corrier",20),bg="#add8e6", fg='black')
Label_title.pack()
#dernie text
Label_title= Label(frame, text="Voici mon compte twitter pour discuter",font=("corrier",10),bg="#add8e6", fg='black')
Label_title.pack()
#Ajouter un premier button
yt_button = Button(frame,text='Mon Compte Twitter',font=("corrier",25),bg='black', fg='#fff' ,command=open_graver_channel)
yt_button.pack(pady=25, fill=X)
#Ajouter
frame.pack(expand=YES)
#afficher

window.mainloop()
