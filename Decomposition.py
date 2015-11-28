from simplesMatricesFonctions import *

from Permutations import *
from Transvections import *

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
            L = ProduitPermutD ( L, MatricePermutationInverse( P ) )

            pivot = A[lig][col]

            for j in range ( lig+1, n ):
                x = -( A[j][col]/pivot )

                T = MatriceTransvection( j+1, x , lig+1 )


                A = ProduitTransvectionG( T, A )

                L = ProduitTransvectionD( L , MatriceTransvectionInverse(T) )


            lig+=1
            col+=1

        L = ProduitPermutG ( MatricePermutationInverse ( P ), L )
        U = A

    return (P, L, U)
