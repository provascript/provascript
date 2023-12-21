# Creazione della lista
tabellina_quattro = [prodotti for prodotti in range(0, 41, 4)]

# Utilizzo del metodo reverse()
tabellina_quattro.reverse()
print("Lista invertita con reverse():", tabellina_quattro)

# Utilizzo dell'operatore di slicing
al_contrario = tabellina_quattro[::-1]
print("Lista invertita con slicing:", al_contrario)
