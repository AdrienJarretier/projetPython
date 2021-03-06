from Transvections import *
from Matrice_inverse_cofacteurs import inverse, produit

def testMatriceTransvection() :
    print("")
    print("*"*32, "****************************", "*"*32)
    print("*"*32, "Tests de MatriceTransvection", "*"*32)

    def afficherTest( t ) :
        print("")
        print( "MatriceTransvection", t, " : " )
        print( "matrice (", max( t[0], t[2] ), ",", max( t[0], t[2] ), ")" )
        print( "coefficient :", t[1], ", ligne :",t[0], ", colonne :" ,t[2] )
        Mt = MatriceTransvection( t[0], t[1], t[2] )
        AfficherMat( Mt )

    t = ( 1, 3, 3 )
    afficherTest( t )

    t = ( 3, 12, 5 )
    afficherTest( t )

    t = ( 3, 2, 1 )
    afficherTest( t )

    print("")
    print("*"*32, "                            ", "*"*32)
    print("*"*32, "****************************", "*"*32)
    print("")




def testEstTransvection() :
    print("")
    print("*"*32, "************************", "*"*32)
    print("*"*32, "Tests de EstTransvection", "*"*32)

    M=[ [
        [1,0,0],
        [0,1,0],
        [0,0,1]
        ],
        [
        [1,0,0],
        [0,1,0],
        [1,0,1]
        ],
        [
        [1,0,0],
        [1,1,1],
        [0,0,1]
        ],
        [
        [1,0,0,0,0],
        [2,2,0,0,0],
        [0,0,1,0,0],
        [3,2,1,1,0],
        [4,0,0,0,1]
        ]
        ]
    for i in range( len ( M ) ):
            print("La matrice M est :")
            AfficherMat( M[ i ] )
            print("Une matrice de transvection doit :")
            print(" - avoir tous ces coefficients diagonaux egaux a 1")
            print(" - avoir un seul (ou aucuns) coefficient non diagonal different de 0")
            print(" ")
            print("La Matrice M est elle une matrice de transvection ?")
            print( EstTransvection( M[ i ] ) )
            print("-"*50)


    print("")
    print("*"*32, "                        ", "*"*32)
    print("*"*32, "************************", "*"*32)
    print("")





def testMatriceTransvectionInverse() :
    print("")
    print("*"*32, "***********************************", "*"*32)
    print("*"*32, "Tests de MatriceTransvectionInverse", "*"*32)

    def afficherTest(M,i,j,a):
        print("")
        print("Matrice :")
        AfficherMat(M)
        print( "inverse en calculant les cofacteurs ( lourd, ici pour test et comparer ) : " )
        AfficherMat( inverse( M ) )
        print("")
        print("Inverse de la matrice de transvection :")
        print("Ici la diagonale formee de 1 ne doit pas changer alors que le",a," de la colonne ",j," et de la ligne ",i," doit etre remplace par " ,-a)
        AfficherMat(MatriceTransvectionInverse(M))
        print(" ")



    print("Matrice de transvection Inverse :")

    M=[
        [1,0,0],
        [0,1,1],
        [0,0,1]
        ]
    afficherTest(M,2,3,1)

    P=[
        [1,0,0,0],
        [0,1,0,0],
        [3,0,1,0],
        [0,0,0,1]
        ]
    afficherTest(P,3,1,3)

    T=[
        [1,0,0,0,0,0],
        [0,1,0,0,0,5],
        [0,0,1,0,0,0],
        [0,0,0,1,0,0],
        [0,0,0,0,1,0],
        [0,0,0,0,0,1]
        ]
    afficherTest(T,2,6,5)

    R=[
        [1,0],
        [2,1],
        ]
    afficherTest(R,2,2,2)

    print("")
    print("*"*32, "                                   ", "*"*32)
    print("*"*32, "***********************************", "*"*32)
    print("")



