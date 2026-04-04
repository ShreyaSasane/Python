class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self):
        self.radius = float(input("enter the radius : "))

    def CalculateArea(self):
        self.area = self.PI * ((self.radius) ** (self.radius)) 
    
    def CalculateCircumference(self):
    
        self.circumference = 2 * self.PI * self.radius

    def Display(self):
        print("radius of the circle is : ",self.radius)
        print("area of circle is : ",self.area)
        print("circumference of circle is : ",self.circumference)


obj1 = Circle()

obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()