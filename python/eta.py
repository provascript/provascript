# Chiedi all'utente di inserire l'età
eta = int(input("Inserisci la tua età: "))

if eta < 1 or eta > 25:
    print("Fuori età scolastica")
elif 1 <= eta <= 6:
    print("Scuola dell'infanzia")
elif 6 < eta <= 11:
    print("Scuole elementari")
elif 11 < eta <= 14:
    print("Scuole medie")
elif 14 < eta <= 19:
    print("Scuole superiori")
elif 19 < eta <= 25:
    print("Stai facendo l'università?")
