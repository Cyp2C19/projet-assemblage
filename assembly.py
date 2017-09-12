################# CREATION DE SAx ################
def creerSAx(X):
    tSAx = [];
    t = [];
    t_tri = [];

    for i in range(0, len(X)):
        t_tri.append(X[i:len(X)]);
        t.append(X[i:len(X)]);

    t_tri.sort();
    print(t_tri)
    print(t)
    for i in range(0, len(t_tri)):
        for j in range(0, len(t)):
            if t[j] == t_tri[i]:
                tSAx.append(j + 1);  # +1 car X commence sa numérotation à 0
                break
    print(tSAx)
    return tSAx;


################# CREATION DE Bx ################
def creerBx(tSAx, X):
    Bx = [];

    for i in (tSAx):
        if i == 1:
            Bx.append('$');
        else:
            Bx.append(X[i - 2]);  # -2 car X commence sa numérotation à 0
    print(Bx)
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

def generalSAx(reads):      # Reads = list of reads
    if reads[0][-1] != '$':
        for i in range(0,len(reads)):
            reads[i]+='$'

    GSAx = []
    for i in range (0,len(reads)):
        for j in range(0,len(reads[i])):
            if GSAx == []:
                GSAx.append((i,j))
            else:
                find=False
                for k in range(0,len(GSAx)):
                    if reads[GSAx[k][0]][GSAx[k][1]:] > reads[i][j:]:
                        GSAx.insert(k,(i,j))
                        find=True
                        break
                    elif reads[GSAx[k][0]][GSAx[k][1]:] == reads[i][j:]:
                        if GSAx[k][0] > i:
                            GSAx.insert(k, (i, j))
                            find=True
                            break
                if not(find):
                    GSAx.append((i, j))
    print(GSAx)
    return(GSAx)


def generalBx(gSAx, reads):
    Bx = [];
    for i in (gSAx):
        if i[1] == 0:
            Bx.append('$');
        else:
            Bx.append(reads[i[0]][i[1]-1]);
    print(Bx)
    return Bx;

def generalCx(Bx):
    Cx={"$":1}
    Cx["A"] = len([i for i in Bx if i == '$'])+1
    Cx["C"] = len([i for i in Bx if i == 'A'])+Cx["A"]
    Cx["G"] = len([i for i in Bx if i == 'C'])+Cx["C"]
    Cx["T"] = len([i for i in Bx if i == 'G']) + Cx["G"]
    print(Cx)
    return(Cx)


def generalOccx(Bx):
    lettre = ["$","A","C","G","T"]
    Occx = {"$":[],"A":[],"C":[],"G":[],"T":[]}
    for i in Bx:
        Occx[i].append(1) if Occx[i]==[] else Occx[i].append((Occx[i][-1])+1)
        for l in [k for k in lettre if k != i]:
            Occx[l].append(0) if Occx[l]==[] else Occx[l].append((Occx[l][-1]))
    print(Occx)
    return(Occx)

def updateBackward2(l, u, cx, occx, lettre):
    newL = cx[lettre] + occx[lettre][l-2]
    newU = cx[lettre] + occx[lettre][u-1]-1
    return(newL,newU)

def findOverlap(read,cx,occx,sax):
    lettre = ["$", "A", "C", "G", "T"]
    i = len(read)
    l = cx[read[i-1]]
    lettreSuiv = read[i-1]
    if lettreSuiv != "T":
        lettreSuiv = lettre.index(lettreSuiv)+1
        u = cx[lettre[lettreSuiv]] - 1
    else:
        u = len(sax)
    i -= 1
    while l <= u and i >= 1 :
        if ((len(read) - i-1 + 1) >= 0):
            l2,u2 = updateBackward2(l,u,cx,occx,"$")
            if l2 <= u2:
                print("X=",read,", l2=",l2,", u2=",u2)
        l,u = updateBackward2(l,u,cx,occx, read[i-1])
        i -= 1
    if l <= u:
        print("X=",read,", l=",l,", u=",u)
        return(l,u)
    return(-1,-1)


def genOverlap(l, u, sax, suff, read):
    if l != u:
        print("if 0 ok")
        ssl = []
        for k in range(l, u + 1):
            ssl.append(sax[k-1])
        print("ssl:")
        print(ssl)
        for m in ssl:
            if m[0] == 0:
                print("if 1 ok")
                if m[1] + len(suff) == len(read) :
                    print("if 2 ok")
                    if (1,0) in ssl:
                        print("if 3 ok")
                        return True
        return False
    else:
        return False

def parcoursReads(listeReads,overlapSize):
    seq = ""
    for i in range(0,len(listeReads)-1):
        print("Reads:",listeReads[i],", ",listeReads[i+1])
        ssListe=[listeReads[i],listeReads[i+1]]
        sax = generalSAx(ssListe)
        bx = generalBx(sax, ssListe)
        cx = generalCx(bx)
        occx = generalOccx(bx)

        for j in reversed(range(1, overlapSize + 1)):
            suff=ssListe[0][:-1][-j:]
            l, u = findOverlap(suff, cx, occx, sax)
            print("Sax = ")
            print(sax)
            print("l=",l,", u=",u)
            res = genOverlap(l,u,sax,suff,listeReads[i])
            print(res)
            if res:
                seq += listeReads[i][:-len(suff)]
                break
            print("****************************")
        print("----------------------------------")
    seq += listeReads[-1]
    print(seq)
    return(seq)


#main_methode2()
# seq = TCTGAGAACAACGTACGGACCGGTATGTACACAGGAGATATTCATTGATAGCACGCTTAGCCCCCCCAAAAACTTTAAGCTCAACCATTAACTGTGTACGAGACGTCTGAATAAGGGTGATCCTGCGCACTTGGCTCAACAGTTCCTGATCGTTTTGCACAGCCTAGAGACCTTACCGCATAGGGATGGACTTTCCGCTG
#listeReads=["ATGCT","CTTGATG","GATCCAT","ATC","TCTATATA"]
listeReads=["TCTGAGA","GAACAACGT","GTACGGA","ACCGGTAT","TATGTACAC","CAGGAGA","AGATATTCA","ATTGATA","TAGCACGCT","TTAGCCC","CCCCCCCA","CAAAAACT","CTTTAAG","AAGCTCA","CAACCAT","CATTAAC","CTGTGTAC","ACGAGAC","GACGTCT","CTGAATAA","AAGGGTG","GATCCTGCG","CGCACTTG","TTGGCTC","CAACAGTT","TTCCTGAT","TCGTTTT","TTGCACAG","CAGCCTAG","TAGAGACC","CCTTACCGC","CGCATAGGG","GGATGGACT","CTTTCCG","GCTG"]

parcoursReads(listeReads,3)



# #l1 = ["ATGCT","CTTGAT"]
# sax=generalSAx(l1)
# bx=generalBx(sax,l1)
# cx=generalCx(bx)
# occx=generalOccx(bx)
# l,u=findOverlap("GCT",cx,occx,sax)
# checkOverlap(l,u,sax)
