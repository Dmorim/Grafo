import tkinter as tk
import matplotlib.pyplot as plt


class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        root.title('Gráfico de Linha')

        self.label1 = tk.Label(root, text='Digite os valores do eixo x, separados por vírgula:')
        self.label1.pack()

        self.entry1 = tk.Entry(root)
        self.entry1.pack()

        self.label2 = tk.Label(root, text='Digite os valores do eixo y, separados por vírgula:')
        self.label2.pack()

        self.entry2 = tk.Entry(root)
        self.entry2.pack()

        self.confirmar_button = tk.Button(root, text='Confirmar', command=self.plot_grafico)
        self.confirmar_button.pack()

        self.pers_button = tk.Button(root, text='Personalizar Gráfico', command=self.personalizar_grafico)
        self.pers_button.pack()

    def plot_grafico(self):
        eixo_x = self.entry1.get().split(',')
        eixo_y = self.entry2.get().split(',')

        plt.plot(eixo_x, eixo_y, linestyle=self.tlinha)
        plt.title('Grafico de Linha')
        plt.xlabel('Eixo X')
        plt.ylabel('Eixo Y')
        plt.show()

    def personalizar_grafico(self):
        self.janela = tk.Toplevel(self.root)
        self.janela.title('Personalizar Gráfico')

        self.tracl_label = tk.Label(self.janela, text='Selecione o tipo de linha:')
        self.tracl_label.pack()

        self.tlinha = 'o-'

        self.tlinha1b = tk.Button(self.janela, text='Contínua', command=self.continua)
        self.tlinha1b.pack(side='left')

        self.tlinha2b = tk.Button(self.janela, text='Tracejada', command=self.tracejada)
        self.tlinha2b.pack(side='left')

        self.tlinha3b = tk.Button(self.janela, text='Pontilhada', command=self.pontilhada)
        self.tlinha3b.pack(side='left')

    def continua(self):
        self.tlinha = '-'
        plt.plot([], linestyle=self.tlinha)
        plt.show()

    def tracejada(self):
        self.tlinha = '--'
        plt.plot([], linestyle=self.tlinha)
        plt.show()

    def pontilhada(self):
        self.tlinha = ':'
        plt.plot([], linestyle=self.tlinha)
        plt.show()


if __name__ == '__main__':
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()
