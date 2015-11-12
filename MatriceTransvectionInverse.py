##MatriceTransvectionInverse
##
##Entree :
##	M : Liste de listes : Matrice de transvection
##
##Sortie :
##	M : Liste de listes : matrice inverse de M

def MatriceTransvectionInverse (M):
    n=len( M )
    for i in range( n ) :
        for j in range( n ) :
            if i != j and M[i][j] != 0 :
                M[i][j] = - M[i][j]
    return M



