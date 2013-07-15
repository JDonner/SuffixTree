import strmat

### Tests to see if we can add and remove strings

if __name__ == '__main__':
    t = strmat.SuffixTree()
    N = 8000
    mystrings = open('/usr/share/dict/words').readlines()[:N]
    for i in range(len(mystrings)):
        next_string = mystrings[i].strip()
        assert(t.add_string(next_string, i+1) == 1)
    for i in range(N):
        print "Removing %d" % (i+1)
        assert(t.remove_string(i+1) == 1)
