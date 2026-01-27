#printing numbers from 1 to n
class NumberPrint:
    def __init__(self,n):
        self.n=n
    def print_numbers(self):
        for i in range(1,self.n+1):
            print(i,end=" ")
obj=NumberPrint(10)
obj.print_numbers()