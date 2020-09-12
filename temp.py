import numpy as np

class Node:
    def __init__ (self, valor):
        self.valor = valor
        self.next = None
    
    def mostra_no (self):
        print (self.valor)

class LinkedList:
    def __init__ (self):
        self.head = None

    def insere_inicio (self, valor):
        new = Node (valor)
        new.next = self.head
        self.head = new

    def mostrar (self):
        atual = self.head
        while atual:
            atual.mostra_no()
            atual = atual.next

    def exclui_inicio (self):
        temp = self.head
        self.head = self.head.next 
        if self.head:
            return temp
        else:
            return self.head

lista = LinkedList ()
lista.insere_inicio(8)
lista.insere_inicio(10)
lista.insere_inicio(3)
lista.mostrar()
lista.insere_inicio(6)
lista.mostrar()
lista.insere_inicio(-7)
lista.mostrar()
lista.exclui_inicio()
lista.mostrar()
lista.exclui_inicio()
lista.exclui_inicio()
lista.exclui_inicio()
lista.mostrar()
lista.exclui_inicio()
lista.mostrar()
