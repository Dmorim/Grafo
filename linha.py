import matplotlib.pyplot as plt
import tkinter as tk

def linha():
    global entry1
    global entry2
    global root
    root = tk.Tk()
    root.geometry('270x140')
    label1 = tk.Label(root, text= 'Digite os valores do eixo x, separados por virgula')
    entry1 = tk.Entry(root)
    label2 = tk.Label(root, text= 'Digite os valores do eixo y, separados por virgula')
    entry2 = tk.Entry(root)
    label1.pack()
    entry1.pack()
    label2.pack()
    entry2.pack()
    button = tk.Button(root, text= 'Confirmar',
                       command= grafico)
    button.pack()
    #pers = tk.Button(root, text= 'Personalizar o Gráfico',
                     #command= personalizar)
    #pers.pack(side= tk.LEFT)

    root.mainloop()
def personalizar():
    global tlinha
    global janela
    janela = tk.Tk()
    janela.geometry('190x150')
    tracl = tk.Label (janela, text='Selecione o tipo de linha')
    tracl.pack(side='top')
    tlinha = '-'
    def continuo():
        global tlinha
        tlinha += ''
    def tracejada():
        global tlinha
        tlinha += '-'
    def pontilhada():
        global tlinha
        tlinha -= '-'
        tlinha += ':'
    tlinha1b = tk.Button(janela, text= 'Contínua',
                         command= continuo)
    tlinha1b.pack(side='left', anchor='nw')
    tlinha2b = tk.Button(janela, text= 'Tracejada',
                         command= tracejada)
    tlinha2b.pack(side='right', anchor='nw')
    tlinha3b = tk.Button(janela, text= 'Pontilhada',
                         command= pontilhada)
    tlinha3b.pack(side= 'right', anchor= 'nw')

def grafico():
    eixox = entry1.get().split(',')
    eixoy = entry2.get().split(',')
    plt.plot(eixox,eixoy, 'o-')
    plt.title('Grafico de Linha')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    root.destroy()
    #janela.destroy()
    plt.show()

