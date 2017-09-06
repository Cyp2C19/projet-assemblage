import random

seq = "ATCGCGACAAGCGCTGAGGCCTGCGATGC"

def genererReads(seq, n, k):
    """Permet de générer des reads de taille n en fonction d'une
       séquence ADN entrée en paramètre """
    reads = []
    i = 0

    while i <= len(seq):
        if i + n > len(seq):
            break
        else:
            reads.append(seq[i:i+n])
            i += n - random.randint(1,k)
    #Tri aléatoire de la liste de reads
    random.shuffle(reads)
    n += random.randint(-2, 2)
    return reads

print(seq)
print(genererReads(seq, 4, 3))