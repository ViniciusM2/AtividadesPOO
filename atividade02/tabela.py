def printDecimal(n):
    print(n, end='')


def printOctal(n):
    print(oct(n)[2:], end='')


def printHexadecimal(n):
    print(hex(n)[2:].upper(), end='')


def printBinario(n):
    print(bin(n)[2:], end='')


<<<<<<< HEAD
def imprimirTabela():
=======
def printTabela():
>>>>>>> bf54236a54d6fa6472fedcf8b8d42f724c452b93
    print('Decimal\t\tOctal\t\tHexadecimal\tBinario')
    print('-------\t\t-----\t\t-----------\t-------')
    for x in range(256):
        printDecimal(x)
        print('\t\t', end='')
        printOctal(x)
        print('\t\t', end='')
        printHexadecimal(x)
        print('\t\t', end='')
        printBinario(x)
        print()


<<<<<<< HEAD
imprimirTabela()
=======
printTabela()
>>>>>>> bf54236a54d6fa6472fedcf8b8d42f724c452b93
