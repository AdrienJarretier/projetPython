
'''
MatNulle

Entree :
	n : un entier
	p : un entier

Sortie :
	Matrice nulle de taille (n, p) représentée par une liste de listes
'''
def MatNulle(n, p) :
	m = []
	for i in range(n) :
		L = []
		for j in range(p):
			L.append(0)

		m.append(L)

	return m

def AfficherMat( m ) :
	# m : n'importe quelle matrice representee comme une liste de listes

	# pas de retour
	for i in range( len( m ) ) :
		print( m[ i ] )

