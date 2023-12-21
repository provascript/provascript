stringa_lunga = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# Dividi la stringa in parole
parole = stringa_lunga.split()

# Conta il numero totale di parole
numero_totale_parole = len(parole)

print(f"Il numero totale di parole è: {numero_totale_parole}")

# Inizializza il conteggio per la parola 'dolor'
conteggio_dolor = 0

# Itera attraverso le parole nella lista
for parola in parole:
    # Confronta la parola con 'dolor' (ignorando maiuscole e minuscole)
    if parola.lower() == 'dolor':
        # Incrementa il conteggio se la parola corrente è 'dolor'
        conteggio_dolor += 1

# Stampa il risultato
print(f"La parola 'dolor' appare {conteggio_dolor} volte nella stringa.")
