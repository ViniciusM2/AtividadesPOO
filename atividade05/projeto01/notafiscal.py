"""
    Módulo notafiscal -
    Classe NotaFiscal -
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado.
"""
import datetime
from cliente import Cliente
from produto import Produto
from itemnotafiscal import ItemNotaFiscal
from functools import reduce


class NotaFiscal():
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo = codigo
        self._cliente = cliente
        self._data = datetime.datetime.now()
        self._itens = []
        self._valorNota = 0.0

    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente

    def adicionarItem(self, item):
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)

    def calcularNotaFiscal(self):
        valor = 0.0
        for item in self._itens:
            valor = + item._valorItem
        self.valorNota = valor

    def imprimirlinha(self, item):
        seq = str(item._sequencial).zfill(3)
        return f"{seq:<8}{item._descricao:<52}{item._quantidade:<12}{item._valorUnitario:<20,.2f}{item._valorUnitario * item._quantidade:<8,.2f}"

    def imprimirNotaFiscal(self):
        date = f'{self._data.day}/{self._data.month}/{self._data.year}'
        header = f"""
        ----------------------------------------------------------------------------------------------------
        {'NOTA FISCAL':90}{date:10}                                                                               
        Cliente: {self._cliente._codigo}   Nome: {self._cliente._nome}
        CPF/CNPJ: {self._cliente._cnpjcpf}
        ----------------------------------------------------------------------------------------------------
        ITENS
        ----------------------------------------------------------------------------------------------------
        Seq     Descrição                                           QTD         Valor Unit          Preço
        ----    -----------------------------------------------    -----     --------------      -----------
            """
        print(header)
        
        for i, p in enumerate(self._itens):
            print(f"{'':8}",self.imprimirlinha(p),end='')
            if(i != len(self._itens) - 1):
                print('\n')


        valortotal = 0
        for item in self._itens:
            valortotal += item._valorUnitario * item._quantidade
        footer = f"""
        ____________________________________________________________________________________________________
        Valor Total: {valortotal:.2f}
                  """
        print(footer)
