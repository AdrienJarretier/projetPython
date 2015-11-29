from simplesMatricesFonctions import *
from Applications import *

def testDeterminantPLU() :
        print(" ----------------- Determinant PLU ------------")

        print(" Determinant PLU :")

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

                AfficherMat( A )

                detA = DeterminantPLU( A )

                print("")
                print( "determinant :", detA)




def TestResolutionTriSupCramer () :
        print(" # "*50)
        A1Tests = [
                        [
                                [ 1, 1, 1 ],
                                [ 0, 1, 1 ],
                                [ 0, 0, 1 ]
                        ],

                        [
                                [ 2, 2, 2, 2 ],
                                [ 0, 2, 2, 2 ],
                                [ 0, 0, 2, 2 ],
                                [ 0, 0, 0, 2 ]
                        ],

                        [
                                [ 3, 3 ],
                                [ 0, 3 ]

                        ],
                        [
                                [ 1, 2, 3 ],
                                [ 0, 4, 5 ],
                                [ 0, 0, 6 ]
                        ]


                  ]


        B1Tests = [
                        [ 1, 1, 1 ],
                        [ 0, 2, 1, 3 ],
                        [ 1, 2 ],
                        [ 6, 6, 6 ]
                  ]

        SolAttendues1 = [
                                [ 0, 0, 1 ],
                                [ -1, 0.5, -1, 1.5 ],
                                [ -1/3, 2/3 ],
                                [ 2.5, 0.25, 1 ]
                        ]

        for i in range ( len( A1Tests ) ):
                print(" ----------------- ResolutionTriSupCramer ------------")
                print("Systeme a resoudre :")
                print(" Matrice A :")
                AfficherMat( A1Tests[ i ] )
                print( " " )
                print( " Second membre " )
                AfficherMat( B1Tests[ i ] )
                print(" ")
                print(" Solution du systeme A * X = B attendue :")
                print(SolAttendues1[ i ])
                print(" ")
                print("Solutions du systeme A * X = B trouvée :")
                print(ResolutionTriSupCramer( A1Tests[ i ], B1Tests[ i ] ) )
                print(" ")
                print("-" * 50)



def TestResolutionTriInfCramer () :
        print(" # "*50)
        A2Tests = [
                        [
                                [ 1, 0, 0 ],
                                [ 1, 1, 0 ],
                                [ 1, 1, 1 ]
                        ],

                        [
                                [ 2, 0, 0, 0 ],
                                [ 2, 2, 0, 0 ],
                                [ 2, 2, 2, 0 ],
                                [ 2, 2, 2, 2 ]
                        ],

                        [
                                [ 1, 0 ],
                                [ 2, 3 ]

                        ],
                        [
                                [ 1, 0, 0 ],
                                [ 2, 3, 0 ],
                                [ 4, 5, 6 ]

                        ]
                  ]

        B2Tests = [
                        [ 1, 1, 1 ],
                        [ 0, 2, 1, 3 ],
                        [ 1, 2 ],
                        [ 6, 6, 6 ]
                  ]

        SolAttendues2 = [
                                [ 1, 0, 0 ],
                                [ 0, 1, -0.5, 1 ],
                                [ 1, 0 ],
                                [ 6, -2, -4/3 ]
                        ]

        for i in range ( len( A2Tests ) ):
                print(" ----------------- ResolutionTriInfCramer ------------")
                print("Systeme a resoudre :")
                print(" Matrice A :")
                AfficherMat( A2Tests[ i ] )
                print( " " )
                print( " Second membre " )
                AfficherMat( B2Tests[ i ] )
                print(" ")
                print(" Solution du systeme A * X = B attendue :")
                print(SolAttendues2[ i ])
                print(" ")
                print("Solutions du systeme A * X = B trouvée :")
                print(ResolutionTriInfCramer( A2Tests[ i ], B2Tests[ i ] ) )
                print(" ")
                print("-" * 50)

def TestResolutionCramer ():
        print(" # "*50)
        print(" ----------------- ResolutionCramer ------------")
        A=[
            [ 5, 8, 9, 10, 8 ],
            [ 4, 5, 6, 4, 6 ],
            [ 7, 8, 10, 5, 9 ],
            [ 11, 8, 4, 9, 2 ],
            [ 9, 4, 12, 3, 1 ]
            ]

        B = [ 1, 4, 5, 7, 8 ]

        P, L, U = DecompositionPLU(A)
        print("Soit la matrice A :")
        AfficherMat(A)
        print(" ")
        print("Et le second membre B :")
        AfficherMat(B)
        print(" ")
        print("La decomposition PLU de A est :")
        print("Matrice P :")
        AfficherMat(P)
        print(" ")
        print("Matrice L :")
        AfficherMat(L)
        print(" ")
        print("Matrice U :")
        AfficherMat(U)
        print(" ")
        print("Les solutions du systeme A*X = B sont :")
        try :
            print(ResolutionCramer( A,B ))
        except Exception as mess :
            AfficherMat(mess.args[1])
            print(mess.args[0])

        print(" ")
        print(" Or les solutions trouvees sur sage sont :")
        print(5431/1514)
        print(-4317/757)
        print(-971/1514)
        print(1657/1514)
        print(2225/757)
        print("Nous constatons que nous obtenons les memes solutions")
        print("alors que la decomposition PLU est differente sur sage")
       

if __name__ == "__main__":

        testDeterminantPLU()
        TestResolutionTriSupCramer ()
        TestResolutionTriInfCramer ()
        TestResolutionCramer ()
