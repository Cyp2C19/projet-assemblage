import random

seq = "AGCTCGAGTCAGCGCTCTAGATCG"

def genererReads(seq, n):
    """Permet de générer des reads en fonction d'une séquence
       entrée en paramètre et de la taille des reads"""
    reads = []
    i = 0
    while i <= len(seq):
        if i + n > len(seq):
            break
        else:
            reads.append(seq[i:i+n])
            i += 1
    #Tri aléatoire de la liste de reads
    random.shuffle(reads)
    return reads

print(seq)
print(genererReads(seq, 6))