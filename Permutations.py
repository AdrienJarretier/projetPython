from random import shuffle
from simplesMatricesFonctions import *


'''
PermutationAleatoire

Entree :
	n : un entier ; n > 0

Sortie :
	Une liste qui represente une matrice de permutation aleatoire de taille n*n (n-uplet)

Fonctionnement :
	genere une liste d'entiers de 1 a n
	puis melange la liste
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
	Liste de listes correspondant a la Matrice de permutation associee a nUpletPermutation
'''
def MatricePermutation( nUpletPermutation ) :

	n = len( nUpletPermutation )
	matricePerm = MatNulle( n, n )

	for col in range( n ) :
		lig = nUpletPermutation[ col ] - 1

		# on ajoute un " 1 " a la ligne specifiee par nUpletPermutation
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
##	M : matrice a tester de taille n*p (ici il faut que la matrice soit de taille n*n)
##
## Sortie :
##	Vrai si la matrice M est une matrice de permutation valide
##
## Fonctionnement :
##        On cherche :
##            - Si la matrice est carree
##            - S'il n'y a pas de valeurs differente de 0 et de 1
##            - Si dans chaque ligne on a qu'un seul 1
##            - Si dans chaque colonne on a qu'un seul 1
##        Si toutes ces conditions sont respectees alors on a une matrice de permutation

def EstPermutation( M ) :
    n = len( M )
    p = len( M[ 0 ] )
    if n != p :
        return False
    for i in range( n ) :
        cptLigne = 0
        cptColonne = 0
        for j in range( n ) :
            if M[i][j] != 0 and M[i][j] != 1 :
                return False
            if M[i][j] == 1 :
                cptLigne += 1
            if M[j][i] == 1 :
                cptColonne +=1
        if cptLigne != 1 or cptColonne != 1 :
            return False

    return True



## MatricePermutationInverse
##
## L'inverse d'une matrice de permutation est egale a la transposee de la dite matrice
##
## Utilisation d'une fonction Transposee()
##
## Entree :
##	mPerm : matrice de permutation
##
## Sortie :
##	matrice inverse de mPerm
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
	# print( " **DEBUG** nUplet : ", nUplet, " **DEBUG** " )

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
##	P : matrice de permutation
##	M : matrice quelconque
##
## Sortie :
##	matrice produit de M et P ( M * P )
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

