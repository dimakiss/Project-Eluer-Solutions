
#Solution to problem 102
#https://projecteuler.net/problem=102
#Run time 11.0ms

#point object
class point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
#triangel object (colaction of 3 points)
class triangle:
    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def zerobet(self): #if we put a point inside a triangle and draw 3 lines to his points we will get 3 triangles
                   #if we calculate they area and sum up we would get the original triangle area
        zerop=point(0,0)
        return self.area(self.p1,self.p2,self.p3)==self.area(self.p1,self.p2,zerop)+self.area(self.p2,self.p3,zerop)+self.area(self.p3,self.p1,zerop)
    def area(self,p1,p2,p3):# the formula to calculate the area of a triangle by his points
        return 0.5*abs((p1.x-p3.x)*(p2.y-p1.y)-(p1.x-p2.x)*(p3.y-p1.y))

# the text file with all points
with open("points.txt",'r') as f:
    points=f.read().split('\n')

count=0
for p_coll in points:
    p_coll=p_coll.split(',')
    p1=point(int(p_coll[0]),int(p_coll[1]))
    p2 = point(int(p_coll[2]), int(p_coll[3]))
    p3 = point(int(p_coll[4]), int(p_coll[5]))
    t1 = triangle(p1, p2, p3)
    if t1.zerobet():
        count+=1
print(count)
#Answer: 228
