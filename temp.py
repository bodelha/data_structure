import numpy as np

class Deque:
    def __init__ (self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.fim = 0
        # self.numero_elementos = 0
        self.valores = np.empty (self.capacidade, dtype=int)

    def __deque_cheio (self):
        # return self.numero_elementos == self.capacidade
        return (self.inicio == 0 and self.fim == self.capacidade -1) or self.inicio == self.fim + 1


    def __deque_vazio (self):
        # return self.numero_elementos == 0
        return self.inicio == -1

    def inserir_inicio (self, valor):
        if self.deque_cheio():
            print ('Cheio')
            return
        if self.inicio == -1:
            self.inicio = 0
            self.fim = 0
        elif self.inicio == 0:
            self.inicio = self.capacidade -1
        else:
            self.inicio -= 1
        self.valores [self.inicio] = valor

    def inserir_final (self, valor):
        if self.deque_cheio():
            print ('Cheio')
            return
        if self.inicio == -1:
            self.inicio += 1
            self.fim = 0
        elif self.fim == self.capacidade - 1:
            self.fim = 0
        else:
            self.fim += 1
        self.valores [self.fim] = valor

    def exlui_inicio(self):
        if self.__deque_vazio():
            print ("Vazio")
            return
        if self.inicio == self.fim:
            self.inicio = -1
            self.fim = 0
        elif self.inicio != self.capacidade -1:
            self.inicio += 1
        else:
            self.inicio = 0

    def exclui_final (self):
        if self.__deque_vazio():
            print ("Vazio")
            return
        if self.inicio == self.fim:
            self.inicio = -1
            self.fim = 0
        elif self.fim == 0:
            self.fim == self.capacidade -1
        else:
            self.fim -= 1

    def get_inicio (self):
        if self.__deque_vazio():
            print ("Vazio")
            return
        return self.valores[self.inicio]

    def get_fim (self):
        if self.__deque_vazio():
            print ("Vazio")
            return
        return self.valores[self.fim]