import random

seq = "ATCGCGACAAGCGCTGAGG"

def genererReads(seq, n, dn, k):
    """Permet de générer des reads de taille n en fonction d'une
       séquence ADN entrée en paramètre """
    reads = []
    i = 0
    tailleReads = n

    while i <= len(seq):
        if i + tailleReads > len(seq):
            reads.append(seq[i:])
            break
        else:
            reads.append(seq[i:i+tailleReads])
            i += tailleReads - random.randint(1,k)
    #Tri aléatoire de la liste de reads
    random.shuffle(reads)
    tailleReads = n + random.randint(-dn, dn)
    return reads

print(seq)
print(genererReads(seq, 6, 2, 3))