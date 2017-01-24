from fileUtils import *
from animation import *

class InitialCrewMember:
  race = ""
  name = ""
  
  def __init__(self,f):
    self.read(f)
  
  def read(self,f):
    self.race = getString(f)
    self.name = getString(f)
  
  def write(self, f):
    writeString(self.race, f)
    writeString(self.name, f)
      
class CrewMember:
  name = ""
  race = ""
  isEnemyBoardingDrone = False
  health = 0
  x = 0
  y = 0
  roomID = 0
  roomSquare = 0
  isPlayerControlled = True
  cloneReady = 0
  tint = []
  isMindControlled = False
  savedRoomSquare = 0
  savedRoomID = 0
  pilotSkill = 0
  engineSkill = 0
  shieldSkill = 0
  weaponSkill = 0
  repairSkill = 0
  combatSkill = 0
  isMale = False
  repairs = 0
  kills = 0
  evasions = 0
  jumpsSurvived = 0
  skillMasteries = 0
  stunTicks = 0
  healthBoost = 0
  clonebayPriority = 0
  damageBoost = 0
  unknown_alpha = 0
  universalDeathCount = 0
  pilotMasteryLvl1 = 0
  pilotMasteryLvl2 = 0
  engineMasteryLvl1 = 0
  engineMasteryLvl2 = 0
  shieldMasterLvl1 = 0
  shieldMasteryLvl2 = 0
  weaponMasteryLvl1 = 0
  weaponMasteryLvl2 = 0
  repairMasteryLvl1 = 0
  repairMasteryLvl2 = 0
  combatMasteryLvl1 = 0
  combatMasteryLvl2 = 0
  unknown_beta = False
  teleportAnimation = 0
  unknown_gamma = False
  # Crystal Attributes
  lockdownRechargeTick = 0
  lockdownRechargeTickGoal = 0
  unknown_delta = 0
  
  def __init__(self,f):
    self.read(f)
  
  def read(self,f):
    self.name = getString(f)
    self.race = getString(f)
    self.isEnemyBoardingDrone = getBool(f)
    self.health = getInt(f)
    self.x = getInt(f)
    self.y = getInt(f)
    self.roomID = getInt(f)
    self.roomSquare = getInt(f)
    self.isPlayerControlled = getBool(f)
    self.cloneReady = getInt(f)
    self.clonebayPriority = getInt(f)
    self.tint = [getInt(f) for i in range(getInt(f))]
    self.isMindControlled = getBool(f)
    self.savedRoomSquare = getInt(f)
    self.savedRoomID = getInt(f)
    self.pilotSkill = getInt(f)
    self.engineSkill = getInt(f)
    self.shieldSkill = getInt(f)
    self.weaponSkill = getInt(f)
    self.repairSkill = getInt(f)
    self.combatSkill = getInt(f)
    self.isMale = getBool(f)
    self.repairs = getInt(f)
    self.kills = getInt(f)
    self.evasions = getInt(f)
    self.jumpsSurvived = getInt(f)
    self.skillMasteries = getInt(f)
    self.stunTicks = getInt(f)
    self.healthBoost = getInt(f)
    if self.clonebayPriority != getInt(f):
      raise Exception("Clonebay Priority Mismatch")
    self.damageBoost = getInt(f)
    self.unknown_alpha = getInt(f)
    self.universalDeathCount = getInt(f)
    self.pilotMasteryLvl1 = getInt(f)
    self.pilotMasteryLvl2 = getInt(f)
    self.engineMasteryLvl1 = getInt(f)
    self.engineMasteryLvl2 = getInt(f)
    self.shieldMasterLvl1 = getInt(f)
    self.shieldMasteryLvl2 = getInt(f)
    self.weaponMasteryLvl1 = getInt(f)
    self.weaponMasteryLvl2 = getInt(f)
    self.repairMasteryLvl1 = getInt(f)
    self.repairMasteryLvl2 = getInt(f)
    self.combatMasteryLvl1 = getInt(f)
    self.combatMasteryLvl2 = getInt(f)
    self.unknown_beta = getBool(f)
    self.teleportAnimation = Animation(f)
    self.unknown_delta = getBool(f)
    if (self.race == "Crystal"):
      self.lockdownRechargeTick = getInt(f)
      self.lockdownRechargeTickGoal = getInt(f)
      self.unknown_gamma = getInt(f)
      
  def write(self, f):
    writeString(self.name, f)
    writeString(self.race, f)
    writeBool(self.isEnemyBoardingDrone, f)
    writeInt(self.health, f)
    writeInt(self.x, f)
    writeInt(self.y, f)
    writeInt(self.roomID, f)
    writeInt(self.roomSquare, f)
    writeBool(self.isPlayerControlled, f)
    writeInt(self.cloneReady, f)
    writeInt(self.clonebayPriority, f)
    writeInt(len(self.tint), f)
    for tint in self.tint:
      writeInt(tint, f)
    writeBool(self.isMindControlled, f)
    writeInt(self.savedRoomSquare, f)
    writeInt(self.savedRoomID, f)
    writeInt(self.pilotSkill, f)
    writeInt(self.engineSkill, f)
    writeInt(self.shieldSkill, f)
    writeInt(self.weaponSkill, f)
    writeInt(self.repairSkill, f)
    writeInt(self.combatSkill, f)
    writeBool(self.isMale, f)
    writeInt(self.repairs, f)
    writeInt(self.kills, f)
    writeInt(self.evasions, f)
    writeInt(self.jumpsSurvived, f)
    writeInt(self.skillMasteries, f)
    writeInt(self.stunTicks, f)
    writeInt(self.healthBoost, f)
    writeInt(self.clonebayPriority, f)
    writeInt(self.damageBoost, f)
    writeInt(self.unknown_alpha, f)
    writeInt(self.universalDeathCount, f)
    writeInt(self.pilotMasteryLvl1, f)
    writeInt(self.pilotMasteryLvl2, f)
    writeInt(self.engineMasteryLvl1, f)
    writeInt(self.engineMasteryLvl2, f)
    writeInt(self.shieldMasterLvl1, f)
    writeInt(self.shieldMasteryLvl2, f)
    writeInt(self.weaponMasteryLvl1, f)
    writeInt(self.weaponMasteryLvl2, f)
    writeInt(self.repairMasteryLvl1, f)
    writeInt(self.repairMasteryLvl2, f)
    writeInt(self.combatMasteryLvl1, f)
    writeInt(self.combatMasteryLvl2, f)
    writeBool(self.unknown_beta, f)
    self.teleportAnimation.write(f)
    writeBool(self.unknown_delta, f)
    if (self.race == "Crystal"):
      writeInt(self.lockdownRechargeTick, f)
      writeInt(self.lockdownRechargeTickGoal, f)
      writeInt(self.unknown_gamma, f)
