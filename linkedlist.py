class Node:
    #Create a Node for LinkedList
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    #Print method for linkedlist
    def printList(self):
        temp = self.head
        #Iterate on 'temp' node and print its data
        while (temp):
            print(temp.data)
            temp = temp.next
#Inserting a Node
    #Inserting a Node at the head
    def push(self, new_data):
        #Create a new node
        new_node = Node(new_data)

        #Make next of new_node as Head
        new_node.next = self.head
        #Head changed to new_node
        self.head = new_node

    #Insert Node at a given position. Previous node position req
    def insertAfter(self, prev_node, new_data):
        #If prev_node doesn't exist
        if prev_node is None:
            return
        #Create new node
        new_node = Node(new_data)

        #New node to position after prev_node
        new_node.next = prev_node.next

        #next of prev_node as new_node
        prev_node.next = new_node

    #Add node in the end
    def append(self, new_data):
        new_node = Node(new_data)

        #Check if LL is empty
        if self.head is None:
            self.head = new_node
            return

        #Move to the last node
        last = self.head
        while(last.next):
            last = last.next

        #Change the next of last node
        last.next = new_node

#Deleting a Node

    #Delete a node with a key (Data)
    def deleteNode(self, key):
        temp = self.head

        #If head node is the key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        #if key not in LL
        if temp == None:
            return

        #Remove links from LL
        prev.next = temp.next

        temp = None

    def deleteNodePos(self, position):
        #if empty
        if self.head == Node:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return
        #Get to the position
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        #If position is higher than LL size
        if temp is None:
            return
        if temp.next is None:
            return
        #temp.next is to be deleted
        x = temp.next.next

        temp.next = None
        temp.next = x
#Count the size of/number of elements in LL
    def getCount(self):
        count = 0
        temp = self.head

        while temp is not None:
            temp = temp.next
            count += 1
        return count
    #Recursive method for count
    def getCountRec(self, node):
        if(not node):
            return 0
        else:
            return 1+self.getCountRec(node.next)

#Searching elements
    def search(self, key):
        temp = self.head

        #check if element is on the head node
        if temp is not None:
            if temp.data == key:
                return True

        while(temp is not None):
            if temp.data == key:
                return True
            else:
                temp = temp.next

        return False

#Swapping Nodes x and y (in place)
    def swapNodes(self, x, y):
        #If x and y are same, no need to swap
        if x == y:
            return

        #Start searching for x
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        #Search for y
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
        #If x and y are not present, return!
        if currX == None or currY == None:
            return

        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY
        #If x is not head
        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY

        #If y is not head
        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp


    #Find Nth element
    def getNth(self, index):

        temp = self.head
        count = 0

        while(temp):
            if (count == index):
                return temp.data
            count += 1
            temp = temp.next

        assert(false)
        return 0

    #Find middle element
    def findMiddle(self):
        temp = self.head
        tick = False
        half = self.head
        while temp:
            temp = temp.next
            if tick:
                half = half.next
            tick = not tick
        return half.data

    #print Nth from last
    def printNthfromLast(self, n):
        main_ptr = self.head
        ref_ptr = self.head

        count = 0
        while (count < n):
            if (ref_ptr is None):
                return #n > LL size
            ref_ptr = ref_ptr.next
            count += 1

        while(ref_ptr is not None):
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next

        return main_ptr.data

    #Get count for repetitions of a no.
    def countRep(self, num):
        temp = self.head
        count = 0

        while temp is not None:
            if temp.data == num:
                count += 1
            temp = temp.next
        return count

    #Detect loop in a LL
    def detectLoop(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while (slow_ptr and fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                return True
        return False



if __name__ == '__main__':
    llist = LinkedList()

    llist.push(40)
    llist.push(5)
    llist.push(1)
    llist.push(4)
    #llist.push(7)
    #llist.push(16)
    #llist.push(1)
    #llist.push(1)
    #llist.push(56)
    #llist.printList()
    #print('Count =', llist.getCountRec(llist.head))
    #llist.deleteNodePos(3)
    #llist.swapNodes(40,7)
    print("After")
    #print('Nth element :', llist.getNth(10))
    #print('Middle element :', llist.findMiddle())
    #print('Nth element from the end :', llist.printNthfromLast(1))
    #print('Count of 1s repeting :', llist.countRep(1))
    llist.head.next.next.next.next = llist.head
    print(llist.detectLoop())
    #llist.printList()
    #print('Count =', llist.getCount())
    #llist.printList()
    #print('If Found = ', llist.search(200))
