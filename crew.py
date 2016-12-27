from fileUtils import *

class InitalCrewMember:
  race = ""
  name = ""
  
  def read(f):
    self.race = getString(f)
    self.name = getString(f)
    
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
  deathOrder = 0
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
