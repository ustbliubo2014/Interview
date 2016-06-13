# encoding: utf-8
__author__ = 'liubo'

"""
@version: 
@author: 刘博
@license: Apache Licence 
@contact: ustb_liubo@qq.com
@software: PyCharm
@file: cat_dog_deque.py
@time: 2016/6/1 23:39
"""

from Queue import Queue
def func():
    pass


class Pet():
    def __init__(self, type):
        self.type = type


class Cat(Pet):
    def __init__(self, type):
        Pet.__init__(self, type)

class Dog(Pet):
    def __init__(self, type):
        Pet.__init__(self, type)

class PetQueue():
    def __init__(self):
        self.cat_num = 0
        self.dog_num = 0
        self.cat_deque = Queue()
        self.dog_deque = Queue()
        self.dog_type = 'dog'
        self.cat_type = 'cat'

    def put_dog(self, dog):
        self.dog_deque.put(dog)
        self.dog_num += 1

    def put_cat(self, cat):
        self.cat_deque.put(cat)
        self.cat_num += 1

    def poll_dog(self):
        if self.dog_num == 0:
            print 'Empty dog deque'
            return None
        else:
            self.dog_num -= 1
            return self.dog_deque.get()

    def poll_cat(self):
        if self.cat_num == 0:
            print 'Empty dog deque'
            return None
        else:
            self.cat_num -= 1
            return self.cat_deque.get()

    def put(self,pet):
        if pet.type == self.dog_type:
            self.put_dog(pet)
        elif pet.type == self.cat_type:
            self.put_cat(pet)
        else:
            print 'error type'


if __name__ == '__main__':
    dog = Dog('dog')
    cat = Cat('cat')

    petQueue = PetQueue()
    petQueue.put_cat(cat)
    petQueue.put(dog)
    print petQueue.dog_num
    print petQueue.cat_num
    print petQueue.poll_dog()