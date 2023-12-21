n = int(input("Inserisci il valore per il range: "))

for i in range(n):
    for j in range(n):
        if (j == 0 or j == j//2) or ((i == 0 or i == n//2-1 or (j == n-1 or i <= n//2-1))) and (j > 0 and j < n+1):
            print("P", end="")
        else:
            print("", end="")
    print()