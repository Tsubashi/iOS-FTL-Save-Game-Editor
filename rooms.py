from fileUtils import *
from enum import IntEnum, Enum

class StationDirection(IntEnum):
  Down  = 0
  Right = 1
  Up    = 2
  Left  = 3
  none  = 4

RoomCount = {
    "PLAYER_SHIP_HARD": {
        "rooms": 17
       ,"squares": 48
       ,"doors": 26
  }
  , "PLAYER_SHIP_CIRCLE": {
      "rooms": 16
    , "squares": 42
    , "doors": 22
  }
  , "PLAYER_SHIP_CIRCLE_2": {
      "rooms": 14
    , "squares": 32
    , "doors": 21
  }
}          
             
class RoomSquare:
  fireHealth = 0
  ignitionProgress = 0
  extinguishmentProgress = 0
  
  def __init__(self,f):
    self.read(f)
  
  def read(self,f):
    self.fireHealth = getInt(f)
    self.ignitionProgress = getInt(f)
    self.extinguishmentProgress = getInt(f)

  def write(self,f):
    writeInt(self.fireHealth, f)
    writeInt(self.ignitionProgress, f)
    writeInt(self.extinguishmentProgress, f)


class Room:
  oxygenLevel = 0
  squares = []
  stationSquare = 0
  stationDirection = StationDirection.none
  
  def __init__(self,f):
    self.read(f)
  
  def read(self,f):
    self.oxygenLevel = 0
    self.squares = []
    self.stationSquare = 0
    self.stationDirection = StationDirection.none
  
class Breach:
  x = 0
  y = 0
  health = 0
  
  def __init__(self,f):
    self.read(f)
  
  def read(self,f):
    self.x = getInt(f)
    self.y = getInt(f)
    self.health = getInt(f)

  def write(self,f):
    writeInt(self.x, f)
    writeInt(self.y, f)
    writeInt(self.health, f)

class Door:
  maxHealth = 0
  health = 0
  nominalHealth = 0
  open = False
  inUse = False
  unknown_alpha = 0
  unknown_beta = 0
  
  def __init__(self,f):
    self.read(f)
  
  def read(self,f):
    self.maxHealth = getInt(f)
    self.health = getInt(f)
    self.nominalHealth = getInt(f)
    self.open = getBool(f)
    self.inUse = getBool(f)
    self.unknown_alpha = getInt(f)
    self.unknown_beta = getInt(f)

  def write(self,f):
    writeInt(self.maxHealth, f)
    writeInt(self.health, f)
    writeInt(self.nominalHealth, f)
    writeBool(self.open, f)
    writeBool(self.inUse, f)
    writeInt(self.unknown_alpha, f)
    writeInt(self.unknown_beta, f)

class CrystalLockdown:
  x = 0
  y = 0
  speed = 0
  goalX = 0
  goalY = 0
  hasArrived = False
  isDone = False
  lifetime = 0
  isSuperFreeze = False
  lockingRoom = 0
  animationDirection = 0
  shardProgress = 0
  
  def __init__(self,f):
    self.read(f)
  
  def read(self,f):
     self.x = getInt(f)
     self.y = getInt(f)
     self.speed = getInt(f)
     self.goalX = getInt(f)
     self.goalY = getInt(f)
     self.hasArrived = getBool(f)
     self.isDone = getBool(f)
     self.lifetime = getInt(f)
     self.isSuperFreeze = getBool(f)
     self.lockingRoom = getInt(f)
     self.animationDirection = getInt(f)
     self.shardProgress = getInt(f)

  def write(self,f):
     writeInt(self.x, f)
     writeInt(self.y, f)
     writeInt(self.speed, f)
     writeInt(self.goalX, f)
     writeInt(self.goalY, f)
     writeBool(self.hasArrived, f)
     writeBool(self.isDone, f)
     writeInt(self.lifetime, f)
     writeBool(self.isSuperFreeze, f)
     writeInt(self.lockingRoom, f)
     writeInt(self.animationDirection, f)
     writeInt(self.shardProgress, f)
