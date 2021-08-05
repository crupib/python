"""A set of functions for calculating areas."""
import math		
def area_rect(w, h):
   """Calculate the area of a rectangle. """
   area = w * h
   if w >= 0:
      return area
   else:
      return None
def area_circle(r):
    """Calculate the area of a circle."""
    area_circle = math.pi * r * r 
    return area_circle
