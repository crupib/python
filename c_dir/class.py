from myclasslib import Trail, BikeTrail

verst = Trail("Mt. Verstovia", 4)
print(f"Destination: {verst.dest}")
verst.describe_trail()
verst.run_trail()
ms = Trail("Middle Sister",10)
ms.describe_trail()
ms.run_trail()
cross_trail = BikeTrail("Harbor Mountain",5)
cross_trail.ride_trail()
