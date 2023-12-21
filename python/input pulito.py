opzioni = ['uno', 'due', 'tre', 'quattro', 'altro']

while True:
    # Chiedi all'utente di inserire un'operazione
    input_utente = input("""
    Seleziona un'operazione:
     - Addizione
     - Sottrazione
     - Moltiplicazione
     - quattro
     - altro
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
        # Aggiungi qui il codice per l'opzione selezionata
    else:
        print("Opzione non valida. Riprova.")
