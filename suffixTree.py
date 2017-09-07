# -*- coding: utf-8 -*-
# Titre          : Partie 2 Projet Bio-Informatique. Indexation par arbres suffixes.
# Description    : Ce programme permet de saisir une séquence d'ADN et de créer un arbre des suffixes
#                  pour cette séquence. Plusieurs opérations sont ensuite possibles : recherche de
#                  motifs et de suffixes, comptage du nombre d'occurences d'un motif, affichage des
#                  suffixes par ordre alphabétique mais aussi l'affichage du motif le plus long répété
#                  au moins deux fois.
# Auteurs        : Babujhi, Cyprien
# Date           : 07/04/2017
# Version Python : 3.6
# ──────────────────────────────────────────────────────────────────────────────────────────────────────#


###────────────────────────────────────────── CLASSE NOEUD ──────────────────────────────────────────###

class Noeud:
    """
       Classe définissant le noeud d'un arbre suffixe caractérisé par :
          - Un dictionnaire représentant ses noeuds enfants (clé = label/caractère contenu dans la
            branche qui pointe vers le noeud enfant (=valeur)
          - Un noeud connecté au noeud courant via un lien de suffixes
    """

    # ───────────────────────────────────── Méthodes classe Noeud ─────────────────────────────────────#

    def __init__(self, lienSuffixe=None):
        """
           Constructeur de la classe Noeud
        """
        self.enfants = dict()
        if lienSuffixe is not None:  # Si on a passé un objet noeud en paramètre
            self.lienSuffixe = lienSuffixe  # L'attribut de l'objet courant prend cette valeur
        else:
            self.lienSuffixe = self  # Par défaut on pointe les liens suffixes des noeuds sur eux mêmes

    def ajoutEnfant(self, car, noeud):
        """
           Méthode qui permet d'ajouter un enfant au noeud courant. Le caractère donné
           représentera le label de la branche entre le noeud courant et le noeud enfant ajouté
        """
        self.enfants[car] = noeud

    def lien(self, noeud):
        """
           Méthode qui permet de définir un lien suffixe pour le noeud courant
        """
        self.lienSuffixe = noeud


###────────────────────────────────────────── CLASSE ARBRE SUFFIXE ─────────────────────────────────────────###

