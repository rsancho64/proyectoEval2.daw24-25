#! /usr/bin/python3
"""
GUI client"""

from core import next
import tkinter as tk

# def calcular_siguiente():
#     try:
#         numero = int(entrada.get())
#         siguiente_numero = numero + 1
#         resultado.config(text=f"Siguiente entero: {siguiente_numero}")
#     except ValueError:
#         resultado.config(text="Por favor, introduce un número entero válido.")

def calcular_siguiente():
    # global textHelp
    textHelp = """
        uso: <entero> retorno>
        uso: bye or BYE for exit
        uso: help : this help
    """
    try:
        i = entrada.get()
        i = i.lower().strip()        
        if i == "bye":
            ventana.destroy()
        if i == "help":
            # resultado.configure(text=textHelp)
            # resultado.config(text=f"{textHelp}")
            # resultado.config(text="puta ayuda")        
            resultado.config(text="THIS IS HELP")

        numero = int(i)
        siguiente_numero = next(numero)
        resultado.config(text=f"Siguiente entero: {siguiente_numero}")
    except ValueError:
        resultado.config(text="Por favor, introduce un número entero válido.")



if __name__ == "__main__":

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Calculadora del siguiente entero")

    # Crear un cuadro de entrada
    entrada = tk.Entry(ventana)
    entrada.pack(pady=10)

    # Crear un botón que llama a la función calcular_siguiente
    boton = tk.Button(ventana, text="Calcular", command=calcular_siguiente)
    boton.pack(pady=5)

    # Crear una etiqueta para mostrar el resultado
    resultado = tk.Label(ventana, text="")
    resultado.pack(pady=10)

    # Ejecutar el bucle principal de Tkinter
    ventana.mainloop()


