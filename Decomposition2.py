from simplesMatricesFonctions import *
from Permutations import *
from Transvections import *


def DecompositionPLU ( A ):
    n = len( A )
    lig = 0 # Indice de la ligne courante
    col = 0 # Indice de la colonne courante
    P = MatId( n ) # Initialisation de P
    L = MatId( n ) # Initilaisation de L

    while lig < n and col < n :
        Trouve = False
        lp = 0
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
##                print("DEBUG T :")
##                AfficherMat(T)
                

                A = ProduitTransvectionG( T, A )
                #M=MatriceTransvection(j+1, -x, lig+1)
                #M=MatriceTransvectionInverse(T)
                L = ProduitTransvectionD( L , MatriceTransvectionInverse(T) )
                

            lig+=1
            col+=1

        L = ProduitPermutG ( MatricePermutationInverse ( P ), L )
        U = A
        
    
    print("P :")
    AfficherMat(P)
    print(" ")
    print("L :")
    AfficherMat(L)
    print(" ")
    print("U :")
    AfficherMat(U)
    return (P, L, U)

##A=[
##    [4, -9, 2],
##    [2, -4, 4],
##    [-1, 2, 2]
##    ]
##
##print(DecompositionPLU(A))
##
##B=[
##    [2,4,2,0],
##    [1,2,1,0],
##    [1,2,1,3],
##    [1,2,2,1]
##    ]
##print(DecompositionPLU(B))
