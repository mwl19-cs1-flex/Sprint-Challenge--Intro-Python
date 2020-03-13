# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    # the base class for all vehicles
    pass

class GroundVehicle(Vehicle):
    # the base class for ground vehicles
    # this includes: car, motorcycle
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

class FlightVehicle(Vehicle):
    # the base class for flight vehicles
    # this includes: starship, airplane
    pass

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass
