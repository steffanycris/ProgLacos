

contador = 1

while ( contador < 20 ):

    print( contador )

    if ( contador == 10 ):
        print("--- INÍCIO DO BLOCO DO IF ---")
        print("Neste momento o contador vale 10")
        break #tire esse break para ver a diferença
        print("--- FIM DO BLOCO DO IF ---")

    contador = contador + 1

print("--- Linha após o bloco do while ---")
print("--- FIM DO PROGRAMA ---")