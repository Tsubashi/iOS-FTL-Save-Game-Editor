from enum import IntEnum

class ShelfType(IntEnum):
  Weapon = 0
  Drone = 1
  Augment = 2
  Crew = 3
  System = 4
  
class ItemAvailability(IntEnum):
  Unavailable = -1
  Purchased = 0
  Available = 1

class Store:
  shelf = []
  fuelCount = 0
  missileCount = 0
  dronePartCount = 0
  
class StoreShelf:
  type = ShelfType.Weapon
  item = []
  
class StoreItem:
  availability = ItemAvailability.Unavailable
  itemID = ""
  extraData = 0