class ArbreSuffixe:
    """
       Classe définissant un arbre de suffixes caractérisé par :
          - Un noeud déterminant la racine de l'arbre
          - Une séquence d'ADN à partir de laquelle l'arbre sera crée
            Le caractère '$' sera ajouté à la fin de cette séquence
    """

    def __init__(self, seq):
        """
           Constructeur de la classe ArbreSuffixe
        """
        self.racine = Noeud()
        self.sequence = seq + "$"

    # ───────────────────────────────────── Méthodes classe ArbreSuffixe ─────────────────────────────────────#

    def construction(self):
        """
           Méthode de construction d'un arbre des suffixes. Algorithme on-line qui se fait un caractère à la
           fois. Les liens suffixes permettent d'accélérer la création de l'arbre avec une compléxité linéaire
           en temps
        """
        seq = self.sequence

        # Création des deux premiers noeuds de l'arbre
        racine = self.racine
        noeudPlusProfond = Noeud(racine)  # Noeud le plus profond dans l'arbre = plus long chemin de l'arbre
        racine.ajoutEnfant(seq[0],
                           noeudPlusProfond)  # Ajout de ce noeud avec le premier caractère de la séquence dans les enfants de la racine

        # Pour chaque caractère de la séquence (premier caractère déjà traité)
        for car in seq[1:]:
            noeudCourant = noeudPlusProfond  # On définit le noeud courant comme étant le plus profond dans l'arbre
            noeudPrecedent = None  # On définit le noeud précédemment inséré. Pas de noeud précédent par défaut

            # Tant qu'il n'y a pas de branche sortante à partir du noeud courant qui contient le caractère traité
            while car not in noeudCourant.enfants:
                # Ajout d'un nouveau noeud dans les enfants du noeud courant. La branche aura comme label le caractère traité
                nouveauNoeud = Noeud()
                noeudCourant.ajoutEnfant(car, nouveauNoeud)

                # Si un noeud a été précédemment inséré, on pointe un lien suffixe du précédent vers le nouveau noeud
                if noeudPrecedent is not None:
                    noeudPrecedent.lien(nouveauNoeud)

                noeudPrecedent = nouveauNoeud  # Le noeud précédent prend la valeur du nouveau noeud inséré
                noeudCourant = noeudCourant.lienSuffixe  # Le noeud courant se déplace vers le noeud pointé via son lien suffixe

            # Mise en place du dernier lien suffixe
            if noeudCourant is racine and noeudPrecedent is racine.enfants[car]:
                noeudPrecedent.lien(racine)
            else:
                noeudPrecedent.lien(noeudCourant.enfants[car])

            # On avance le noeud le plus profond vers le nouveau noeud crée
            noeudPlusProfond = noeudPlusProfond.enfants[car]

    def afficher(self, racine, n=0):
        """
           Méthode qui permet d'afficher l'arbre des suffixes
        """
        for i in racine.enfants.keys():
            print(n * "  │" + "──" + i)
            self.afficher(racine.enfants[i], n + 1)

    def traverser(self, seq):
        """
           Méthode qui permet de traverser l'arbre en suivant les caractères d'une séquence donnée.
           Retourne le noeud qui a une branche liant son noeud parent avec le dernier caractère
           de la séquence donnée. Retourne None si la séquence n'est pas trouvée
        """
        noeudCourant = self.racine
        for car in seq:
            if car not in noeudCourant.enfants:
                return None
            noeudCourant = noeudCourant.enfants[car]
        return noeudCourant

    def chercheMotif(self):
        """
           Méthode qui permet de traverser l'arbre avec la méthode traverser et qui permet
           d'afficher si la séquence donnée est un motif de la séquence cible ou non
        """
        print("\nRecherche de motif dans la séquence :", self.sequenceBrute())
        seq = saisieSequence()
        noeud = self.traverser(seq)
        if noeud is not None:
            print("\n", seq, "est un motif de la séquence cible")
        else:
            print("\n", seq, "n'est pas un motif de la séquence cible")

    def chercheSuffixe(self):
        """
           Méthode qui permet de traverser l'arbre avec la méthode traverser et qui permet
           d'afficher si la séquence donnée est un suffixe de la séquence cible ou non.
           Un suffixe de l'arbre aura une branche étiquettée avec un '$' parmis ses enfants
        """
        print("\nRecherche de suffixe dans la séquence :", self.sequenceBrute())
        seq = saisieSequence()
        noeud = self.traverser(seq)
        if noeud is not None and '$' in noeud.enfants:
            print("\n", seq, "est un suffixe de la séquence cible")
        else:
            print("\n", seq, "n'est pas un suffixe de la séquence cible")

    def nombreFeuilles(self, noeud):
        """
           Méthode qui permet de calculer le nombre de feuilles dans le sous arbre d'un
           noeud
        """
        nbFeuilles = 0
        for i in noeud.enfants.keys():
            if i == '$':
                nbFeuilles += 1
            else:
                nbFeuilles += self.nombreFeuilles(noeud.enfants[i])
        return nbFeuilles

    def nombreOccurences(self):
        """
           Méthode qui permet de traverser l'arbre et fficher le nombre d'occurences d'un motif donné
           dans la chaine cible. Le nombre d'occurences correspondra au nombre de feuilles dans le sous
           arbre du noeud trouvé si le motif est présent dans la séquence
        """
        print("\nRecherche du nombre d'occurences d'un motif dans la séquence :", self.sequenceBrute())
        seq = saisieSequence()
        noeud = self.traverser(seq)
        if noeud != None:
            print("\nNombre d'occurences du motif", seq, "=>", self.nombreFeuilles(noeud))
        else:
            print("\nLe motif n'est pas présent dans la séquence cible")

    def listeSuffixes(self, racine, liste, str):
        """
           Méthode qui permet de parcourir tous les noeuds de l'arbre et de stocker dans
           une liste tous les suffixes de cet arbre
        """
        if '$' in racine.enfants:  # Si on arrive en fin de suffixe
            liste.append(str)
        for i in racine.enfants.keys():
            self.listeSuffixes(racine.enfants[i], liste, str=str + i)
        return liste

    def affichageSuffixesOrdre(self):
        """
           Méthode qui permet, à partir de la liste des suffixes de l'arbre, d'afficher
           ces suffixes par ordre alphabétique
        """
        liste = self.listeSuffixes(self.racine, [], "")  # Liste des suffixes de l'arbre
        liste.remove("")  # On supprime la chaine vide pour la racine
        liste.sort()  # Tri de la liste

        print("\nAffichage des suffixes de l'arbre par ordre alphabétique pour la séquence :",
              self.sequenceBrute(), "\n")
        for i in liste:
            print("-", i)

    def listeMotifsRepetes(self, racine, liste, str):
        """
           Méthode qui permet de parcourir tous les noeuds de l'arbre et de stocker dans
           une liste tous les motifs qui sont répétés au moins deux fois dans la séquence
           cible
        """
        if self.nombreFeuilles(racine) >= 2:  # Suffixe répété au moins 2 fois
            liste.append(str)
        for i in racine.enfants.keys():
            self.listeMotifsRepetes(racine.enfants[i], liste, str=str + i)
        return liste

    def affichageMotifsRepetes(self):
        """
           Méthode qui permet, à partir de la liste des motifs répétés au moins deux fois,
           d'afficher le/les plus long motif(s) pour cette liste
        """
        liste = self.listeMotifsRepetes(self.racine, [], "")  # Liste des suffixes de l'arbre
        liste.sort(key=lambda item: len(item), reverse=True)  # Tri de la liste par tailles motifs décroissants
        if "" in liste:
            liste.remove("")  # Si deux feuilles à la racine on supprime le mot vide
        if len(liste) == 0:
            print("\nAucun motif n'est répété au moins deux fois dans la séquence : ", self.sequenceBrute())
        else:
            tailleMax = len(liste[0])  # Taille max du plus long motif répété deux fois
            print("\nAffichage du/des motif(s) le(s) plus long répété(s) au moins 2 fois dans la séquence",
                  self.sequenceBrute(), ":")
            for i in liste:
                if len(i) == tailleMax:  # On affiche tous les motifs de taille max
                    print("-", i)

    def sequenceBrute(self):
        """
           Méthode qui permet d'afficher la séquence contenue dans l'arbre sans le caractère '$'
        """
        seq = self.sequence
        seq = seq.replace("$", "")
        return seq


