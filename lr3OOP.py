from abc import ABC, abstractmethod
import random

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

class listZoo(__storageList__): #внутри наше "хранилище" ведет себя тоже как список
    def __init__(self):
        self.head = None
        self.len = 0

    def add(self, x):
        newNode = Node(x)
        if self.head is None:
            self.head = newNode
            self.len += 1
            return
        lastNode = self.head
        while (lastNode.next):
            lastNode = lastNode.next
        lastNode.next = newNode
        newNode.prev = lastNode
        self.len += 1

    def deleteIndex(self, index):
        lastNode = self.head
        if index == 0:
            self.head = lastNode.next
            lastNode.next.prev = None
            self.len -= 1
            return
        for i in range(index):
            if lastNode.next:
                lastNode = lastNode.next
            else:
                raise IndexError("IndexError")
        
        if lastNode.next is not None:
            lastNode.next.prev = lastNode.prev
        lastNode.prev.next = lastNode.next

        del lastNode
        self.len -= 1

    def show(self):
        lastNode = self.head
        result = ""
        while lastNode:
            result += str(lastNode.key) + " "
            lastNode = lastNode.next
        result += "\n"
        print(result)
        print(self.len) 
        print("\n")
