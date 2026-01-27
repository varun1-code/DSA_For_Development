#even or odd number
class Classifcation:
    def __init__(self,n):
        self.n=n
    def check(self):
        if self.n%2==0:
            print(self.n,"is an Even number")
        else:
            print(self.n,"is an Odd number")
obj=Classifcation(7)
obj.check()