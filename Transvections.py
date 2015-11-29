from simplesMatricesFonctions import *
from copy import deepcopy


##MatriceTransvection
##
##On notera une transvection : t(i,a,j)
##
##Matrice identite + a * Matrice Eij
##
##Entree :
##    i : entier : indice de la ligne a remplacer si utilisee dans un produit a gauche: 1 <= i
##                              colonne de remplacement si utilisee dans un produit a droite
##
##    a : reel : coefficient de multiplication de la ligne/colonne de remplacement 
##
##    j : entier : indice de la ligne de remplacement si utilisee dans un produit a gauche: 1 <= j ET j != i
##                              colonne a remplacer si utilisee dans un produit a droite
##
##    n : entier : dimensions de la matrice (n,n) : Optionnel,
##              si non fourni n prendra max( i, j )
##Sortie :
##    Liste de listes : Matrice de transvection
##
##Fonctionnement :
##        On verifie que i et j soient differents et superieurs a 0 car si ce n'est pas le cas
##        on ne peut pas cree la matrice transvection.
##
##        Comme par la suite on n'effectue pas de vrais produits de matrices on a decide de ne pas
##        rendre le parametre n obligatoire car il n'est pas necessaire d'avoir deux matrices de taille
##        n*p pour l'une et p*r pour l'autre.
##
##        Donc on regarde si le parametre n a ete specifie, si non on prend le maximum entre i et j comme
##        taille de matrice.
##        Puis on ajoute a a la ligne i-1 et a la colonne j-1. 
        
def MatriceTransvection( i, a, j, n=0 ) :

        # print("DEBUG : n :", n)

        if i == j or i < 1 or j < 1 :
                raise Exception( "'i' et 'j' doivent etre differents et superieurs a 0" )
        else :
                if n == 0 :
                        Id = MatId( max( i, j ) )
                elif n > max( i, j ) :
                        Id = MatId( n )
                else :
                        raise Exception( "n est inferieur a i et a j ! " )

                Id[ i - 1 ][ j - 1 ] = a
                return Id



##EstTransvection
##
##Une matrice de transvection a :
##      - uniquement des 1 dans la diagnonale
##      - des 0 partout sauf un et un seul element
##
##Entree :
##      M : Liste de listes : Matrice
##
##Sortie :
##      Booleen : vrai si M est une matrice de transvection
##
##Fonctionnement :
##        On regarde si les coefficients diagonaux sont tous egaux a 1 et on increment un compteur c lorsque c'est le cas.
##        Puis on regarde dans la matrice tous les coefficients differents de 0 et on incremente un
##        compteur cpt lorsque c'est le cas.
##        A la fin si cpt est strictement plus grand que c+1 c'est alors qu'il y a plus d'un coefficient en dehors de la
##        diagonale qui est different de 0. 
        

def EstTransvection(M):
        n = len( M )
        c = 0
        cpt = 0

        for i in range ( n ) :

                if M[ i ][ i ] == 1 :
                        c += 1
                else :
                        return False

                for j in range( n ) :

                        if M[ i ][ j ] != 0 :
                                cpt += 1

        if cpt > c + 1 :
                return False

        return True



##MatriceTransvectionInverse
##
##Entree :
##      M : Liste de listes : Matrice de transvection
##
##Sortie :
##      M : Liste de listes : matrice inverse de M
##
##Fonctionnement :
##        On regarde que i et j soient different (pour pas etre sur la diagonale contenant des 1)
##        puis on regarde aussi que le coefficient a soit different de 0.
##        Si ces deux conditions sont remplies alors on multiplie le coefficient a par -1. 

def MatriceTransvectionInverse (M):

        inverse = deepcopy( M )

        n=len( inverse )
        for i in range( n ) :
                for j in range( n ) :
                        if i != j and inverse[i][j] != 0 :
                                inverse[i][j] = - inverse[i][j]
        return inverse



