from Decomposition import  *
from TriangulaireInf import*
from TriangulaireSup import*

##Entree :
##    P : une matrice de permutation
##Sortie :
##    Determinant de la matrice de permutation
##
##Fonctionnement :
##    P etant une matrice permutation son determinant sera (-1)**a ou a est le nombre de
##    permutations necessaires pour obtenir la matrice identite Idn.
##    On utilise la fonction PermutationAssociee pour obtenir le n-uplet de la matrice de
##    permutation P puis on compte combien de permutations sont necessaires pour retrouver
##    la matrice identite.

def DeterminantMatricePerm( P ) :

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

    return ( -1 )**CPermutations

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

    P, L, U = DecompositionPLU( M )

    detP = DeterminantMatricePerm( P );

    detU = 1

    for i in range ( len( U ) ):

        detU *= U[ i ][ i ]

    return detP * detU



##ResolutionTriSupCramer
##
##Entree :
##    A : une matrice triangulaire superieure de taille n*n
##    B : second membre de taille n
##Sortie :
##    Les solutions du systeme de l'equation : A * X = B

def ResolutionTriSupCramer( A,B ) :
    n = len(A)
    if not TriangulaireSup( A ) :
        raise Exception ("Ceci n'est pas une matrice triangulaire", A)
    for i in range( n ):
        if A[ i ][ i ] == 0 :
            raise Exception ("Ceci n'est pas un systeme de Cramer car tous les \
                                     coefficients diagonaux ne sont pas non nuls", A)
    X = list ( range ( n ) )
    X[ n-1 ] = B[ n-1 ] / A[ n-1 ][ n-1 ]
    for i in reversed (range ( n-1 )):
        S = 0
        for j in range ( i+1,n ) :
            S += A[ i ][ j ] * X[ j ]
        X[ i ] = ( B[ i ] - S ) / A[ i ][ i ]
    return X


##ResolutionTriInfCramer
##
##Entree :
##    A : une matrice triangulaire inferieure de taille n*n
##    B : second membre de taille n*1
##Sortie :
##    Les solutions du systeme de l'equation : A * X = B

def ResolutionTriInfCramer( A,B ):
    n = len(A)
    if not TriangulaireInf( A ):
         raise Exception ("Ceci n'est pas une matrice triangulaire", A)
    for i in range( n ):
        if A[ i ][ i ] == 0 :
            raise Exception ("Ceci n'est pas un systeme de Cramer car tous les \
                                     coefficients diagonaux ne sont pas non nuls", A)
    X = list ( range ( n ) )
    X[ 0 ] = B[ 0 ] / A[ 0 ][ 0 ]
    for i in range ( 1,n ):
        S=0
        for j in range ( i ):
            S+=A[ i ][ j ] * X [ j ]
        X[ i ] = ( B[ i ] - S ) / A[ i ][ i ]
    return X

##ResolutionCramer
##
##Entree :
##    A : une matrice carree de taille n*n
##    B : second membre de taille n*1
##Sortie :
##    Les solutions du systeme de l'equation : A * X = B

##Fonctionnement :
##    On decompose la matrice A en PLU. Puis on applique la fonction
##    ResolutionTriInfCramer a L et P^T*B en resolvant : L * Y = P^T * B
##    (ou Y est l'inconnue).
##    Enfin on applique la fonction ResolutionTriSupCramer a U et Y (Y ayant ete
##    trouve juste avant).
##     Ainsi on obtiendra les solutions de l'equation : A * X = B.


def ResolutionCramer( A,B ):
    if DeterminantPLU( A ) == 0 :
        raise Exception ("Cette matrice n'est pas un systeme de Cramer")

    P, L, U = DecompositionPLU( A )

    Y = ResolutionTriInfCramer( L, ProduitPermutG ( MatricePermutationInverse( P ),B ) )

    return ResolutionTriSupCramer( U,Y )

A=[
    [ 5, 8, 9, 10, 8 ],
    [ 4, 5, 6, 4, 6 ],
    [ 7, 8, 10, 5, 9 ],
    [ 11, 8, 4, 9, 2 ],
    [ 9, 4, 12, 3, 1 ]
    ]

B = [ 1, 4, 5, 7, 8 ]






try :
    print(ResolutionCramer( A,B ))
except Exception as mess :
    AfficherMat(mess.args[1])
    print(mess.args[0])
