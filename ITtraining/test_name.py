# write Fibonacci series up to n
def fib(n):
    ''' Print a Fibonacci series up to n. '''
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def main():
    a = fib(2000)
    print('test fib(2000)= {}'.format(a))


print(__name__)

if __name__ == '__main__':
    main()
    print(__name__)