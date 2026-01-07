"""
Module permettant de calculer la liste de syracuse d'un nombre n
"""
#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure
### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    Retourne un graphique de la suite
    
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    l = [ ]                 # On crée la liste vide
    val = n                 # Puis la valeur suivante
    while n > 1 :           # Et on vérifie la condition d'arret de la suite
        l.append(n)         # On ajoute l'élément courant
        if n%2 != 0 :       # Et on s'occupe des deux cas de parité
            val = n * 3 + 1
            n = val
        else :
            val = n // 2
            n = val
    l.append(1)             # Enfin on ajoute la 1 final à la liste
    return l                # Et on la renvoi

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """

    n = len(l) - 1    # On défini simplement la valeur à renvoyer comme la longueur de la suite - 1
    return n

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    origine = l[0]  # On initialise la limite de l'altitude
    n = 0
    for valeur in enumerate(l[1:]):  # Puis on parcourt toute la liste
        if valeur >= origine :          # Tant qu'on est au dessus de l'origine
            n += 1                      # Alors on ajoute 1 au tva
        else :
            break                   # Sinon on sort de la boucle

    return n


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """

    n = l[0]    # On initialise avec un valeur de la liste pour ne pas avoir de problème
                # d'appartenance
    for valeur in l:# Puis on cherche la maximum de la liste
        n = max(n, valeur)

    return n


#### Fonction principale


def main():
    """
    Fonction main du module syracuse
    """

    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
