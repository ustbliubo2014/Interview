# -*- coding:utf-8 -*-
__author__='liubo'



class Node(object):
    def __init__(self, value, pre=None, next=None):
        self.data = value
        self.next = pre
        self.prev = next


class LinkList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def __getitem__(self, key):
        # 取第k个元素
        if self.is_empty():
            print 'linklist is empty.'
            return
        elif key < 0 or key > self.getlength():
            print 'the given key is error'
            return
        else:
            return self.getitem(key)

    def __setitem__(self, key, value):
        if self.is_empty():
            print 'linklist is empty.'
            return
        elif key < 0 or key > self.getlength():
            print 'the given key is error'
            return
        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            node.prev = p
            p = p.next

    def getlength(self):
        p = self.head
        length = 0
        while p != None:
            length += 1
            p = p.next
        return length

    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False

    def clear(self):
        # 不能这样处理,里面的节点最好也删掉,否则会造成内存泄露
        p = self.head
        while p != None:
            tmp = p
            p = p.next
            del tmp
        self.head = Node

    def append(self,item):
        q = Node(item)
        if self.head == None:
            self.head = q
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = q
            q.prev = p

    def getitem(self, index):
        if self.is_empty():
            print 'Linklist is empty.'
            return
        j = 0
        p = self.head
        while p.next != None and j < index:
            p = p.next
            j += 1
        if j == index:
            return p.data
        else:
            print 'target is not exist!'

    def insert(self, index, item):
        # 将item插入到第i个元素的后面
        if self.is_empty() or index < 0 or index > self.getlength():
            print 'Linklist is empty.'
            return
        if index == 0:
            # 插入到head的后面
            if self.head == None:# 当前没有元素
                q = Node(item, pre=self.head, next=None)
                self.head.next = q
            else:
                tmp = self.head.next
                q = Node(item, pre=self.head, next=self.head.next)
                # 修改原链表中head后节点的pre
                tmp.prev = q
                self.head.next = q
            return
        p = self.head
        j = 0
        while p.next != None and j < index:
            p = p.next
            j += 1
        if index == j:
            pre = p
            next = pre.next
            q = Node(item, pre=pre, next=next)
            pre.next = q
            next.prev = q

    def delete(self, index):
        if self.is_empty() or index < 0 or index > self.getlength():
            print 'Linklist is empty.'
            return
        if index == 0:# 删除头节点后的第一个元素
            tmp = self.head.next
            self.head.next = tmp.next
            tmp.next.prev = self.head
            del tmp
            return

        p = self.head
        post = self.head
        j = 0
        while p.next != None and j < index:
            post = p
            p = p.next
            j += 1
        if index == j:
            if p.next == None:
                post.next = None
            else:
                post.next = p.next
                p.next.prev = post
            del p

    def index(self,value):
        if self.is_empty():
            print 'Linklist is empty.'
            return
        p = self.head
        i = 0
        while p.next != None and not p.data == value:
            p = p.next
            i += 1
        if p.data == value:
            return i
        else:
            return -1

    def travel(self):
        p = self.head
        print 'travel double list'
        while p != None:
            print p.data
            p = p.next


if __name__ == '__main__':
    l = LinkList()
    l.initlist([1, 2, 3, 4, 5])
    print l.getitem(4)
    l.append(6)
    print l.getitem(5)

    l.insert(4, 40)
    print l.getitem(3)
    print l.getitem(4)
    print l.getitem(5)

    l.delete(5)
    l.delete(1)
    l.delete(0)
    print l.getitem(5)

    l.index(5)

    l.travel()

