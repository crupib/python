class Trail():
    """A class to represent trails."""
    def __init__(self, dest, len=0):
       self.dest = dest
       self.len = len
    def describe_trail(self):
       """Print a description of trail."""
       desc = f"This trail goes to {self.dest}."
       if self.len:
          desc += f"\nThe trail is {self.len}km."
       print(desc)
verst = Trail("Mt. Verstovia", 4)
print(f"Destination: {verst.dest}")
verst.describe_trail()

