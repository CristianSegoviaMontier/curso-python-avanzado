# import tkinter as tk
from tkinter import Tk  # de esta forma solo importo la clase Tk
from tkinter.ttk import Treeview  # importo solo una clase dentro de un packete

# root = tk.Tk() # Es una clase ya que comienza con mayuscula
root = Tk()  # Es una clase ya que comienza con mayuscula

root.title('mi primera gui')


tree = Treeview(root)
tree['columns'] = ('Nombre', 'Email')
tree.column('#0', width=0)
tree.column('Nombre')
tree.column('Email')

tree.heading('#0', text='id')
tree.heading('Nombre', text='Nombre')
tree.heading('Email', text='Email')

tree.grid(row=0, column=0)

root.mainloop()