def testProduitTransvectionG() :
    print("")
    print("*"*32, "*****************************", "*"*32)
    print("*"*32, "Tests de ProduitTransvectionG", "*"*32)
    print(" ---------------- ProduitTransvectionG -------------------")
    M=[
        [1,1,1],
        [2,2,2],
        [3,3,3],
        [4,4,4]
        ]

    a = 2
    i = 1
    j = 3
    t = MatriceTransvection( i, a, j )
    print("La matrice de depart est :")
    AfficherMat(M)
    print(" ")
    print("a=",a,"i=",i,"j=",j)
    print(" ")
    print("La ligne ",i," va être remplacee par la ligne ",i,"+ la ligne ",j,"*",a)
    print("On obtient la matrice :")
    AfficherMat( ProduitTransvectionG( t, M ) )
    print("-"*50)

    print(" ---------------- ProduitTransvectionG -------------------")
    M=[
        [4,5,6],
        [8,9,10],
        [2,1,5],
        [1,1,1]
        ]

    a = 2
    i = 3
    j = 4
    t = MatriceTransvection( i, a, j )
    print("La matrice de depart est :")
    AfficherMat(M)
    print(" ")
    print("a=",a,"i=",i,"j=",j)
    print(" ")
    print("La ligne ",i," va être remplacee par la ligne ",i,"+ la ligne ",j,"*",a)
    print("On obtient la matrice :")
    AfficherMat( ProduitTransvectionG( t, M ) )
    print("-"*50)

    
    print(" ---------------- ProduitTransvectionG -------------------")
    M=[
        [1, 10, 20, 5],
        [2, 2, 5, 1],
        [10, 4, 5, 7],
        [2, 2, 2, 2]
        ]

    a = 1
    i = 1
    j = 4
    t = MatriceTransvection( i, a, j )
    print("La matrice de depart est :")
    AfficherMat(M)
    print(" ")
    print("a=",a,"i=",i,"j=",j)
    print(" ")
    print("La ligne ",i," va être remplacee par la ligne ",i,"+ la ligne ",j,"*",a)
    print("On obtient la matrice :")
    AfficherMat( ProduitTransvectionG( t, M ) )
    print("-"*50)

    print(" ---------------- ProduitTransvectionG -------------------")
    M=[
        [1,2],
        [2,3],
        [3,3],
        [4,4],
        [1,1]
        ]

    a = 2
    i = 1
    j = 5
    t = MatriceTransvection( i, a, j )
    print("La matrice de depart est :")
    AfficherMat(M)
    print(" ")
    print("a=",a,"i=",i,"j=",j)
    print(" ")
    print("La ligne ",i," va être remplacee par la ligne ",i,"+ la ligne ",j,"*",a)
    print("On obtient la matrice :")
    AfficherMat( ProduitTransvectionG( t, M ) )
    print("-"*50)


    print("")
    print("*"*32, "                             ", "*"*32)
    print("*"*32, "*****************************", "*"*32)
    print("")




def testProduitTransvectionD() :
    print("")
    print("*"*32, "*****************************", "*"*32)
    print("*"*32, "Tests de ProduitTransvectionD", "*"*32)

    def afficherTest( M, i, a, j ) :

            T = MatriceTransvection( i, a, j, len( M[0] ) )

            print("matrice de transvection : ")
            AfficherMat( T )
            print("")
            print("matrice sur laquelle appliquer la transvection :")
            AfficherMat( M )
            print("")
            print("resultat attendu : ")
            print("C"+str(j),"<= C"+str(j),"+",a,"* C"+str(i), "=", M[0][j-1]+a*M[0][i-1] )
            print("")
            print("resultat de la fonction ProduitTransvectionD :")
            AfficherMat( ProduitTransvectionD( M, T ) )
            print("")
            print("produit en utilisant la methode classique et lourde pour comparer : ")
            try :
                    AfficherMat( produit( M, T ) )
            except Exception as inst:
                    print("")
                    print( inst )
                    print("")
            print("")



    A = [
            [ 1, 2, 3, 4, 5 ],
            [ 1, 2, 3, 4, 5 ],
            [ 1, 2, 3, 4, 5 ]
    ]

    tests = [
                    ( A, 4, 0, 5 ),
                    ( A, 4, 3, 5 ),
                    ( A, 2, 1, 1 ),
                    ( A, 1, 10, 2 ),
                    ( A, 1, 10, 3 )
                    ]

    print( "A : " )
    AfficherMat( A )

    for t in tests :
            try :
                    print("-"*30, "testProduitTransvectionD( A," , t[1], ",", t[2], ",", t[3], ")", "-"*30 )
                    afficherTest( t[0], t[1], t[2], t[3] )
                    print("")
            except Exception as inst:
                    print("")
                    print( "(", t[1], ",", t[2], ",", t[3],") :",inst )
                    print("")

    print("")
    print("*"*32, "                             ", "*"*32)
    print("*"*32, "*****************************", "*"*32)
    print("")



def testTransvectionAssociee() :
    print("")
    print("*"*32, "*****************************", "*"*32)
    print("*"*32, "Tests de TransvectionAssociee", "*"*32)
    print("")

    def afficherTest( t ) :

            i = t[ 0 ]
            a = t[ 1 ]
            j = t[ 2 ]

            try :
                    Mt = MatriceTransvection( i, a, j )
                    print( "Mt : " )
                    AfficherMat( Mt )

                    if a != 0 :
                            print( "Attendu :", (i, a, j) )
                    else :
                            print( "Attendu : (1, 0, 1) car alpha == 0, la transvection n'aura aucun effet" )

                    print( "resultat de la fonction TransvectionAssociee a Mt :" )
                    print( TransvectionAssociee( Mt ) )
                    print("")

            except Exception as inst :
                    print( inst )

    tests = [
                            ( 1, 2, 2 ),
                            ( 4, 2, 2 ),
                            ( 1, 0, 2 ),
                            ( 20, 10, 20 )
                    ]

    for t in tests :
            print("-"*30, "TransvectionAssociee", t, "-"*30 )
            afficherTest( t )
            print("")

    print("")
    print("*"*32, "                             ", "*"*32)
    print("*"*32, "*****************************", "*"*32)
    print("")



if __name__=="__main__":
        testMatriceTransvection()
        testEstTransvection()
        testMatriceTransvectionInverse()
        testProduitTransvectionG()
        testProduitTransvectionD()
        testTransvectionAssociee()
