class Trail():
    """A class to represent trails."""
    def __init__(self, dest, len=0):
       self.dest = dest
       self.len = len
    def run_trail(self):
       """Simulate running the trail."""
       print(f"Running to {self.dest}.")
    def describe_trail(self):
       """Print a description of trail."""
       desc = f"This trail goes to {self.dest}."
       if self.len:
          desc += f"\nThe trail is {self.len}km."
       print(desc)
class BikeTrail(Trail):
    """Represent a bike trail."""
    def __init__(self, dest, len=0):
       super().__init__(dest,len)
       self.paved = True
       self.bikes_only = True
    def ride_trail(self):
       """Simulate riding the trail."""
       print(f"Riding to {self.dest}")   
       print(f"Paved? {self.paved}")
verst = Trail("Mt. Verstovia", 4)
print(f"Destination: {verst.dest}")
verst.describe_trail()
verst.run_trail()
ms = Trail("Middle Sister",10)
ms.describe_trail()
ms.run_trail()
cross_trail = BikeTrail("Harbor Mountain",5)
cross_trail.ride_trail()
