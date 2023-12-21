# Dimensioni dell'area
area = [30, 30]

# Chiedi all'utente di inserire le coordinate del punto
punto_x = float(input("Inserisci la coordinata x del punto: "))
punto_y = float(input("Inserisci la coordinata y del punto: "))

# Corregi gli operatori di confronto
interno_area = 0 <= punto_x <= area[0] and 0 <= punto_y <= area[1]

# Determina il risultato in base alla condizione
risultato = "interno" if interno_area else "esterno"

# Stampa il risultato
print(f"Il punto [{punto_x}, {punto_y}] è {risultato} all'area.")
