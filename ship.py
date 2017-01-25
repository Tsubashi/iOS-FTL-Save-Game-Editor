from enum import IntEnum, Enum
from systems import *
from fileUtils import *
from crew import *
from rooms import *
from animation import *
 
class Weapon:
  name = ""
  isArmed = False
  
  def __init__(self,f):
    self.read(f)
  
  def read(self,f):
    self.name = getString(f)
    self.isArmed = getBool(f)

  def write(self,f):
    writeString(self.name, f)
    writeBool(self.isArmed, f)

class Drone:
  type = ""
  isArmed = False
  isPlayerControlled = True
  x = 0
  y = 0
  roomID = 0
  roomSquare = 0
  health = 0
  
  def __init__(self,f):
    self.read(f)
  
  def read(self,f):
    self.type = getString(f)
    self.isArmed = getBool(f)
    self.isPlayerControlled = getBool(f)
    self.x = getInt(f)
    self.y = getInt(f)
    self.roomID = getInt(f)
    self.roomSquare = getInt(f)
    self.health = getInt(f)
  
  def write(self,f):
    writeString(self.type, f)
    writeBool(self.isArmed, f)
    writeBool(self.isPlayerControlled, f)
    writeInt(self.x, f)
    writeInt(self.y, f)
    writeInt(self.roomID, f)
    writeInt(self.roomSquare, f)
    writeInt(self.health, f)
  
class Ship:
  blueprintID = 0
  unknown_alpha = False
  jumpChargeTicks = 0
  isJumping = False
  jumpAnimationTicks = 0
  health = 0
  fuel = 0
  drones = 0
  missiles = 0
  cash = 0
  reservePowerCapacity = 0
  system = 0
  room = []
  breach = []
  door = []
  lockdown = []
  weapon = []
  drone = []
  augment = []
  cargo = []
  crew = []
  
  def __init__(self,blueprintID,f):
    self.blueprintID = blueprintID
    self.read(f)
  
  def read(self,f):
    self.unknown_alpha = getBool(f)
    self.jumpChargeTicks = getInt(f)
    self.isJumping = getBool(f)
    self.jumpAnimationTicks = getInt(f)
    self.health = getInt(f)
    self.fuel = getInt(f)
    self.drones = getInt(f)
    self.missiles = getInt(f)
    self.cash = getInt(f)
    self.crew = [CrewMember(f) for i in range(getInt(f))]
    self.reservePowerCapacity = getInt(f)
    self.system = SystemList(f)
    self.system.clonebay.readExtended(f)
    self.system.battery.readExtended(f)
    self.system.shields.readExtended(f)
    self.system.cloaking.readExtended(f)
    
    # Since room data requires info from the schematic file, and since we don't
    # HAVE that file, we'll just skip trying to do anything with it for now. 
    # Perhaps someday we will come back and find a better solution 
    roomDataSize = (4*3*RoomCount[self.blueprintID]['rooms'])+(4*3*RoomCount[self.blueprintID]['squares'])
    self.room = f.read(roomDataSize)
    
    self.breach = [Breach(f) for i in range(getInt(f))]
    
    # Since doors only require a single number from the schematic file, we'll 
    # just fudge it.
    self.doors = [Door(f) for i in range(RoomCount[self.blueprintID]['doors'])]
    
    self.system.cloaking.cloakAnimationTicks = getInt(f)
    self.lockdown = [CrystalLockdown(f) for i in range(getInt(f))]
    self.weapon = [Weapon(f) for i in range(getInt(f))]
    self.drone = [Drone(f) for i in range(getInt(f))]
    self.augment = [getString(f) for i in range(getInt(f))]
    
  def write(self,f):
    writeBool(self.unknown_alpha, f)
    writeInt(self.jumpChargeTicks, f)
    writeBool(self.isJumping, f)
    writeInt(self.jumpAnimationTicks, f)
    writeInt(self.health, f)
    writeInt(self.fuel, f)
    writeInt(self.drones, f)
    writeInt(self.missiles, f)
    writeInt(self.cash, f)
    writeInt(len(self.crew), f)
    for member in self.crew:
      member.write(f)
    writeInt(self.reservePowerCapacity, f)
    self.system.write(f)
    self.system.clonebay.writeExtended(f)
    self.system.battery.writeExtended(f)
    self.system.shields.writeExtended(f)
    self.system.cloaking.writeExtended(f)
    f.write(self.room)
    writeInt(len(self.breach), f)
    for b in self.breach:
      b.write(f)
    for door in self.doors:
      door.write(f)
    writeInt(self.system.cloaking.cloakAnimationTicks, f)
    writeInt(len(self.lockdown), f)
    for lock in self.lockdown:
      lock.write(f)
    writeInt(len(self.weapon), f)
    for w in self.weapon:
      w.write(f)
    writeInt(len(self.drone), f)
    for d in self.drone:
      d.write(f)
    writeInt(len(self.augment), f)
    for a in self.augment:
      writeString(a, f)
    writeInt(len(self.cargo), f)
    for c in self.cargo:
      writeString(c, f)
    
