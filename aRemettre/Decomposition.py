from simplesMatricesFonctions import *
from Permutations import *
from Transvections import *

# TriangulaireSup
# Entree :
#   M : Matrice de taille n*n
# Sortie :
#   Booleen qui renvoie si la matrice est triangulaire superieure
#
# Fonctionnement :
#   On verifie que la matrice est bien une matrice carree
#   Puis on regarde si les coefficients sous la diagonale sont egaux a 0

def TriangulaireSup ( M ):
    n = len( M )
    if n != len( M[0] ):
        return False 
    for i in range( n ):
        for j in range ( i ):
            if M[i][j] != 0:
                return False
    return True


## TriangulaireInf
## Entree :
##    M : matrice de taille n*p
## Sortie :
##    Booleen indiquant si la matrice est triangulaire superieure
##
## Fonctionnement :
##      On verifie que la matrice est bien une matrice carree
##      Puis on regarde si les coefficients au dessus de la diagonale sont egaux a 0

def TriangulaireInf ( M ):
    n=len(M)
    if n!=len(M[0]):
        return False
    for i in range ( n ):
        for j in range ( i+1 , n ):
            if M[i][j] != 0 :
                return False
    return True



'''
DecompositionPLU

Decomposition en 3 matrices P, L et U
de la matrice carree donnee en entree

A peut se decomposer
sous la forme du produit de 3 matrices
sous la forme : A = PLU

Entree :
	A : liste de listes : Matrice carree

Sortie :
	P : liste de listes : Matrice de permutation
	L : liste de listes : Matrice triangulaire inferieure
	U : liste de listes : Matrice triangulaire superieure

'''
def DecompositionPLU ( A ):
    n = len( A )

    lig = 0 # Indice de la ligne courante
    col = 0 # Indice de la colonne courante

    P = MatId( n ) # Initialisation de P
    L = MatId( n ) # Initilaisation de L

    while lig < n and col < n :
        Trouve = False
        # booleen : False si on a trouve aucun pivot dans la colonne

        lp = 0 # ligne du pivot

        for i in range ( lig , n ):
            if A[i][col] != 0 :
                lp = i
                Trouve = True
                break

        if not Trouve :
            col += 1

        else :
            # Creation de la matrice Paux
            permut = list( range( 1, n+1 ) )
            permut[ lig ] = lp + 1
            permut[ lp ] = lig + 1
            Paux = MatricePermutation ( permut )

            A = ProduitPermutG ( Paux, A )
            P = ProduitPermutG ( Paux, P )
            L = ProduitPermutD ( L, MatricePermutationInverse( Paux ) )

            pivot = A[lig][col]

            for j in range ( lig+1, n ):
                x = -( A[j][col]/pivot )

                T = MatriceTransvection( j+1, x , lig+1 )

                # print("**DEBUG**  T : ")
                # AfficherMat( T )

                A = ProduitTransvectionG( T, A )

                L = ProduitTransvectionD( L , MatriceTransvectionInverse(T) )


            lig+=1
            col+=1

    L = ProduitPermutG ( MatricePermutationInverse ( P ), L )
    U = A

    return (P, L, U)
