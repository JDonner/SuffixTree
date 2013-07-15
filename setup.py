from distutils.core import *

setup(name='SuffixTree',
      version='0.7',
      description="Suffix Trees data structure",
      author="Danny Yoo",
      author_email="dyoo@hkn.eecs.berkeley.edu",
      packages=['SuffixTree'],
      package_dir = {'SuffixTree': 'SuffixTree'},
##       py_modules = ['SuffixTree',
##                     'SubstringDict'],
      ext_modules=[Extension('SuffixTree.SuffixTreec',
                             ['src/stree.c',
                              'src/SuffixTree_wrap.c',
                              'src/SuffixTree.c'],
                             )
                   ],
      )

                             
      
                    
                              
