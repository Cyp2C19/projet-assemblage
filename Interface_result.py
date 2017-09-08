from tkinter.filedialog import *
from assembly import *


def displayResults(reads):
    fenetre = Tk()
    seq=""
    for i in reads:
        seq+=str(i)
    seq+="$"
    tSx= creerSAx(seq)
    bx=creerBx(tSx,seq)
    cx=creerCx(seq)
    tOcc = creerOcc(bx);
    res = backwardsSearch("ACA", cx, tOcc, tSx);
    """---------------------------------------------"""
    l = res[0];
    u = res[1];
    print('l : ' + str(l));
    print("u : " + str(u));
    print();
    posMotif = [l, u];
    if (l > u):
        print("Le motif n'est pas présent dans la séquence !");
    elif (l == u):
        print("Le motif est présent dans la chaine caractère à la position : ");
        print("\t> " + str(tSx[l - 1]));
    else:
        lVide = []
        print("Le motif est présent dans la chaine caractère aux positions : ");
        for i in range(posMotif[0], posMotif[1] + 1):
            lVide.append(tSx[i - 1])
        print(lVide)
        lVide.sort()
        print(lVide)
    """---------------------------------------------"""
    fenetre.mainloop()