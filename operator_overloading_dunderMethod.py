# Working of Special/Dunder Methods ie ( __init__ (constructor) ,__str__ (used when print) ,__add__ (used when +) )                                                               

class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f" {self.i}i + {self.j}j + {self.k}k"  
    def __add__(self,x):   # x is that object
        print("Addition of vectors are below:")
        # return f"{self.i+x.i}i+{self.j+x.j}j+{self.k+x.k}k"   # This returns a string vector which we dont want 
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)         # This function returns a Vector Object when we print it ie Vector(8,11,11) 

v1=Vector(2,3,4)        # first object
print(v1)               # prints object without str dunder method otherwise prints whatever is inside the __str__ method
v2=Vector(6,8,7)        # second object    
print(v2)

print(v1+v2)     # python INTERNALLY calls: v1.__add__(v2) , So when the returned Vector(8, 11, 11) is printed, it calls: Vector(8, 11, 11).__str__()

print(type(v1+v2))       




 
