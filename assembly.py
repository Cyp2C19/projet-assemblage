################# CREATION DE SAx ################
def creerSAx(X):
    tSAx = [];
    t = [];
    t_tri = [];

    for i in range(0, len(X)):
        t_tri.append(X[i:len(X)]);
        t.append(X[i:len(X)]);

    t_tri.sort();

    for i in range(0, len(t_tri)):
        for j in range(0, len(t)):
            if t[j] == t_tri[i]:
                tSAx.append(j + 1);  # +1 car X commence sa numérotation à 0

    return tSAx;


################# CREATION DE Bx ################
def creerBx(tSAx, X):
    Bx = [];

    for i in (tSAx):
        if i == 1:
            Bx.append('$');
        else:
            Bx.append(X[i - 2]);  # -2 car X commence sa numérotation à 0
    return Bx;


################ CREATION DE Cx(a) ###############
def creerCx(X):
    Cx = [];
    cmpS = 0;  # Compteur de lettre plus petite que $
    cmpA = 0;
    cmpC = 0;
    cmpG = 0;
    cmpT = 0;

    for i in X:
        if i < '$':
            cmpS = cmpS + 1;
        if i < 'A':
            cmpA = cmpA + 1;
        if i < 'C':
            cmpC = cmpC + 1;
        if i < 'G':
            cmpG = cmpG + 1;
        if i < 'T':
            cmpT = cmpT + 1;

    Cx.append(cmpS + 1);
    Cx.append(cmpA + 1);
    Cx.append(cmpC + 1);
    Cx.append(cmpG + 1);
    Cx.append(cmpT + 1);

    return Cx;


################# CREATION DE Occ ################
def creerOcc(tBx):
    tOcc = [];
    cmpS = 0;  # Compteur de lettre $ dans Bx
    cmpA = 0;
    cmpC = 0;
    cmpG = 0;
    cmpT = 0;
    ligne = [];
    for i in range(1, len(tBx) + 1):
        ligne = [];
        for j in tBx[:i]:
            if j == '$':
                cmpS = cmpS + 1;
            elif j == 'A':
                cmpA = cmpA + 1;
            elif j == 'C':
                cmpC = cmpC + 1;
            elif j == 'G':
                cmpG = cmpG + 1;
            elif j == 'T':
                cmpT = cmpT + 1;

        ligne.append(cmpS);
        ligne.append(cmpA);
        ligne.append(cmpC);
        ligne.append(cmpG);
        ligne.append(cmpT);
        cmpS = 0;
        cmpA = 0;
        cmpC = 0;
        cmpG = 0;
        cmpT = 0;
        tOcc.append(ligne);

    return tOcc;


################## Update backward ##############
def updateBackward(l, u, a, tCx, tOcc):
    if a == 'A':
        a = 1;
    elif a == 'C':
        a = 2;
    elif a == 'G':
        a = 3;
    elif a == 'T':
        a = 4;
    elif a == '$':
        a = 0;

    l = tCx[a] + tOcc[l - 2][a];
    u = tCx[a] + tOcc[u - 1][a] - 1;

    return l, u


################## backwardsSearch ##############
def backwardsSearch(motif, tCx, tOcc, tSAx):
    i = len(motif) - 1;

    if motif[i] == 'A':
        a = 1;
        b = 2;
    elif motif[i] == 'C':
        a = 2;
        b = 3;
    elif motif[i] == 'G':
        a = 3;
        b = 4;
    elif motif[i] == 'T':
        a = 4;
    elif motif[i] == '$':
        a = 0;
        b = 1;

    l = tCx[a];
    if motif[i] != 'T':
        u = tCx[b] - 1
    else:
        u = len(tSAx);

    i = i - 1;
    while l <= u and i >= 0:
        res = updateBackward(l, u, motif[i], tCx, tOcc);
        l = res[0];
        u = res[1];
        i = i - 1;

    return l, u;


###################### MAIN ######################
def main_methode2():
    X = "AGGTGGGGGG$";
    motif = "GG";
    print('Séquence : ' + str(X));
    print('Motif    : ' + str(motif));
    print();

    tSAx = creerSAx(X);
    print('SAx : ' + str(tSAx));
    print();

    tBx = creerBx(tSAx, X);
    print('Bx : ' + str(tBx));
    print();

    tCx = creerCx(X);
    print('Cx : ' + str(tCx));
    print();

    tOcc = creerOcc(tBx);
    print('Occ : ' + str(tOcc));
    print();

    res = backwardsSearch(motif, tCx, tOcc, tSAx);
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
        print("\t> " + str(tSAx[l - 1]));
    else:
        print("Le motif est présent dans la chaine caractère aux positions : ");
        for i in range(posMotif[0], posMotif[1] + 1):
            print("\t> " + str(tSAx[i - 1]));

main_methode2()