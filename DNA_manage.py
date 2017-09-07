import random

def createRandomDNASeq(n):
    seq = ''
    for i in range(0, n):
        seq += random.choice(['A','C','G','T'])
    return seq

def createReads(seq,readSize,delta,overlap,repeat):
    print("Parameters")
    print(seq)
    print(readSize)
    print(delta)
    print(overlap)
    print(repeat)

    reads = []
    for j in range(0,repeat):
        i = 0
        while i < len(seq):
            if i != 0:
                i -= random.randint(1,overlap)
            lenR=random.randint(readSize-delta,readSize+delta)
            reads.append(seq[i:i+lenR])
            i += lenR
    random.shuffle(reads)
    return(reads)
