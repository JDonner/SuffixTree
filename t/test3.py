import strmat

### A small memory test: watch top to see if we're doing ok...

def depth(n):
    while n:
        foo, bar = n.edgestr(), n.labelstr()
        depth(n.children())
        n = n.next()



if __name__ == '__main__':
    for x in range(10):
        print "Iteration %d" % x
        t = strmat.SuffixTree()
        N = 8000
        mystrings = open('/usr/share/dict/words').readlines()[:N]
        for i in range(len(mystrings)):
            next_string = mystrings[i].strip()
            assert(t.add_string(next_string, i+1) == 1)
        print "Suffix tree built.  Now chasing through the tree."
        depth(t.root())
