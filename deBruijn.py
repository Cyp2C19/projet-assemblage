class GrapheDeBruijn:
    """ De Bruijn multigraph built from a collection of strings.
        User supplies strings and k-mer length k.  Nodes of the de
        Bruijn graph are k-1-mers and edges correspond to the k-mer
        that joins a left k-1-mer to a right k-1-mer. """

    @staticmethod
    def chop(st, k):
        """ Chop a string up into k mers of given length """
        for i in range(0, len(st) - (k - 1)):
            yield (st[i:i + k], st[i:i + k - 1], st[i + 1:i + k])

    class Node:
        """ Node in a de Bruijn graph, representing a k-1 mer.  We keep
            track of # of incoming/outgoing edges so it's easy to check
            for balanced, semi-balanced. """

        def __init__(self, km1mer):
            self.km1mer = km1mer

        def __hash__(self):
            return hash(self.km1mer)

    def __init__(self, strIter, k):
        self.G = {}
        self.nodes = {}
        self.k = k

        for st in strIter:
            for kmer in self.chop(strIter, k):
                print(kmer)
                km1L, km1R = kmer[:-1], kmer[1:]
                nodeL, nodeR = None, None
                if (km1L in self.nodes):
                    nodeL = self.nodes[km1L]
                else:
                    nodeL = self.nodes[km1L] = self.Node(km1L)
                if (km1R in self.nodes):
                    nodeR = self.nodes[km1R]
                else:
                    nodeR = self.nodes[km1R] = self.Node(km1R)

                self.G.setdefault(nodeL, []).append(nodeR)


graphe = GrapheDeBruijn("actg", 3)
x = 0
for key, value in graphe.G.items():
    print("Noeud", x, " ", key.km1mer)
    x += 1
    for i in value:
        print(i.km1mer)
