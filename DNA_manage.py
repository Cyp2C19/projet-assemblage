from random import randint

def createReads(seq,readSize,delta,overlap,repeat):
    print("Parameters")
    print(seq)
    print(readSize)
    print(delta)
    print(overlap)
    print(repeat)

    reads = []
    i = 0
    while i < 10:


        lenR=randint(readSize-delta,readSize+delta)
        print(lenR)