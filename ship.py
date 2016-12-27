from enum import IntEnum
from systems import *
from fileUtils import *

class StationDirection(IntEnum):
  Down  = 0
  Right = 1
  Up    = 2
  Left  = 3
  none  = 4
  
class WeaponState(IntEnum):
  Disarmed = 0
  Armed    = 1
  
class RoomSquare:
  fireHealth = 0
  ignitionProgress = 0
  extinguishmentProgress = 0

class Room:
  oxygenLevel = 0
  squares = []
  stationSquare = 0
  stationDirection = StationDirection.none

class Breach:
  x = 0
  y = 0
  health = 0

class Door:
  maxHealth = 0
  health = 0
  nominalHealth = 0
  open = False
  inUse = False
  unknown_alpha = 0
  unknown_beta = 0
  
class CrystalLockdown:
  x = 0
  y = 0
  speed = 0
  goalX = 0
  goalY = 0
  arrived = False
  done = False
  lifetime = 0
  superFreeze = False
  lockingRoom = 0
  animationDirection = 0
  shardProgress = 0
  
class Weapon:
  name = ""
  armed = WeaponState.Disarmed

class Drone:
  type = ""
  isArmed = False
  isPlayerControlled = True
  x = 0
  y = 0
  roomID = 0
  roomSquare = 0
  health = 0
  
class MainShip:
  unknown_alpha = 1
  unknown_beta = 87
  unknown_gamma = 0
  unknown_delta = 0
  health = 0
  fuel = 0
  drones = 0
  missiles = 0
  reservePowerCapacity = 0
  system = []
  clonebayInfo = ClonebayInfo()
  batteryInfo = BatteryInfo()
  shieldInfo = ShieldInfo()
  room = []
  breach = []
  door = []
  lockdown = []
  weapon = []
  drone = []
  augment = []
  cargo = []
  
  def read(f):
    self.unknown_alpha = getInt(f)

