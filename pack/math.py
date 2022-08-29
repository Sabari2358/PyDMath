import math
class perimeter:
    pi = 22/7
    def circle(self,r):
        return 2*self.pi*r

    def rectangle(self,l,b):
        return 2*(l+b)
    
    def square(self,l):
        return 4*l

    def triangle(self,a,b,c):
        return a+b+c
    
    def eq_triangle(self,a):
        return 3*a

    def parallelogram(self,a,b):
        return 2*(a+b)
    
    def trapezium(self,a,b,c,d):
        return a+b+c+d

    def isosceles_triangle(self,a,b):
        A = 2*a
        return A+b

class area:
    pi = 22/7
    def circle(self,r):
        return self.pi*(r**2)

    def rectangle(self,w,l):
        return w*l

    def square(self,a):
        return a**2

    def triangle(self,b,h):
        return (1/2)*(b*h)
    
    def eq_triangle(self,a):
        return (math.sqrt(3)/4)*(a**2)

    def parallelogram(self,b,h):
        return b*h

    def trapezium(self,a,b,h):
        num = (a+b)/2
        return num*h

    def isosceles_triangle(self,b,h):
        return (b*h)/2

class volume:
    pi = 22/7
    def sphere(self,r):
        return (4/3)*self.pi*(r**3)

    def cylinder(self,r,h):
        return self.pi*(r**2)*h

    def cube(self,a):
        return a**3

    def rectangular_prism(self,l,b,h):
        return l*b*h

    def cone(self,r,h):
        return (1/3)*self.pi*(r**2)*h

    def right_rectangular_pyramid(self,l,w,h):
        """           l = length 
           w = width
           h = height"""
        return (l*w*h)/3