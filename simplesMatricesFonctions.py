##Entree :
##        m : n'importe quelle matrice representee comme une liste de listes
##Sortie :
##	pas de retour
def afficherMat( m ) :
	for i in range( len( m ) ) :
		print( m[ i ] )




##Entree :
##        m : matrice de taille n*p
##Sortie :
##        matrice transposee de m
def transpose(m):
    nb_lig=len(m)
    nb_col=len(m[0])
    aux=[]
    for i in range(nb_col):
        L=[]
        for j in range(nb_lig):
            L.append(m[j][i])
        aux.append(L)
    return aux

