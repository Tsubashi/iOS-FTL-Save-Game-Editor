from enum import IntEnum

class SystemName(IntEnum):
  Shields     = 0
  Engines     = 1
  Oxygen      = 2
  Weapons     = 3
  Drones      = 4
  Medbay      = 5
  Pilot       = 6
  Sensors     = 7
  Doors       = 8
  Teleporter  = 9
  Cloaking    = 10
  Artillery   = 11
  Battery     = 12
  Clonebay    = 13
  MindControl = 14
  Hacking     = 15
    
class ShipSystem:
  name = ""
  capacity = 0
  power = 0
  damage = 0
  ionized = 0
  deIonizationTicks = 0
  repairProgress = 0
  damageProgress = 0
  batteryPowerLevel = 0

class ClonebayInfo:
  regenTicks = 0
  regenTicksGoal = 0
  doomTicks = 0

class BatteryInfo:
  active = False
  used = 0
  dischargeTicks = 0

class ShieldInfo:
  layers = 0
  energyLayers = 0
  energyLayersMax = 0
  rechargeTicks = 0
  isAnimatingDrop = False
  dropAnimationTicks = 0
  isAnimatingRaise = False
  raiseAnimationTicks = 0
  isAnimatingEnergyShield = False
  energyShieldAnimationTicks = 0
  unknown_alpha = 0
  unknown_beta = 0

class CloakingInfo:
  unknown_alpha = 0
  unknown_beta = 0
  cloakTicksGoal = 0
  cloakTicks = 0
  cloakAnimationTicks = 0
