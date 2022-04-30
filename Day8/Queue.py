#First in is first out. FIFO 
def queue():

    tempStack = []
    #All 10 item is inserted into the stack 
    for item in range(10):
        tempStack.append(item)
    
    #for popping we pop method. Here I popped till the stack is empty
    for i in range(len(tempStack)):
        print(tempStack.pop(0)) #pop the last  item in the stack 
    
    

queue()