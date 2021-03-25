import test_name
print(dir(test_name))
print(test_name.__file__)
print(test_name.__name__)
print()

from simple_package import a,b
a.bar()
b.bar()
print()

'''
from simple_package.a import *
bar()
bar1()
'''

import package