""" 1) Add a method to the Point class from the reading today called midpoint(self,
point) that returns a new Point representing the midpoint of the line segment
between self and other.
For example, if p1 = Point(3, 2) and p2 = Point(7, 4) then p1.midpoint(p2)
should return Point(5, 3). p1.midpoint(p2) should also return Point(5,
3)."""

from cmath import sqrt


class Point:
 def __init__(self, x_coord, y_coord):
  self.x = x_coord
  self.y = y_coord

def distance(self, point):
 return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

def distance_from_origin(self):
 zero_point = Point(0, 0)
 return self.distance(zero_point) 

def midpoint(self, point):
 mid_x = (self.x + point.x) / 2
 mid_y = (self.y + point.y) / 2
 return Point(mid_x, mid_y)

def negate(self):
 return Point(-1 * self.x, -1 * self.y)
