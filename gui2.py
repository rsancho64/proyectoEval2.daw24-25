#! /usr/bin/python3
 
import tkinter as tk

def calcular_siguiente():
    entrada_texto = entrada.get()
    if entrada_texto == "help":
        resultado.config(text="No hay ayuda de momento")
    else:
        try:
            numero = int(entrada_texto)
            siguiente_numero = numero + 1
            resultado.config(text=f"Siguiente entero: {siguiente_numero}")
        except ValueError:
            resultado.config(text="Por favor, introduce un número entero válido.")

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


