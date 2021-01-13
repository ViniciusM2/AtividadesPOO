from csv import reader
import matplotlib.pyplot as plt
import numpy as np
import random

def initialize():
    x = []
    y = []
    with open('csv0601.csv', 'r', encoding='utf-8') as tabelas:
        leitor = reader(tabelas, delimiter=',')
        
        for linha in leitor:
            x.append(linha[0])
            y.append((linha[1]))

        x.pop(0)
        y.pop(0)



    x = list(map(lambda i: int(i), x))
    y = list(map(lambda i: int(i), y))
    return x, y