def inverter_string(texto):    
    return "".join([str(texto[x]) for x in range(len(texto) -1, -1, -1)])    

texto = str(input("Insira um texto: "))
print(f"Texto invertido: {inverter_string(texto)}")