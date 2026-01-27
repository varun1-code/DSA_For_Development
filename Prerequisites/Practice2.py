# sum of N numbers
class Sum_of_numbers:
    def __init__(self,n):
        self.n=n
    def total(self):
        sum=0
        for i in range(1,self.n+1):
            sum+=i
            print("Sum after adding",i,"is",sum)
obj=Sum_of_numbers(10)
obj.total()