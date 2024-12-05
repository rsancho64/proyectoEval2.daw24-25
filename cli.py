#! /usr/bin/python3
"""
CLI client"""

from core import next

def help():
    print("""
        uso: <entero> retorno>
        uso: bye or BYE for exit
        uso: help : this help
    """)


if __name__ == "__main__":

    # for i in range(30):
    #     resultado = next(i)
    #     print(f"el next de {i} es {resultado}")

    # i = input("entero? ")
    # try:
    #     i = int(i)
    # except ValueError:
    #     exit()
    # print(f"el next de {i} es {next(i)}")

    # while True:
    #     i = input("entero? ")
    #     try:
    #         i = int(i)
    #     except ValueError:
    #         print(f"dato no valido: {i}")
    #         continue
    #     print(f"el next de {i} es {next(i)}")    

    while True:
        """REPL"""
        i = input("entero? ")
        i = i.lower().strip()

        if i == "bye":
            print(f"ten un buen dia")            
            exit()

        if i == "help":
            help()
            continue

        try:
            i = int(i)
        except ValueError:
            print(f"dato no valido: {i}")
            continue
        print(f"el next de {i} es {next(i)}")