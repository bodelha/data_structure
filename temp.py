class Node:
    def __init__ (self, valor):
        self.valor = valor
        self.prev = None
        self.next = None

    def show (self):
        print (
            f"Valor = {self.valor}", 
            f"Anterior = {self.prev}", 
            f"Próximo = {self.next}", 
            sep='\n'
            )
    

class DoublyLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
    
    def __lista_vazia (self):
        if not self.head and not self.tail:
            print ("Vazia")
            return True
        return False

    def __adjust_left (self, new, old):
        if old:
            old.prev = new
        new.next = old
    
    def __adjust_right (self, old, new):
        if old:
            old.next = new
        new.prev = old

    def insere_inicio (self, valor):
        new = Node (valor)
        if self.__lista_vazia ():
            self.tail = new
        else:
            self =  self.__adjust_left (new, self.head)
        self.head = new

    def insere_final (self, valor):
        new = Node (valor)
        if self.__lista_vazia ():
            self.head = new
        else:
            self.__adjust_right (self.head, new)
        self.tail = new

    def exclui_inicio (self):
        if self.__lista_vazia():
            return
        self.__adjust_right (None, self.head.next)
        self.head = self.head.next

    def exclui_final (self):
        if self.__lista_vazia:
            return
        self.__adjust_left (self.tail.prev, None)
        self.tail = self.tail.prev

    def exclui_valor (self, valor):
        if self.head.valor == valor:
            return exclui_inicio ()
        if self.tail.valor == valor:
            return exclui_final ()
        atual1 = self.head.next
        atual2 = self.tail.prev
        while atual1.valor != valor or atual2.valor != valor:
            if atual1 == atual2 or atual1 == atual2.prev:
                print ('Não está na lista')
                return
            atual1 = atual1.next
            atual2 = atual2.prev
        atual = atual1 if atual1.valor == valor else atual2
        self.__adjust_left (atual.prev, atual.next)

    def mostrar (self):
        atual = self.head
        while atual:
            atual.show()
            atual = atual.next
        
lista = DoublyLinkedList()
lista.insere_final(3)
lista.insere_final(4)
lista.insere_inicio(9)
lista.insere_final(5)
lista.insere_inicio(1)
lista.insere_final(7)
lista.insere_final(-7)
lista.insere_inicio(-2)
lista.insere_final(6)
lista.mostrar()
lista.exclui_inicio()
lista.mostrar()
lista.exclui_final()
lista.mostrar()
lista.exclui_valor(9)
lista.mostrar()
lista.exclui_valor(9)
lista.mostrar()
lista.exclui_final()
lista.exclui_final()
lista.exclui_inicio()
lista.exclui_inicio()
lista.exclui_inicio()
lista.exclui_inicio()

