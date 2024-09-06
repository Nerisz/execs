def verificar_letra_a(string):
    quantidade = string.lower().count('a')
    
    if quantidade > 0:
        print(f"A letra 'a' aparece {quantidade} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")

texto = input("Informe uma string para verificar a existência da letra 'a': ")

verificar_letra_a(texto)