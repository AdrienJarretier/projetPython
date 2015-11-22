from random import shuffle
from simplesMatricesFonctions import *


'''
PermutationAleatoire

Entree :
	n : un entier

Sortie :
	Une liste qui represente une matrice de permutation aleatoire de taille n*n (n-uplet)
'''
def PermutationAleatoire( n ) :

	nUpletPermut = []

	for i in range( n ):
		nUpletPermut.append( i + 1 )

	shuffle( nUpletPermut )

	return nUpletPermut



'''
MatricePermutation

Entree :
	nUpletPermutation : liste representant une matrice de permutation

Sortie :
	Liste de listes correspondant à la Matrice de permutation associee a nUpletPermutation
'''
def MatricePermutation( nUpletPermutation ) :

	n = len( nUpletPermutation )
	matricePerm = MatNulle( n, n )

	# start DEBUG
	# afficherMat( matricePerm )
	# print( "" )
	# end DEBUG

	for col in range( n ) :
		lig = nUpletPermutation[ col ] - 1
		# on ajoute un " 1 " a la ligne specifiee par nUpletPermutation, sinon un " 0 "
		matricePerm[ lig ][ col ] = 1

	return matricePerm



'''
PermutationAssociee

Entree :
	mPerm : matrice de permutation

Sortie :
	liste representant mPerm (n-uplet associe)
'''
def PermutationAssociee( mPerm ) :
	nUpletPermutation = []

	for j in range( len( mPerm[ 0 ] ) ) :
		for i in range( len( mPerm ) ) :
			if mPerm[ i ][ j ] == 1 :
				nUpletPermutation.append( i + 1 )

	return nUpletPermutation



## EstPermutation
##
## Enree :
##		M : matrice à tester de taille n*p
##
## Sortie :
##		Vrai si la matrice M est une matrice de permutation valide
##
def EstPermutation( M ) :
    n = len( M )
    p = len( M[0] )
    L = []
    if n != p :
        return False
    for i in range( n ) :
        cptLigne = 0
        for j in range( n ) :
            if M[i][j] != 0 and M[i][j] != 1 :
                return False
            if M[i][j] == 1 :
                cptLigne += 1
                L.append(i)
                if i in L :
                    return False
        if cptLigne != 1 :
            return False

    return True



## MatricePermutationInverse
##
## L'inverse d'une matrice de permutation est egale a la transposee de la dite matrice
##
## Utilisation d'une fonction Transposee()
##
## Entree :
##		mPerm : matrice de permutation
##
## Sortie :
##		matrice inverse de mPerm
##
def MatricePermutationInverse( mPerm ):
    return Transposee( mPerm)



'''
ProduitPermutG

nUplet : n-uplet associe a P

l'ordre des Lignes change,
dans chaque ligne i de ( P * M ) on a la ligne de M de la position de i dans nUplet

Entree :
	P : matrice de permutation
	M : matrice quelconque de du meme nombre de lignes que P

Sortie :
	matrice produit de P et M ( P * M )
'''
def ProduitPermutG( P, M ) :
	MProduct = []

	nUplet = PermutationAssociee( P )

	for i in range( len( M ) ) :
		MProduct.append( M[ nUplet.index( i+1 ) ] )

	return MProduct



## ProduitPermutD
##
## n-uplet : n-uplet associe a P
##
## l'ordre des Colonnes change,
## dans chaque colonne j de ( M * P ) on a la colonne n-uplet[j] de M
##
## Entree :
##		P : matrice de permutation
##		M : matrice quelconque
##
## Sortie :
##		matrice produit de M et P ( M * P )
##
def ProduitPermutD( M, P ) :

    L = PermutationAssociee( P )
    n = len ( M )
    p = len ( M[ 0 ] )
    A = MatNulle( n, p )

    for j in range( p ) :

        for i in range( n ) :

            A[ i ][ j ] = M[ i ][ L[ j ] - 1 ]

    return A

