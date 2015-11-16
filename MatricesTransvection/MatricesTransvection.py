from simplesMatricesFonctions import *
from copy import deepcopy


##MatriceTransvection
##
##On notera une transvection : t(i,a,j)
##
##Matrice identite + a * Matrice Eij
##
##Entree :
##    i : entier : indice de la ligne/colonne à remplacer : 1 <= i
##    a : reel : coefficient de multiplication de la ligne/colonne j : a != 0
##    j : entier : indice de la ligne/colonne de remplacement : 1 <= j ET j != i
##Sortie :
##    Liste de listes : Matrice de transvection
##
def MatriceTransvection( i, a, j ) :

	if i == j or i < 1 or j < 1 :
		raise Exception( "'i' et 'j' doivent etre differents et superieurs a 0" )
	elif a == 0 :
		raise Exception( "'a' doit etre different de 0" )
	else :
		Id = MatId( max( i, j ) )
		Id[ i - 1 ][ j - 1 ] = a
		return Id



##EstTransvection
##
##uniquement des 1 dans la diagnonale
##et des 0 partout sauf un et un seul element
##
##Entree :
##	M : Liste de listes : Matrice
##
##Sortie :
##	Booleen : vrai si M est une matrice de transvection

def EstTransvection(M):
    n=len(M)
    c=0
    cpt=0
    for i in range (n):
        if M[i][i]==1:
            c+=1
        else :
            return False
        for j in range(n):
            if M[i][j]!=0:
                cpt+=1
    if cpt!=c+1:
        return False
    return True



##MatriceTransvectionInverse
##
##Entree :
##	M : Liste de listes : Matrice de transvection
##
##Sortie :
##	M : Liste de listes : matrice inverse de M

def MatriceTransvectionInverse (M):
    n=len( M )
    for i in range( n ) :
        for j in range( n ) :
            if i != j and M[i][j] != 0 :
                M[i][j] = - M[i][j]
    return M



## ProduitTransvectionG
##
## Entree :
##	T : Liste de listes : Matrice de transvection(n, p)
##	M : Liste de listes : Matrice(p, x)
##
## Sortie :
##	Liste de listes : matrice produit ( T * M )

def ProduitTransvectionG( T, M ) :

    P = deepcopy( M )

    i, a, j = TransvectionAssociee( T )

    for k in range( len( P[ 0 ] ) ) :

        P[ i ][ k ] += a * P[ j ][ k ]

    return P



'''
ProduitTransvectionD

	Cj <- Cj + a * Ci

Entree :
	M : Liste de listes : Matrice(n, p)
	T : Liste de listes : Matrice de transvection(p, x)

Sortie :
	Liste de listes : matrice produit ( M * T )
'''
def ProduitTransvectionD( M, T ) :
	MProduct = deepcopy( M )

	# print( "DEBUG : ", TransvectionAssociee( T ) )

	Ci, alpha, Cj = TransvectionAssociee( T )

	n = len( M )
	p = len( M[ 0 ] ) # nombre de colonnes

	if p < Ci or p < Cj :

		raise Exception("le nombre de colonnes de M est inferieur aux colonnes donnees dans la matrice de transvection")

	else :

		for i in range( n ) :
			MProduct[ i ][ Cj - 1 ] += alpha * M[ i ][ Ci - 1 ]

	return MProduct



'''
Entree :
	T : Liste de listes : matrice de transvection

Sortie :
	composants de la transvection (i, a, j) :
		i : entier : indice de la ligne/colonne à remplacer : 1 <= i
		a : reel : coefficient de multiplication de la ligne/colonne j
		j : entier : indice de la ligne/colonne de remplacement : 1 <= j ET j!=i

'''
def TransvectionAssociee( T ) :

	# AfficherMat( T )
	# print("")

	if( EstTransvection( T ) ) :

		nT = len( T )
		pT = len( T[ 0 ] )

		for i in range( nT ) :
			for j in range( pT ) :
				if i != j and T[ i ][ j ] != 0 :

					# print( "DEBUG : i+1 : ", i + 1 )
					# print( "DEBUG : j+1 : ", j + 1 )
					# print( "DEBUG : a : ", T[ i ][ j ] )

					return i+1, T[ i ][ j ], j+1

	else :
		raise Exception("ce n'est pas une matrice de transvection valide")

