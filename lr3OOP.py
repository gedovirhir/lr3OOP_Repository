from abc import ABC, abstractmethod
from random import randint, choice
import time

class __storageList__(ABC): #снаружи наше "хранилище" ведет себя как список
    @abstractmethod
    def __init__(self): #ининциализация списка
        pass
    def add(self, x, index): #добавление элемента по индексу
        pass
    def getNode(self, index): #получение узла по индексу
        pass
    def cotnains(self, name): #проверка наличия элемента в узлах списка
        pass
    def isEmpty(self): #проверяет список на наличие хотя бы 1го элемента 
        pass
    def deleteIndex(self, index): #удаление элемента по индексу
        pass
    def show(self): #вывод элементов 
        pass
    def clear(self): #очистка списка
        pass 


"""
Наше хранилище будет реализовывать идею зоопарка, где изначальным классом-предком является listZoo, который в свою очередь является предком __storageList__,
абстрактного класса-интерфейса реализующего методы двусвязного списка. В качестве композиции в классе listZoo используется класс Node для определения узлов списка
"""
class Node(object):
    def __init__(self, x = None, v = None):
        self.key = x
        self.next = None
        self.prev = v

class listZoo(__storageList__): #внутри наше "хранилище" ведет себя тоже как список
    def __init__(self):
        self.head = None
        self.len = 0

        self.animalName = "Its not animal, just a cage :)"
        self.weightOfAnimal = 0

    def add(self, x, index = None):
        newNode = Node(x)
        if self.head is None:
            self.head = newNode
            self.len += 1
            return
        lastNode = self.head
        if index:
            for i in range(index):
                if (lastNode.next):
                    lastNode = lastNode.next
        else:
            while lastNode.next:
                lastNode = lastNode.next
        if lastNode.next:
            lastNode.next.prev = newNode
            newNode.next = lastNode.next
        lastNode.next = newNode
        newNode.prev = lastNode
        self.len += 1

    def getNode(self, index):
        if index > self.len-1: IndexError("IndexError")
        lastNode = self.head
        for i in range(index):
            lastNode = lastNode.next
        return lastNode
    
    def cotnains(self, name):
        lastNode = self.head
        while (lastNode):
            if name == lastNode.key:
                return True
            else:
                lastNode = lastNode.next
        return False

    def isEmpty(self):
        if self.head:
            return False
        else:
            return True

    def deleteIndex(self, index):
        lastNode = self.head
        if index == 0:
            self.head = lastNode.next
            if lastNode.next:
                lastNode.next.prev = None
            self.len -= 1
            return
        lastNode = self.getNode(index)
        
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
    
    def clear(self):
        for i in range(self.len):
            self.deleteIndex(0)

    def getInfo(self):
        result = ""
        for i in self.__dict__.items():
            result += (i[0] + ": " + str(i[1]) + ", ")
        result += '\n'
        return result
    
    def __str__(self):
        return self.animalName

    def setDefaultCharacteristic(self,name, weight):
        self.animalName = name
        self.weightOfAnimal = weight
    
    def addCharacteristic(self, nameOfCharacteristic, value):
        self.__dict__.update({nameOfCharacteristic : value})

class Dog(listZoo):
    def __init__(self, weight):
        self.setDefaultCharacteristic("Dog", weight)
class Cat(listZoo):
    def __init__(self, weight):
        self.setDefaultCharacteristic("Cat", weight)
class Donkey(listZoo):
    def __init__(self, weight):
        self.setDefaultCharacteristic("Donkey", weight)
class Antilope(listZoo):
    def __init__(self, weight):
        self.setDefaultCharacteristic("Antilope", weight)

start_time = time.time()

MyStor = listZoo()
avaliableCharct = {"Height": randint(50, 170), "Age" : randint(0, 15), "Sex" : choice(["Male", "Female"]), "Name" : choice(["Richard","Rasmus", "Tony", "Aubrey", "Don Juan", "Graham","George" ]) }

for i in range(5):
    newObject = choice([Dog(randint(20,30)), Cat(randint(3,5)), Donkey(randint(120,380)),Antilope(randint(100,200))])
    name, weight = choice(list(avaliableCharct.items()))
    newObject.addCharacteristic(name, weight)
    MyStor.add(newObject)
print("Введите количество случайных итераций\n")
n = int(input())
for i in range(n):
    ite = randint(1,3)
    if ite == 1:
        newObject = choice([Dog(randint(20,30)), Cat(randint(3,5)), Donkey(randint(120,380)),Antilope(randint(100,200))])
        name, weight = choice(list(avaliableCharct.items()))
        newObject.addCharacteristic(name, weight)
        if not MyStor.isEmpty():
            MyStor.add(newObject, randint(0,MyStor.len-1))
        else:
            MyStor.add(newObject)
    elif ite == 2:
        if not MyStor.isEmpty():
            MyStor.deleteIndex(randint(0,MyStor.len-1))
    elif ite == 3:
        if not MyStor.isEmpty():
            someObject = MyStor.getNode(randint(0,MyStor.len-1))
            print(someObject.key.getInfo())
    

print("Время выполнения программы: " + str(time.time() - start_time))