###────────────────────────────────────────── SAISIES ─────────────────────────────────────────###

def saisieSequence():
    """
        Fonction de saisie contrôlée d'une chaîne d'ADN
        Retourne une chaine de caractères composée de A|C|T|G
    """
    encore = True
    seq = ""
    print("\nVeuillez entrer une séquence d'ADN (non sensible à la casse) => ")
    while (encore):
        seq = input().upper()
        for i in seq:
            if (i != 'A' and i != 'T' and i != 'C' and i != 'G'):
                encore = True
                print("Un caractère différent de A,T,C,G a été saisi, veuillez réessayer")
                break
            else:
                encore = False
    return (seq)


###────────────────────────────────────────── MENU ─────────────────────────────────────────###

def affichageMenu():
    """
        Fonction qui permet d'afficher le menu du programme
    """
    print("\n", 31 * "─", "MENU", 31 * "─")
    print("1. Construction de l'arbre des suffixes pour une séquence d'ADN")
    print("2. Recherche de motif")
    print("3. Recherche de suffixe")
    print("4. Comptage du nombre d'occurences d'un motif")
    print("5. Motif(s) le(s) plus long répété(s) au moins deux fois")
    print("6. Liste des suffixes triés par ordre alphabétique")
    print("7. Quitter")
    print(69 * "─")


def erreurArbre():
    """
       Fonction qui permet d'afficher un message d'erreur dans le menu si l'arbre
       n'a pas été crée avant d'effectuer une opération
    """
    print("\nVeuillez créer un arbre avant d'éffectuer cette opération\n")


###────────────────────────────────────────── MAIN ─────────────────────────────────────────###

run = True
arbre = ArbreSuffixe("")

while (run):
    affichageMenu()
    choix = input("Entrez votre choix [1-7] => ")

    if choix == '1':
        seq = saisieSequence()
        arbre = ArbreSuffixe(seq)
        arbre.construction()
        print("\nVisualisation de l'arbre des suffixes : \n")
        arbre.afficher(arbre.racine)

    elif choix == '2':
        arbre.chercheMotif() if arbre.sequence != "$" else erreurArbre()

    elif choix == '3':
        arbre.chercheSuffixe() if arbre.sequence != "$" else erreurArbre()

    elif choix == '4':
        arbre.nombreOccurences() if arbre.sequence != "$" else erreurArbre()

    elif choix == '5':
        arbre.affichageMotifsRepetes() if arbre.sequence != "$" else erreurArbre()

    elif choix == '6':
        arbre.affichageSuffixesOrdre() if arbre.sequence != "$" else erreurArbre()

    elif choix == '7':
        run = False
    else:
        print("\nLa saisie ne correspond à aucun menu, réessayez")
