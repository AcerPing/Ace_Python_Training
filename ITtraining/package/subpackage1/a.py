from . import b

def bar(mydata):
    print('Hello! function "bar" from module "a" calling.')
    print('mydata = {}'.format(mydata))
    b.foo()