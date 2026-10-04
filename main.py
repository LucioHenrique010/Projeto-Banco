from classes import *
from rich import print, inspect

def main():
    a = PessoaFisica("Joao", "M", 2004, "123486")
    inspect(a, methods=True, private=True)

if __name__ == "__main__":
    main()