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