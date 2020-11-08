def printDecimal(n):
    return n


def printOctal(n):
    return oct(n)[2:]


def printHexadecimal(n):
    return hex(n)[2:].upper()


def printBinario(n):
    return bin(n)[2:]


def imprimirTabela():
    print('Decimal\t\tOctal\t\tHexadecimal\tBinario')
    print('-------\t\t-----\t\t-----------\t-------')
    for x in range(256):
        print('{}\t\t{}\t\t{}\t\t{}'.format(printDecimal(x),
                                            printOctal(x), printHexadecimal(x), printBinario(x),))


imprimirTabela()
