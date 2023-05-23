import matplotlib.pyplot as plt
import tkinter as tk

root = tk.Tk()
root.geometry('140x55')

Lbl1 = tk.Label(root, text= 'Escolha o tipo de gráfico')
Lbl1.pack()
def graph():
    root.destroy()
    import linha
    linha.linha()
button = tk.Button(root, text= 'Gráfico em Linha',
                   command=graph)
button.pack()
root.mainloop()