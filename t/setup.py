from distutils.core import *

setup(name='strmat',
      version='0.6',
      py_modules=["strmat"],
      ext_modules=[Extension('strmatc',
                             ['stree.c', 'strmat_wrap.c'],
                             ## define_macros=[('STRMAT', 1),
                             ##                ('STATS', 1)]
                             )])

                             
      
                    
                              
