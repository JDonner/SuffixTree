from SubstringDict import SubstringDict
import MySQLdb, sys, readline, os
import re

def getAbstractDict(conn):
    cursor = conn.cursor()
    mydict = SubstringDict()
    number_of_results = cursor.execute('''select article_id, abstract
    from article''');
    print number_of_results, "articles found."
    print "Now generating suffix tree dictionary."
    print "This will take a minute.  You can get a cup of coffee."
    while 1:
        results = cursor.fetchone()
        if not results: break
        id, abstract = results
        abstract = addSentinels(cleanString(str(abstract)))
        if abstract.strip():
            mydict[abstract] = id
    print "Suffix tree dictionary constructed."
    return mydict


def getTermNames(conn):
    cursor = conn.cursor()
    number_of_results = cursor.execute('''select term.name from term''')
    results = []
    for i in xrange(number_of_results):
        term = cleanString(cursor.fetchone()[0])
        if term.strip():
            results.append(term)
    print number_of_results, "terms read."
    return results


def cleanString(s):
    return re.sub(r'[^\w]', ' ', str(s).lower().strip())


def addSentinels(s):
    return ' %s ' % s


def __test1(conn):
    print """Suffix Tree test1.  This program builds a suffix tree of
all the articles in Pub, and allows one to query for substrings."""
    d = getAbstractDict(conn)
    print
    print """Enter a string at the prompt, and I'll find out which articles
have that string in their abstracts."""
    while 1:
        s = raw_input(">>> ")
        if not s: continue
        article_ids = d[s.lower().strip()]
        print "Here are the article ids that match:", article_ids
    os._exit(0)


def __test2(conn):
    print """Suffix Tree test2.  This program builds a suffix tree of
all the articles in Pub, and tries generating all hits."""
    terms = getTermNames(conn)
    d = getAbstractDict(conn)
    count_hits = 0
    for t in terms:
        article_ids = d[addSentinels(t)]
        if article_ids:
            print "Matches found: here are the article ids that match '%s':"\
                  % t
            print article_ids, "\n\n"
            count_hits += len(article_ids)
    print count_hits, "total matches found."
    os._exit(0)


if __name__ == '__main__':
    try:
        conn = MySQLdb.connect(db='pub2')
##        __test1(conn)
        __test2(conn)
    except SystemExit, e:
        print "Quitting..."
        os._exit(0)
