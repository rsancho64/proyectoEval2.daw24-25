#! /usr/bin/python3
"""
daemon"""

def next(entero) -> int:
    return entero + 1

if __name__ == "__main__":

    for i in range(30):
        resultado = next(i)
        print(f"el next de {i} es {resultado}")

