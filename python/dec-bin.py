# Chiedi all'utente di inserire un numero decimale
num_dec = int(input("Inserisci un numero decimale: "))

num_bin = ""

num_loop = num_dec

while num_loop > 0:
    # Aggiungi la cifra binaria più a destra
    num_bin = str(num_loop % 2) + num_bin
    # Dividi il numero per 2
    num_loop = num_loop // 2

print(f"Il numero {num_dec} in base 2 è {num_bin}")
