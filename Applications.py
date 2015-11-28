##DeterminantPLU 
##
##Entree : 
##	M : Matrice carree de taille n*n
##Sortie : 
##	Le determinant de la matrice M
##
##Fonctionnement : 
##On decompose la matrice M en : M = PLU 
##On sait que : det(M) = det(P) * det(L) * det(U)
##Donc une fois la decomposition de M obtenue on calcule le determinant de chaque matrice :
##	- P etant une matrice permutation son determinant sera (-1)**a ou a est le nombre de
##	permutations necessaires pour obtenir la matrice identite Idn
##	
##	- L etant une matrice triangulaire son determinant est le produit de ses coefficients
##	diagonaux or L etant les produits successifs de matrices de transvection tous ses termes
##	diagonaux seront egaux a 1 donc son determinant sera 1 ( donc det(M) = det(P) * det(U) )
##	
##	- U etant une matrice triangulaire son determinant est le produit de ses coefficients
##	diagonaux (ici tous non nuls car on se restreint a des systemes de Cramer)


def DeterminantPLU( M ) :
    detP = 0
    detU = 1
    P, L, U = DecompositionPLU( M )
    ListePermu = PermutationAssociee( P )
    CPermutations = 0
    tmp=0
    
    for i in range (len (ListePermu) ) :
        if ListePermu[ i ] != ( i+1 ) :
            for j in range ( i+1, len( ListePermu ) ):
                if ListePermu[ j ] == ( i+1 ):
                    CPermutations += 1
                    tmp = ListePermu[ i ]
                    ListePermu[ i ] = ListePermu[ j ]
                    ListePermu[ j ] = tmp
                    break
    detP = ( -1 )**Cpermutations
    print("DEBUG detP :", detP)
    print(" ")
    
    for i in range ( len( ListePermu ) ):
        detU *= ListePermu[ i ][ i ]
    print("DEBUG detU :", detU)
    print(" ")
    return detP * detU

    
                
