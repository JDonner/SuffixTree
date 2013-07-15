import SuffixTree, sys
STDERR = sys.stderr

def depth(n, d=0):
    while n:
        print >>STDERR, '\t' * d,
        print >>STDERR, "edge string: %r" % n.edgestr(),
        print >>STDERR, "label str: %r " % n.labelstr(),
        print >>STDERR, "getch: %s" % n.getch(),
        print
        depth(n.children(), d+1)
        n = n.next()


if __name__ == '__main__':
    t = SuffixTree.SuffixTree()
    N = 5
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    mystrings = open('/usr/share/dict/words').readlines()[:N]
    for i in range(len(mystrings)):
        next_string = mystrings[i].strip()
        print "Adding %s" % next_string
        t.add(next_string, i+1)
    print "Our suffix tree has", t.num_nodes(), "nodes"
    print "The root has", t.root().num_children(), "children."
    depth(t.root())
