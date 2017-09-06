s = "AGCTCGAGTCAGCGCTCTAGATCG"

def genererReads(seq, n, k):
    reads = []
    i = 0
    while i <= len(seq):
        if i + n > len(seq):
            reads.append(seq[i:] + seq[:k])
            break
        else:
            reads.append(seq[i:i+n])
            i += n-k
    return reads

print(s)
print(genererReads(s, 4, 3))