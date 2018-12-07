class Fib(object):

    count= 0

    def __init__(self,value=1000):
        self.a , self.b = 0 , 1
        self.count = value

    def __iter__(self):
        return self

    def __next__(self):
        self.a , self.b = self.b ,self.a + self.b
        if self.a > self.count:
            raise StopIteration()
        return self.a

    def __getitem__(self,n):
        a,b = 1,1
        for index in range(n):
            a , b = b , a + b
        return a


for n in Fib():
    print(n)

f=Fib()
print(f[5])
