

contador = 1

for contador in range( 1,20 ):

    print( contador )

    if ( contador == 10 ):
        print("--- INÍCIO DO BLOCO DO IF ---")
        print("Neste momento o contador vale 10")
        continue #tire esse continue para ver a diferença
        print("--- FIM DO BLOCO DO IF ---")



print("--- Linha após o bloco do for ---")
print("--- FIM DO PROGRAMA ---")