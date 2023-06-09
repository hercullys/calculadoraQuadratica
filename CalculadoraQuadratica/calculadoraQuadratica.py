import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return None  # Não existem raízes reais

    x1 = (-b + np.sqrt(delta)) / (2*a)
    x2 = (-b - np.sqrt(delta)) / (2*a)

    return x1, x2

def equacao_quadratica(x, a, b, c):
    return a*x**2 + b*x + c

def plotar_grafico(a, b, c):
    # Limpar o gráfico anterior
    grafico_frame.clear()

    raizes = calcular_raizes(a, b, c)

    if raizes is None:
        resultado_label.configure(text="A equação não possui raízes reais.")
        return

    resultado_label.configure(text="As raízes da equação são: {:.2f}  {:.2f}".format(raizes[0], raizes[1]))

    x = np.linspace(-10, 10, 100)
    y = equacao_quadratica(x, a, b, c)

    grafico_frame.plot(x, y)
    grafico_frame.axhline(0, color='black', linewidth=0.5)
    grafico_frame.axvline(0, color='black', linewidth=0.5)
    grafico_frame.set_xlabel("x")
    grafico_frame.set_ylabel("y")
    grafico_frame.set_title("Gráfico da Equação Quadrática")
    grafico_frame.grid(True)

    canvas.draw()

def exibir_alerta(mensagem):
    messagebox.showwarning("Aviso", mensagem)

def atualizar_grafico():
    a_entry_text = a_entry.get()
    b_entry_text = b_entry.get()
    c_entry_text = c_entry.get()

    if not a_entry_text or not b_entry_text or not c_entry_text:
        exibir_alerta("Por favor, preencha todos os coeficientes.")
        return

    try:
        a = float(a_entry_text)
        b = float(b_entry_text)
        c = float(c_entry_text)
    except ValueError:
        exibir_alerta("Digite valores numéricos válidos.")
        return

    plotar_grafico(a, b, c)

def limpar_campos():
    a_entry.delete(0, tk.END)
    b_entry.delete(0, tk.END)
    c_entry.delete(0, tk.END)
    resultado_label.configure(text="")
    grafico_frame.clear()
    canvas.draw()

# Criar a janela principal
window = tk.Tk()
window.title("Calculadora de Bhaskara")

# Criar os elementos da interface
a_label = tk.Label(window, text="Coeficiente a:")
a_label.pack()
a_entry = tk.Entry(window)
a_entry.pack()

b_label = tk.Label(window, text="Coeficiente b:")
b_label.pack()
b_entry = tk.Entry(window)
b_entry.pack()

c_label = tk.Label(window, text="Coeficiente c:")
c_label.pack()
c_entry = tk.Entry(window)
c_entry.pack()

calcular_button = tk.Button(window, text="Calcular", command=atualizar_grafico)
calcular_button.pack()

resultado_label = tk.Label(window, text="")
resultado_label.pack()

limpar_button = tk.Button(window, text="Limpar", command=limpar_campos)
limpar_button.pack()

# Frame para o gráfico
fig, grafico_frame = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()

# Executar a interface gráfica
window.mainloop()