## ProduitTransvectionG
##
## Li <- Li + a * Lj
##
## Entree :
##      T : Liste de listes : Matrice de transvection(n, p)
##      M : Liste de listes : Matrice(p, x)
##
## Sortie :
##      Liste de listes : matrice produit ( T * M )
##
##Fonctionnement :
##        On recupere les coefficients i, j et a de la matrice de transvection T
##        avec la fonction TransvectionAssociee.
##        Puis on remplace la ligne i par la ligne i + la ligne j multipliee par a. 

        
def ProduitTransvectionG( T, M ) :

        P = deepcopy( M )

        i, a, j = TransvectionAssociee( T )

        # print("DEBUG : i, a, j : ", i, a, j)
        n = len( M ) # Nombre de ligne
        p = len( M[ 0 ] ) 

        for k in range( len( P[ 0 ] ) ) :

                # print("DEBUG : ", P)
                # print("DEBUG : i : ", i)
                # print("DEBUG : j : ", j)
                # print("DEBUG : k : ", k)

                P[ i - 1 ][ k ] += a * P[ j - 1 ][ k ]

        return P



'''
ProduitTransvectionD

        Cj <- Cj + a * Ci

Entree :
        M : Liste de listes : Matrice(n, p)
        T : Liste de listes : Matrice de transvection(p, x)

Sortie :
        Liste de listes : matrice produit ( M * T )

Fonctionnement :
        On recupere les coefficients Ci, Cj et alpha de la matrice de transvection T
        avec la fonction TransvectionAssociee.
        On verifie que Ci et Cj sont des indices de colonnes valides, c'est a dire qu'ils sont
        inferieurs aux nombres de colonnes de la matrice M. 
        Puis on remplace la colonne j par la colonne j + la colonne i multipliee par alpha. 

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
                        MProduct[ i ][ Cj - 1 ] += alpha * MProduct[ i ][ Ci - 1 ]

        return MProduct



'''
Entree :
        T : Liste de listes : matrice de transvection

Sortie :
        composants de la transvection (i, a, j) :
                i : entier : indice de la ligne a remplacer si utilisee dans un produit a gauche: 1 <= i
                                          colonne de remplacement si utilisee dans un produit a droite

                a : reel : coefficient de multiplication de la ligne/colonne de remplacement : si T = Id alors (i,a,j)=(1,0,1) 

                j : entier : indice de la ligne de remplacement si utilisee dans un produit a gauche: 1 <= j ET j != i
                                          colonne a remplacer si utilisee dans un produit a droite

Fonctionnement :
        On teste si la matrice T est bien une matrice de transvection avec la fonction EstTransvection si c'est le cas ;
        on cherche le coefficient pour lequel i et j sont different (c'est a dire pas sur la diagonale) et qui est different de 0.
        Lorsqu'on l'a trouve on retourne son indice de ligne (ici i+1), le coefficient et son indice de colonne (ici j+1).
        Si aucun coefficient en dehors de la diagonale est different de 0 alors on retourne (1, 0, 1) car aucunes transvections
        n'est effectuee.
        Si la matrice T n'est pas une matrice de transvection on leve une exception.
        
'''
def TransvectionAssociee( T ) :

        # AfficherMat( T )
        # print("")

        # print( "DEBUG TransvectionAssociee T : " )
        # AfficherMat( T )

        if( EstTransvection( T ) ) :

                nT = len( T )
                pT = len( T[ 0 ] )

                for i in range( nT ) :
                        for j in range( pT ) :
                                if i != j and T[ i ][ j ] != 0 :

                                        # print( "DEBUG : i+1 : ", i + 1 )
                                        # print( "DEBUG : j+1 : ", j + 1 )
                                        # print( "DEBUG TransvectionAssociee : a : ", T[ i ][ j ] )

                                        return i+1, T[ i ][ j ], j+1

                return 1, 0, 1

        else :
                raise Exception("ce n'est pas une matrice de transvection valide")

