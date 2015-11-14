from MatricesTransvection.MatriceTransvection import *
from simplesMatricesFonctions import *

def testMatriceTransvection( t ) :
    print("")
    print( "MatriceTransvection", t, " : " )
    print( "matrice (", max( t[0], t[2] ), ",", max( t[0], t[2] ), ")" )
    print( "coefficient :", t[1], ", ligne :",t[0], ", colonne :" ,t[2] )
    Mt = MatriceTransvection( t[0], t[1], t[2] )
    AfficherMat( Mt )

t = ( 1, 3, 3 )
testMatriceTransvection( t )

t = ( 3, 12, 5 )
testMatriceTransvection( t )

t = ( 3, 2, 1 )
testMatriceTransvection( t )
