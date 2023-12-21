def somma():
    a = int(input("insrisci il primo addendo"))
    b =int(input("insrisci il secondo addendo"))
    somma = a + b
    print("il risultato e:", somma)
def sottrazione():
    a = int(input("insrisci il primo numero"))
    b =int(input("insrisci il secondo numero"))
    sottrazione = a - b
    print("il risultato e:", sottrazione)
def moltiplicazione():
    a = int(input("insrisci il primo fattore"))
    b =int(input("insrisci il secondo fattore"))
    Moltiplicazione = a * b
    print("il risultato e:", Moltiplicazione)
def divisione():
    a = int(input("insrisci il primo numero"))
    b =int(input("insrisci il secondo numero"))
    if b == 0:
        print("non posso dividere per 0")
    else:
        Divisione = a / b
        print("il risultato e:", Divisione)
def binario():
    num_dec = int(input("Inserisci un numero decimale: "))
    num_bin = ""
    num_loop = num_dec

    while num_loop > 0:
        # Aggiungi la cifra binaria più a destra
        num_bin = str(num_loop % 2) + num_bin
        # Dividi il numero per 2
        num_loop = num_loop // 2

    print(f"Il numero {num_dec} in base 2 è {num_bin}")
    
opzioni = ['Addizione', 'Sottrazione', 'Moltiplicazione', 'Divisione', 'Binario']
while True:
    # Chiedi all'utente di inserire un'operazione
    input_utente = input("""
    Seleziona un'operazione:
     - 1)Addizione
     - 2)Sottrazione
     - 3)Moltiplicazione
     - 4)Divisione
     - 5)Binario
    (Scrivi 'quit', 'q' o 'esci' per uscire.)""")

    # Pulisci l'input: rimuovi spazi e converti tutto in minuscolo
    input_pulito = input_utente.strip().lower()

    # Verifica la condizione di uscita
    if input_pulito in ['quit', 'q', 'esci']:
        break

    # Verifica se l'input è numerico e mappalo alle opzioni
    if input_pulito.isdigit():
        numero_selezionato = int(input_pulito)
        if 1 <= numero_selezionato <= len(opzioni):
            input_pulito = opzioni[numero_selezionato - 1]
        else:
            print("Numero non valido. Riprova.")
            continue

    # Verifica se l'input è tra le opzioni valide
    if input_pulito in opzioni:
        print(f"Hai selezionato l'opzione {input_pulito}.")
        if input_pulito == 'Addizione':
            somma()
        elif input_pulito == 'Sottrazione':
            sottrazione()
        elif input_pulito == 'Moltiplicazione':
            moltiplicazione()
        elif input_pulito == 'Divisione':
            divisione()
        elif input_pulito == 'Binario':
            binario()
        else:
            print("Opzione non valida. Riprova.")


