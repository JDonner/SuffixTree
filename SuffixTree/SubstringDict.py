from SuffixTree import SuffixTree
import sys


class SubstringDict:
    def __init__(self, debug_flag=0):
        self._trees = [SuffixTree()]
        self._dict = {}
        self._debug_flag = debug_flag
        self._next_index = 1

    def _addToTree(self, key):
        """Adds a key into one of the SuffixTrees, and returns the
        string index of that key.

        There's a reason why this insertion is a little complicated:
        SuffixTree structure can hold, at most, strmat.MAXNUMSTR
        strings and strmat.MAXNUMNODES nodes.  If we go beyond that,
        the add() will fail.  To solve this, we use multiple
        trees."""
        (index, self._next_index) = (self._next_index, self._next_index + 1)
        ok = self._trees[-1].add(key, index)
        if ok:
            return index
        self.debug("Now expanding the tree:")
        self._trees.append(SuffixTree())
        ok = self._trees[-1].add(key, index)
        assert(ok)
        return index
        

    def _lookupKeys(self, subkey):
        """Given a substring of a key, return all indices that
        correspond."""
        results = []
        for tree in self._trees:
            num_matched, node, pos = tree.match(subkey)
            ## if the whole subkey didn't match, we say that there's no match
            ## this can be changed easily to be more versatile.
            if num_matched != len(subkey):
                pass
            else:
                results.extend(getAllIndices(node))
        return uniq(results)
    
    def __setitem__(self, key, value):
        index = self._addToTree(key)
        self._dict[index] = value

    def __getitem__(self, index):
        indices = self._lookupKeys(index)
        return [self._dict[i] for i in indices]

    def debug(self, msg):
        if self._debug_flag:
            print >>sys.stderr, msg

##     def keys(self): return _dict.keys()
##     def values(self): return _dict.values()
##     def size(self): return len(self.values())



def uniq(l):
    """Returns a list of the unique elements of l."""
    dict = {}
    for item in l: dict[item] = 1
    return dict.keys()


def getAllIndices(node):
    """Given a node, return all string ids of the node and its
    children.  Written nonrecursively to avoid potential stack
    problems.  If performance suffers, we can code this in C."""
    stack = [node]
    results = []

    while stack:
        node = stack.pop()
        results.extend(getLeafIds(node))
        child, num_children = node.children(), node.num_children()
        for i in range(num_children):
            stack.append(child)
            child = child.next()
    return results


def getLeafIds(node):
    results = []
    for i in range(node.num_leaves()):
        results.append(node.leaf(i+1)[2])
    return results




######################################################################
## Test harness

def _dictWordsTree(n = -1):
    words = map(lambda x:x.strip(),
                open('/usr/share/dict/words').readlines())
    if n >= 0: words = words[:n]    
    d = SubstringDict()
    for w in words:
        d[w] = w
    return d


def _testWithDictWords():
    print "Reading the dictionary.  Please wait."
    d = _dictWordsTree()
    print """Please enter a word; I'll look for all entries in the dictionary
that have the word as a substring."""
    while 1:
        word = raw_input("word? ")
        results = d[word]
        print len(results), "words found: "
        print results


if __name__ == '__main__':
    _testWithDictWords()
