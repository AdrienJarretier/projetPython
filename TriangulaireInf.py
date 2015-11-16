## TriangulaireInf
## Entree :
##    M : matrice de taille n*p
## Sortie :
##    Booleen indiquant si la matrice est triangulaire superieure

def TriangulaireInf ( M ):
    n=len(M)
    if n!=len(M[0]):
        return False
    for i in range ( n ):
        for j in range ( i+1 , n ):
            if M[i][j] != 0 :
                return False
    return True


