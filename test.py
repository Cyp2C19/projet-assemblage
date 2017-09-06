import random

seq = "ATCGCGACAAGCGCTGAGG"

def genererReads(seq, n, dn, k, prof):
    """Permet de générer des reads"""
    reads = []

    for j in range(0, prof):
        i = 0
        tailleReads = n
        while i <= len(seq):
            if i + tailleReads > len(seq):
                reads.append(seq[i:])
                break
            reads.append(seq[i:i+tailleReads])
            i += tailleReads - random.randint(1,k)
            tailleReads = n + random.randint(-dn, dn)
        #Tri aléatoire de la liste de reads
        random.shuffle(reads)
    return reads

print(seq)
print(genererReads(seq, 6, 2, 3, 5))