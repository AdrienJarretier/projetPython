from Permutations import *

from simplesMatricesFonctions import *

nUplets = [];
matricesPerms = [];


for i in range( 5 ) :

    nUplets.append( [] )
    matricesPerms.append( [] )

    for j in range( 4 ) :

        nUplets[ i ].append( PermutationAleatoire( i ) )
        matricesPerms[ i ].append( MatricePermutation( nUplets[ i ][ j ] ) )



def testPermutationAleatoire() :
    print("")
    print("*"*32, "*****************************", "*"*32)
    print("*"*32, "Tests de PermutationAleatoire", "*"*32)

    for i in range( 2, 5 ) :

        for j in range( 4 ) :

            print("")
            print( "PermutationAleatoire(", i , ") : ", nUplets[i][j] )

    print("")
    print("*"*32, "                             ", "*"*32)
    print("*"*32, "*****************************", "*"*32)
    print("")



def testMatricePermutation() :
    print("")
    print("*"*32, "***************************", "*"*32)
    print("*"*32, "Tests de MatricePermutation", "*"*32)

    for i in range( 2, 5 ) :

        for j in range( 2 ) :

            print("")
            print( "MatricePermutation( ", nUplets[i][j] , " ) : " )
            print( tuple( nUplets[i][j] ) )
            print("---"*i)
            AfficherMat( matricesPerms[ i ][ j ] )

    print("")
    print("*"*32, "                           ", "*"*32)
    print("*"*32, "***************************", "*"*32)
    print("")



def testPermutationAssociee() :
    print("")
    print("*"*32, "****************************", "*"*32)
    print("*"*32, "Tests de PermutationAssociee", "*"*32)

    for i in range( 2, len( matricesPerms ) ) :

        for j in range( 1, len( matricesPerms[ i ] ) ) :

            print("")
            AfficherMat( matricesPerms[ i ][ j ] )
            print( "PermutationAssociee : ", PermutationAssociee( matricesPerms[ i ][ j ] ) )

    print("")
    print("*"*32, "                            ", "*"*32)
    print("*"*32, "****************************", "*"*32)
    print("")



def testEstPermutation() :
    print("")
    print("*"*32, "***********************", "*"*32)
    print("*"*32, "Tests de EstPermutation", "*"*32)

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
        print(" ")
        AfficherMat( M[i] )
        print(" ")
        print("Une matrice de permutation doit :")
        print(" - etre carre,")
        print(" - contenir que des 1 et des 0,")
        print(" - avoir qu'un seul 1 par ligne et par colonne")
        print(" ")
        print("Cette matrice est elle une matrice de permutation ?", EstPermutation( M[ i ] ))
        print("-" * 50)
        print(" ")

    print("")
    print("*"*32, "                       ", "*"*32)
    print("*"*32, "***********************", "*"*32)
    print("")


def testMatricePermutationInverse() :
    print("")
    print("*"*32, "**********************************", "*"*32)
    print("*"*32, "Tests de MatricePermutationInverse", "*"*32)

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
            print("")
            print("Matrice de permutation :")
            AfficherMat( MP[ i ] )
            print(" ")
            print("L'inverse d'une matrice de permutation est egale a la transposee de la dite matrice")
            print("Inverse de la matrice de permutation :")
            AfficherMat( MatricePermutationInverse( MP[ i ] ))
            print(" ")
            print("-" * 50)

    print("")
    print("*"*32, "                                  ", "*"*32)
    print("*"*32, "**********************************", "*"*32)
    print("")



def testProduitPermutG() :
    print("")
    print("*"*32, "***********************", "*"*32)
    print("*"*32, "Tests de ProduitPermutG", "*"*32)
    print("")

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

    print("")
    print("*"*32, "                       ", "*"*32)
    print("*"*32, "***********************", "*"*32)
    print("")



def testProduitPermutD() :
    print("")
    print("*"*32, "***********************", "*"*32)
    print("*"*32, "Tests de ProduitPermutD", "*"*32)
    print("")

    A=[
            [1,2,3],
            [1,2,3],
            [1,2,3]
        ]

    print("matrice non permutee : ")
    AfficherMat( A )

    for i in range( 3, 4 ) :
        for j in range( len( matricesPerms[ i ] )-1 ) :

            print("")
            print("#"*50)
            print( "ProduitPermutD par : " )
            m = matricesPerms[ i ][ j ]

            AfficherMat( m )
            print("")
            AfficherMat( ProduitPermutD( A, m ) )

    print("")
    print("#"*50)
    print( "ProduitPermutD par : " )
    m = MatId( 3 )

    AfficherMat( m )
    print("")

    AfficherMat( ProduitPermutD( A, m ) )

    print("")
    print("*"*32, "                       ", "*"*32)
    print("*"*32, "***********************", "*"*32)
    print("")





if __name__ == "__main__" :

    testPermutationAleatoire()
    testMatricePermutation()
    testPermutationAssociee()
    testEstPermutation()
    testMatricePermutationInverse()
    testProduitPermutG()
    testProduitPermutD()
