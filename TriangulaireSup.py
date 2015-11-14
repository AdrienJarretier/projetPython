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





M=[
    [1,2,2],
    [0,1,2],
    [0,0,1]
    ]
print(TriangulaireSup(M))

print(" ")

P=[
    [1,2,3,4],
    [0,0,2,5],
    [4,5,6,9],
    [5,8,6,8]
    ]
print(TriangulaireSup(P))
print(" ")

T=[
    [1,2,3,4],
    [0,1,2,5],
    [0,0,1,9],
    ]
print(TriangulaireSup(T))
