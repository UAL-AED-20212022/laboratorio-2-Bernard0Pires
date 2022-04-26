from views import cli
import sys

sys.stdout.reconfigure(encoding="utf-8")

if __name__ == "__main__":
    cli.main()

# Programa que permite o armazenamento, consulta e modificação de uma lista ligada (neste caso, contendo nomes de países.)
# Este programa permite:
#   Registar país no início da lista (RPI)
#   Registar país no fim da lista (RPF)
#   Registar país depois de outro elemento (RPDE)
#   Registar país antes de outro elemento (RPAE)
#   Registar país num determinado índice (RPII)
#   Verificar número de elementos (VNE)
#   Verificar se um país se encontra a lista (VP)
#   Eliminar i 1º elemento (EPE)
#   Eliminar o último elemento (EUE)
#   Eliminar um determinado país (EP)