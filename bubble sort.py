liste=[64, 34, 25, 12, 22, 11, 90]
n=len(liste)
for i in range(n):
    for j in range(n-i-1):
        if liste[j]>liste[j+1]:
            liste[j],liste[j+1]=liste[j+1],liste[j]
            print(liste)


