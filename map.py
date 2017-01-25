from enum import IntEnum
from store import Store

class FleetType(IntEnum):
  none       = 0
  Rebel      = 1
  Federation = 2
  Both       = 3

class Sector:
  treeSeed = 0
  layoutSeed = 0
  fleetOffset = 0
  fleetFudge = 0
  fleetPursuitModulo = 0
  currentBeaconID = 0
  unknown_alpha = False
  unknown_beta = 0
  hazardsAreVisible = False
  flagshipIsVisible = False
  flagshipHop = 0
  flagshipIsMoving = False
  count = 0
  unknown_gamma = False
  number = 0
  isCrystalWorlds = False
  
class Quest:
  eventID = 0
  beaconID = 0

class Beacon:
  visitCount = 0
  bgStarscapeInnerPath = 0
  bgSpriteInnerPath = 0
  bgSpriteX = 0
  bgSpriteY = 0
  bgSpriteRotation = 0
  seen = False
  enemyIsPresent = False
  eventID = ""
  autoBlueprintID = ""
  eventSeed = ""
  fleetPresence = FleetType.none
  isUnderAttack = False
  isStore = False
  store = Store()
