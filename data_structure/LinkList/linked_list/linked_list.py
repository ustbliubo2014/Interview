# -*- coding:utf-8 -*-
__author__='liubo'



class Node(object):
    def __init__(self, val, p=None):
        self.data = val
        self.next = p



class LinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None#利用一个元素存储tail可以方便从链表尾部插入
        self.length = 0#利用一个元素保存链表长度


    def __getitem__(self, index):
        # 去第index元素
        if self.is_empty():
            print 'linklist is empty.'
            return
        elif index < 0 or index > self.getlength():
            print 'the given index is error'
            return
        else:
            return self.getitem(index)


    def __setitem__(self, index, value):
        # 将第index元素的值设置成value
        if self.is_empty():
            print 'linklist is empty.'
            return

        elif index < 0 or index > self.getlength():
            print 'the given key is error'
            return

        else:
            # 直接修改值就可以了
            self.setitem(index, value)
            return


    def setitem(self, index, value):
        # 将第index节点的值改为value
        if self.is_empty():
            print 'linklist is empty.'
            return

        elif index < 0 or index > self.getlength():
            print 'the given key is error'
            return

        else:
            # 直接修改值就可以了
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            current_node.value = value
            return


    def initlist(self,data):

        self.head = Node(data[0])

        p = self.head
        self.length = 0

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next
            self.length += 1
            self.tail = p


    def getlength(self):
        return self.length


    def is_empty(self):
        if self.getlength() ==0:
            return True
        else:
            return False


    def clear(self):
        self.head = None


    def append(self, item):
        q = Node(item)
        if self.getlength() == 0:
            self.head = q
            self.tail = q
        else:
            self.tail.next = q
            self.tail = q


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
        if self.is_empty() or index<0 or index >self.getlength():
            print 'Linklist is empty.'
            return

        if index ==0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p


    def delete(self, index):
        # 删除第index个元素
        if self.is_empty() or index < 0 or index > self.getlength():
            print 'Linklist is empty.'
            return

        # 删除第一个元素,需要修改头节点
        if index == 0:
            q = Node(self.head.data, self.head)
            self.head = q
            return

        p = self.head
        post = self.head
        j = 0
        while p.next != None and j < index:
            post = p
            p = p.next
            j += 1

        if index == j:
            post.next = p.next
        # 如果是最后一个元素,
        if index == self.getlength():
            self.tail = post


    def index(self, value):
        # 判断value在链表中的位置
        if self.is_empty():
            print 'Linklist is empty.'
            return

        p = self.head
        i = 0
        while p.next!=0 and not p.data ==value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1


    def travel_list(self):
        node = self.head
        while node != None:
            print node.data
            node = node.next


    def reverse_list(self):
        pre_node  = self.head
        self.tail = pre_node
        curr_node = pre_node.next
        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = pre_node
            pre_node = curr_node
            curr_node = next_node
        self.head.next = None
        self.head = pre_node


    def get_middle_node(self):
        double_head = self.head
        signal_head = self.head
        while double_head.next != None and double_head.next.next != None:
            double_head = double_head.next.next
            signal_head = signal_head.next
        return signal_head


if __name__ == '__main__':

    l = LinkList()
    print 'test init'
    l.initlist([1,2,3,4,5])
    print 'l.getitem(4)', l.getitem(4)
    print 'l.append(6)', l.append(6)
    print 'l.getitem(5)', l.getitem(5)

    print 'l.insert(4, 40)', l.insert(4, 40)

    print 'l.getitem(0)', l.getitem(0)
    print 'l.getitem(3)', l.getitem(3)
    print 'l.getitem(4)', l.getitem(4)
    print 'l.getitem(5)', l.getitem(5)

    print 'l.delete(5)', l.delete(5)
    print 'l.getitem(5)', l.getitem(5)

    print 'l.index(5)', l.index(5)

    print 'raw travel'
    l.travel_list()
    l.reverse_list()
    print 'reverse travel'
    l.travel_list()

    print 'l.tail.data', l.tail.data

    print 'l.get_middle_node().data', l.get_middle_node().data
