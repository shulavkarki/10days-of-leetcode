#Time complecity of getting number in stack is in constant. O(1)
#Solution : To keep record of all minium



class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.minimum:
            self.minimum.append(val)
        else:
            temp = self.minimum[len(self.minimum)-1]
            if temp>=val:
                self.minimum.append(val)
            else:
                self.minimum.append(temp)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack and self.minimum:
            self.stack.pop()
            self.minimum.pop()
            

    def top(self):
        """
        :rtype: int
        """
        length = len(self.stack)
        return self.stack[length - 1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum[len(self.minimum)-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

