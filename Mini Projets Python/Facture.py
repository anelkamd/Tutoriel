import tkinter as tk
from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Facture Anexus')

frame_container = tk.Frame(root, padx=10, pady=10, bg='#d3d3d3')
frame_fields = tk.Frame(frame_container, bg='#d3d3d3')

trv = ttk.Treeview(frame_container,columns=(1,2,3,4), show='headings')

trv.column(1, anchor='center', width=100)
trv.column(2, anchor='center', width=100)
trv.column(3, anchor='center', width=100)
trv.column(4, anchor='center', width=100)

trv.heading(1, text='ID')
trv.heading(2, text='Nom')
trv.heading(3, text='Quantite')
trv.heading(4, text='Prix')

trv.insert("",'end', iid=1,values=(1,"Product 1", 100, 10))
trv.insert("",'end', iid=2,values=(2,"Product 1", 200, 20))
trv.insert("",'end', iid=3,values=(3,"Product 1", 300, 30))
trv.insert("",'end', iid=4,values=(4,"Product 1", 400, 400))
trv.insert("",'end', iid=5,values=(5,"Product 1", 500, 50))
trv.insert("",'end', iid=6,values=(6,"Product 1", 600, 60))

sum_lbl = tk.Label(frame_fields, text='somme:', font=('verdana',14), bg='#d3d3d3')
sum_entry = tk.Entry(frame_fields, font=('verdana',14))

avg_lbl = tk.Label(frame_fields, text='Average:', font=('verdana', 14), bg='#d3d3d3')
avg_entry = tk.Entry(frame_fields, font=('verdana',14))

min_lbl = tk.Label(frame_fields, text='min:', font=('verdana',14), bg='#d3d3d3')
min_entry = tk.Entry(frame_fields, font=('verdana', 14))

max_lbl = tk.Label(frame_fields, text='max:', font=('verdana',14), bg='#d3d3d3')
max_entry = tk.Entry(frame_fields, font=('verdana', 14))

sum_lbl.grid(row=0, column=0, padx=10, sticky='e')
sum_entry.grid(row=0, column=1)

min_lbl.grid(row=2, column=0, padx=10, sticky='e')
min_entry.grid(row=2, column=1)

avg_lbl.grid(row=1, column=0, padx=10, sticky ='e')
avg_entry.grid(row=1, column=1)

max_lbl.grid(row=3, column=0, padx=10, sticky ='e')
max_entry.grid(row=3, column=1)


def getsum(item=""):
    val =0
    for row in trv.get_children(item):
       # print(trv.item(row)["values"][3])# print price
        val = val + trv.item(row)["values"][3]
        print(val)
        sum_entry.insert(0, val)

def getavg(item=""):
    val = 0
    for row in trv.get_children(item):
        # print(trv.item(row)["values"][3])# print price
        val = val + trv.item(row)["values"][3]

        val = val/len(trv.get_children())
        avg_entry.insert(0, val)
def getmin():
    val = trv.item("1")["values"][3]#get the first value
    for row in trv.get_children():
        # print(trv.item(row)["values"][3])# print price
        if val > trv.item(row)["values"][3]:
           val = trv.item(row)["values"][3]

    min_entry.insert(0, val)



def getmax():
    val = trv.item("1")["values"][3]  # get the first value
    for row in trv.get_children():
        # print(trv.item(row)["values"][3])# print price
        if val < trv.item(row)["values"][3]:
            val = trv.item(row)["values"][3]

    max_entry.insert(0, val)


getsum()
getavg()
getmin()
getmax()

trv.pack()
frame_container.pack()
frame_fields.pack()

root.mainloop()