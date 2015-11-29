from simplesMatricesFonctions import *
from Decomposition import *

from Matrice_inverse_cofacteurs import produit

def testTriangulaireSup():
        M=[
                [
                        [ 1, 2, 3 ],
                        [ 0, 1, 2 ],
                        [ 0, 0, 3 ]
                ],
                [
                        [ 1, 2, 3 ],
                        [ 4, 5, 6 ],
                        [ 0, 0, 1 ]
                ],
                [
                        [ 1, 2, 3, 6 ],
                        [ 0, 1, 5 ,7 ],
                        [ 0, 0, 2, 3 ]
                ]
                ]
        
        for i in range (len(M)):
                print("La matrice M est :")
                AfficherMat(M[i])
                print("Une matrice triangulaire Superieure doit avoir :")
                print("tous les coefficients sous la diagonale egaux a 0 et etre carree")
                print(" ")
                print("La matrice M est elle une matrice triangulaire superieure ?", TriangulaireSup(M[i]))
                print("-"*50)

def testTriangulaireInf():
        M=[
                [
                        [ 1, 0, 0 ],
                        [ 3, 1, 0 ],
                        [ 4, 5, 3 ]
                ],
                [
                        [ 1, 2, 0 ],
                        [ 4, 5, 6 ],
                        [ 4, 0, 1 ]
                ],
                [
                        [ 1, 0, 0, 0 ],
                        [ 4, 1, 0, 0 ],
                        [ 5, 10, 2, 0 ]
                ]
                ]
        for i in range (len(M)):
                print("La matrice M est :")
                AfficherMat(M[i])
                print("Une matrice triangulaire Inferieure doit avoir :")
                print("tous les coefficients au dessus de la diagonale egaux a 0 et etre carree")
                print(" ")
                print("La matrice M est elle une matrice triangulaire inferieure ?", TriangulaireInf(M[i]))
                print("-"*50)

def testDecompositionPLU() :
        mTests = [
                                [
                                        [ 4, -9, 2 ],
                                        [ 2, -4, 4 ],
                                        [ -1, 2, 2 ]
                                ],

                                [
                                        [ 2, 4, 2, 0 ],
                                        [ 1, 2, 1, 0 ],
                                        [ 1, 2, 1, 3 ],
                                        [ 1, 2, 2, 1 ]
                                ],

                                [
                                        [ 0, 3, 1 ],
                                        [ 4, 1, 1 ],
                                        [ 2, 2, 4 ]
                                ],

                                [
                                        [ -6, 6 ],
                                        [ -2, -4 ]
                                ],

                                [
                                        [ 1, 1 ],
                                        [ 2, -2 ]
                                ]

                         ]

        for A in mTests :
                print("#"*50)
                print("decomposition PLU de : ")

                AfficherMat( A )

                PLU = DecompositionPLU( A )

                matName = [ "P", "L", "U" ]

                for i in range( 3 ) :
                        print("")
                        print( matName[ i ], ":")
                        AfficherMat( PLU[ i ] )

                print("")
                print("produit P * L * U")
                print("( lourd, pour tester si on retrouve la matrice de depart ) :")
                AfficherMat( produit( produit( PLU[0], PLU[1] ), PLU[2] ) )

                print("")
        print("@"*100)

if __name__ == "__main__":
        testDecompositionPLU()
        testTriangulaireSup()
        testTriangulaireInf()
