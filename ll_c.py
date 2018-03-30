class Node:
    
    def __init__(self, value):
        self.n = value
        self.next = None
        
first = None
    
def main():
    
    while True:
        
        # print instructions
        print('\nMENU\n\n1 - delete\n2 - insert\n3 - search\n4 - traverse\n0 - quit]n')
        
        # get command
        c = int(input("Command: "))
        if c == 0:
            break
        
        # try to execut command
        if c == 1:
            delete()
        elif c == 2:
            insert()
        elif c == 3:
            search()
        elif c == 4:
            traverse()
            
    # python frees the list before quitting
    
def delete():
    
    # prompt user for number
    print("Number to delete: ")
    n = int(input())
    
    global first
    # get ll's first node
    ptr = first
    
    # try to delete number from the ll
    predptr = None
    while ptr != None:
        
        # check for number {. and -> same primitive types python uses . for non primitive python uses ->}
        if ptr.n == n:
            
            # delete from the head {you can compare addresses but not access it ex. Node(1) != Node(1); for arrays you can't even compare addresses [1] == [1]}
            if ptr == first:
                
                first = ptr.next
                # auto free
            
            # delete from middle or tail
            else:
                predptr.next = ptr.next
        
        else:
            
            predptr = ptr
            ptr = ptr.next
    
    # traverse ll
    traverse()
    
def insert():
    
    print("Number to insert: ")
    n = int(input())
    newptr = Node(n)
    
    global first
    # check for empty list
    if first == None:
        
        first = newptr
        
    # else check if number belongs at list's head
    elif newptr.n < first.n:
        
        newptr.next = first
        first = newptr
    
    # else try to insert in the middle or the tail
    else:
        predptr = first # HERE predptr is ptr 
        while True:
            
            if predptr.n == newptr.n:
                # free
                break
            
            # check for insertion at tail
            elif predptr.next == None:
                
                predptr.next = newptr
                break
            
            # check for insertion in middle
            elif predptr.next.n > newptr.n:
                
                newptr.next = predptr.next
                predptr.next = newptr
                break
            
            predptr = predptr.next
    
    # traverse list            
    traverse()
        
        
def search():
    
    print("Number to search for: ")
    n = int(input)
    
    ptr = first
    
    while ptr != None:
        
        if ptr.n == n:
            print('Found')
            return True
            
        ptr = ptr.next
        
    print('Not found')
    return False
    
    
def traverse():
    
    ptr = first
    while ptr != None:
        
        print(ptr.n)
        ptr = ptr.next
        
        
if __name__ == '__main__':
    main()
    
