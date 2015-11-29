# TriangulaireSup

# Entree :
#   M : Matrice de taille n*n
# Sortie :
#   Booleen qui renvoie si la matrice est triangulaire superieure

def TriangulaireSup ( M ):
    n = len( M )
    if n != len( M[0] ):
        return False 
    for i in range( n ):
        for j in range ( i ):
            if M[i][j] != 0:
                return False
    return True


A = [
    [1,1,1,1],
    [0,1,1,1],
    [0,0,1,1],
    [0,0,0,1]
    ]
print(TriangulaireSup(A))
