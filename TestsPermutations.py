from Permutations import *

from simplesMatricesFonctions import *

nUplets = [];
matricesPerms = [];

# def testsPermutations() :
for i in range( 5 ) :

    nUplets.append( [] )
    matricesPerms.append( [] )

    for j in range( 4 ) :

        nUplets[ i ].append( PermutationAleatoire( i ) )
        matricesPerms[ i ].append( MatricePermutation( nUplets[ i ][ j ] ) )

# testsPermutations()

def testPermutationAleatoire() :
    for i in range( 2, 5 ) :

        for j in range( 4 ) :

            print("")
            print( "PermutationAleatoire(", i , ") : ", nUplets[i][j] )

def testMatricePermutation() :
    for i in range( 2, 5 ) :

        for j in range( 2 ) :

            print( "MatricePermutation( ", nUplets[i][j] , " ) : " )
            print( tuple( nUplets[i][j] ) )
            print("---"*i)
            AfficherMat( matricesPerms[ i ][ j ] )
            print("")

def testPermutationAssociee() :
    for i in range( 2, len( matricesPerms ) ) :

        for j in range( 1, len( matricesPerms[ i ] ) ) :

            AfficherMat( matricesPerms[ i ][ j ] )
            print( "PermutationAssociee : ", PermutationAssociee( matricesPerms[ i ][ j ] ) )
            print("")


def testEstPermutation() :
    print("#" * 50)
    print(" ")

    print("Fonction EstPermutation :")

    M=[[
            [ 1, 0, 0, 0 ],
            [ 0, 0, 0, 1 ],
            [ 0, 1, 0, 0 ],
            [ 0, 0, 1, 1 ]
        ],
        [
            [ 1, 0, 0, 0 ],
            [ 0, 0, 0, 1 ],
            [ 0, 1, 0, 0 ],
            [ 0, 0, 1, 0 ]
        ],
        [
            [ 1, 0, 0, 0 ],
            [ 0, 0, 0, 0 ],
            [ 0, 1, 0, 0 ],
            [ 0, 0, 0, 1 ]
        ],
        [
            [ 1, 0, 0, 0 ],
            [ 0, 0, 0, 1 ],
            [ 0, 1, 0, 0 ],
        ],
        [
            [ 1, 2, 0 ],
            [ 0, 0, 1 ],
            [ 0, 1, 0 ],
         ]
        ]

    for i in range (len(M)) :
            AfficherMat( M[i] )
            print(" ")
            print("Une matrice de permutation doit :")
            print(" - etre carre,")
            print(" - contenir que des 1 et des 0,")
            print(" - avoir qu'un seul 1 par ligne et par colonne")
            print("Cette matrice est elle une matrice de permutation ?", EstPermutation( M[ i ] ))
            print("-" * 50)
            print(" ")


def testMatricePermutationInverse() :
    print("#" * 50)
    print("Fontion MatricePermutationInverse :")
    MP = [
            [
                    [ 1, 0, 0 ],
                    [ 0, 0, 1 ],
                    [ 0, 1, 0 ]
            ],
            [
                    [ 0, 0, 0, 1 ],
                    [ 1, 0, 0, 0 ],
                    [ 0, 1, 0, 0 ],
                    [ 0, 0, 1, 0 ]
            ],
            [
                    [ 1, 0 ],
                    [ 0, 1 ]
            ]
         ]

    for i in range ( len( MP ) ):
            print("Matrice de permutation :")
            AfficherMat( MP[ i ] )
            print(" ")
            print("L'inverse d'une matrice de permutation est egale a la transposee de la dite matrice")
            print("Inverse de la matrice de permutation :")
            AfficherMat( MatricePermutationInverse( MP[ i ] ))
            print(" ")
            print("-" * 50)


def testProduitPermutG() :
    A = [
            [ 1, 1, 1 ],
            [ 2, 2, 2 ],
            [ 3, 3, 3 ]
        ]
    print("matrice non permutee : ")
    AfficherMat( A )

    for i in range( 3, 4 ) :
        for j in range( len( matricesPerms[ i ] )-1 ) :

            print("")
            print("#"*50)
            print( "ProduitPermutG par : " )
            m = matricesPerms[ i ][ j ]

            AfficherMat( m )
            print("")
            AfficherMat( ProduitPermutG( m, A ) )

    print("")
    print("#"*50)
    print( "ProduitPermutG par : " )
    m = MatId( 3 )

    AfficherMat( m )
    print("")

    AfficherMat( ProduitPermutG( m, A ) )

# # -------------------------------------- ProduitPermutD --------------------------------------

# print("#" * 50)
# print(" ")
# print("Fonction ProduitPermutD :")

# M=[
#         [1,2,3,4],
#         [5,6,7,8],
#         [9,10,11,12],
#         [13,14,15,16]
#     ],

# P=[
#         [0,0,1,0],
#         [0,1,0,0],
#         [0,0,0,1],
#         [1,0,0,0]
#     ]

# AfficherMat( ProduitPermutD( M, P ) )

# print(" ")

if __name__ == "__main__" :

    #testPermutationAleatoire()
    # testMatricePermutation()
    # testPermutationAssociee()
    # testEstPermutation()
    testProduitPermutG()
