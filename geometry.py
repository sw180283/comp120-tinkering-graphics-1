import time
import random

def makeTriangle(origin, width, height, scale):
  return Polygon([
    origin, 
    Vector(width, 0, 0).scale(scale).add(origin), 
    Vector(0,height,0).scale(scale).add(origin)
    ])
    
def makeSquare(origin, width, height, scale):
  return Polygon([
    origin, 
    Vector(width, 0, 0).scale(scale).add(origin), 
    Vector(width,height,0).scale(scale).add(origin),
    Vector(0,height,0).scale(scale).add(origin),
    ])

def main():
  world = makeWorld(200, 200)
  turtle = makeTurtle(world)
  polygons = [] #makeTriangle(Vector(50, 10, 0), 10, 25, 2)
    
  for i in range(0,50):
    origin = Vector(random.randint(1, 175), random.randint(1, 175),0)
    length = random.randint(4, 20)
    scale = random.randint(1, 4)
    polygon = makeTriangle(origin, length, length, scale)
    polygons.append(polygon)
    
  for i in range(0, 90):
    
    #Draw polygons
    turtle.color = black
    for polygon in polygons:
      polygon.draw(turtle)
      resetTurtle(turtle)
    
    # Delay to slow running    
    time.sleep(0.1)
    
    # Reset the canvas 
    turtle.color = white 
    for polygon in polygons:
      polygon.draw(turtle)
      resetTurtle(turtle)
      
    # Update
    #polygons[0].rotate(pi/8)
    counter = 0
    for polygon in polygons:
      if counter % 2 == 0:
        polygon.rotate(pi/(random.randint(1,8)))
      else:
        polygon.rotate(pi/(random.randint(-8,-1)))
      
     
def resetTurtle(turtle):
  penUp(turtle)
  moveTo(turtle,0,0) 


class Polygon:

  def __init__(self, vertices):
    self.vertices = vertices

  def draw(self, turtle):
    penUp(turtle)
    moveTo(turtle, self.vertices[0].x, self.vertices[0].y)
    penDown(turtle)
    for vertex in self.vertices:
      turtle.moveTo(vertex.x, vertex.y)
    moveTo(turtle, self.vertices[0].x, self.vertices[0].y)
      
  def translate(self, vector):
    for vertex in self.vertices:
      vertex.add(vector)
      
  def rotate(self, radians):
    offset = self.vertices[0]
    for vertex in self.vertices:
      vertex.rotate(radians, offset)


class Vector:

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    
  def add(self, otherVector):
    self.x += otherVector.x
    self.y += otherVector.y
    self.z += otherVector.z
    return self
    
  def scale(self, scaleFactor):
    self.x *= scaleFactor
    self.y *= scaleFactor
    self.z *= scaleFactor
    return self    

  def rotate(self, rads, offset):
    x = self.x - offset.x
    y = self.y - offset.y
    self.x = int((x * cos(rads)) - (y * sin(rads)) + offset.x)
    self.y = int((x * sin(rads)) + (y * cos(rads)) + offset.y)
    
  