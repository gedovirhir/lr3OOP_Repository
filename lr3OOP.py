from abc import ABC, abstractmethod

class __storageList__(ABC): #снаружи наше "хранилище" ведет себя как список
    @abstractmethod
    def __init__(self): #ининциализация списка
        pass
    def add(self, x): #добавление элемента 
        pass
    def deleteIndex(self, index): #удаление элемента
        pass
    def show(self): #вывод элементов 
        pass

class Node(object):
    def __init__(self, x = None, v = None):
        self.key = x
        self.next = None
        self.prev = v

class listZoo(__storageList__):
    def __init__(self):
        self.head = None
    def add(self, x):
        newNode = Node(x)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while (lastNode.next):
            lastNode = lastNode.next
        lastNode.next = newNode
        newNode.prev = lastNode
            