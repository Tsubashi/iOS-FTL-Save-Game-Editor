from fileUtils import *
from pprintpp import pprint as pp

class SystemList:
  shields     = 0
  engines     = 0
  oxygen      = 0
  weapons     = 0
  drones      = 0
  medbay      = 0
  pilot       = 0
  sensors     = 0
  doors       = 0
  teleporter  = 0
  cloaking    = 0
  artillery   = 0
  battery     = 0
  clonebay    = 0
  mindControl = 0
  hacking     = 0
  
  def __init__(self,f):
    self.read(f)
    
  def read(self,f):
    self.shields = ShieldSystem(f)
    self.engines = ShipSystem("Engines",f)
    self.oxygen = ShipSystem("Oxygen",f)
    self.weapons = WeaponSystem(f)
    self.drones = DroneSystem(f)
    self.medbay = ShipSystem("Medbay",f)
    self.pilot = ShipSystem("Piloting",f)
    self.sensors = ShipSystem("Sensors",f)
    self.doors = ShipSystem("Doors",f)
    self.teleporter = ShipSystem("Engines",f)
    self.cloaking = CloakingSystem(f)
    self.artillery = ShipSystem("Artillery",f)
    self.battery = BatterySystem(f)
    self.clonebay = ClonebaySystem(f)
    self.mindControl = ShipSystem("MindControl",f)
    self.hacking = ShipSystem("Hacking",f)
  
  def write(self, f):
    self.shields.write(f)
    self.engines.write(f)
    self.oxygen.write(f)
    self.weapons.write(f)
    self.drones.write(f)
    self.medbay.write(f)
    self.pilot.write(f)
    self.sensors.write(f)
    self.doors.write(f)
    self.teleporter.write(f)
    self.cloaking.write(f)
    self.artillery.write(f)
    self.battery.write(f)
    self.clonebay.write(f)
    self.mindControl.write(f)
    self.hacking.write(f)
    
    
  def toString(self):
    pp(vars(self.shields))
    pp(vars(self.engines))
    pp(vars(self.oxygen))
    pp(vars(self.weapons))
    pp(vars(self.drones))
    pp(vars(self.medbay))
    pp(vars(self.pilot))
    pp(vars(self.sensors))
    pp(vars(self.doors))
    pp(vars(self.teleporter))
    pp(vars(self.cloaking))
    pp(vars(self.artillery))
    pp(vars(self.battery))
    pp(vars(self.clonebay))
    pp(vars(self.mindControl))
    pp(vars(self.hacking))
    
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
  hackLevel = 0
  tempCapacityCap = 0
  tempCapacityLoss = 0
  tempCapacityDivisor = 0
  
  def __init__(self,name,f):
    self.name = name
    self.read(f)
  
  def read(self,f):
    self.capacity = getInt(f)
    if self.capacity > 0:
      self.power = getInt(f)
      self.damage = getInt(f)
      self.ionized = getInt(f)
      self.deIonizationTicks = getInt(f)
      self.repairProgress = getInt(f)
      self.damageProgress = getInt(f)
      self.batteryPowerLevel = getInt(f)
      self.hackLevel = getInt(f)
      self.tempCapacityCap = getInt(f)
      self.tempCapacityLoss = f.read(8) # Something is screwy here. Why 8 bytes?
      self.tempCapacityDivisor = getInt(f)

  def write(self,f):
    writeInt(self.capacity, f)
    if self.capacity > 0:
      writeInt(self.power, f)
      writeInt(self.damage, f)
      writeInt(self.ionized, f)
      writeInt(self.deIonizationTicks, f)
      writeInt(self.repairProgress, f)
      writeInt(self.damageProgress, f)
      writeInt(self.batteryPowerLevel, f)
      writeInt(self.hackLevel, f)
      writeInt(self.tempCapacityCap, f)
      f.write(self.tempCapacityLoss)
      writeInt(self.tempCapacityDivisor, f)

class ClonebaySystem(ShipSystem):
  regenTicks = 0
  regenTicksGoal = 0
  doomTicks = 0
  
  def __init__(self,f):
    self.name = "Clonebay"
    super().read(f)
  
  def readExtended(self,f):
    if self.capacity > 0:
      self.regenTicks = getInt(f)
      self.regenTicksGoal = getInt(f)
      self.doomTicks = getInt(f)
  
  def writeExtended(self,f):
    if self.capacity > 0:
      writeInt(self.regenTicks, f)
      writeInt(self.regenTicksGoal, f)
      writeInt(self.doomTicks, f)
    

class BatterySystem(ShipSystem):
  active = False
  used = 0
  dischargeTicks = 0
  
  def __init__(self,f):
    self.name = "Battery"
    super().read(f)
  
  def readExtended(self,f):
    if self.capacity > 0:
      self.active = getBool(f)
      self.used = getInt(f)
      self.dischargeTicks = getInt(f)
      
  def writeExtended(self,f):
    if self.capacity > 0:
      writeInt(self.active, f)
      writeInt(self.used, f)
      writeInt(self.dischargeTicks, f)


class ShieldSystem(ShipSystem):
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
  downX = 0
  downY = 0
  
  def __init__(self,f):
    self.name = "Shields"
    super().read(f)
  
  def readExtended(self,f):
    self.layers = getInt(f)
    self.energyLayers = getInt(f)
    self.energyLayersMax = getInt(f)
    self.rechargeTicks = getInt(f)
    self.isAnimatingDrop = getBool(f)
    self.dropAnimationTicks = getInt(f)
    self.isAnimatingRaise = getBool(f)
    self.raiseAnimationTicks = getInt(f)
    self.isAnimatingEnergyShield = getBool(f)
    self.energyShieldAnimationTicks = getInt(f)
    self.downX = getInt(f)
    self.downY = getInt(f)

  def writeExtended(self,f):
    writeInt(self.layers, f)
    writeInt(self.energyLayers, f)
    writeInt(self.energyLayersMax, f)
    writeInt(self.rechargeTicks, f)
    writeInt(self.isAnimatingDrop, f)
    writeInt(self.dropAnimationTicks, f)
    writeInt(self.isAnimatingRaise, f)
    writeInt(self.raiseAnimationTicks, f)
    writeInt(self.isAnimatingEnergyShield, f)
    writeInt(self.energyShieldAnimationTicks, f)
    writeInt(self.downX, f)
    writeInt(self.downY, f)

class CloakingSystem(ShipSystem):
  unknown_alpha = 0
  unknown_beta = 0
  cloakTicksGoal = 0
  cloakTicks = 0
  cloakAnimationTicks = 0
  
  def __init__(self,f):
    self.name = "Cloaking"
    super().read(f)
  
  def readExtended(self,f):
    if self.capacity > 0:
      self.unknown_alpha = getInt(f)
      self.unknown_beta = getInt(f)
      self.cloakTicksGoal = getInt(f)
      self.cloakTicks = getInt(f)
  
  def writeExtended(self,f):
    if self.capacity > 0:
      writeInt(self.unknown_alpha, f)
      writeInt(self.unknown_beta, f)
      writeInt(self.cloakTicksGoal, f)
      writeInt(self.cloakTicks, f)
    
class WeaponSystem(ShipSystem):
  def __init__(self,f):
    self.name = "Weapons"
    super().read(f)
  
  def readExtended(self,f):
    raise Warning("Derp")

   
class DroneSystem(ShipSystem): 
  def __init__(self,f):
    self.name = "Drones"
    super().read(f)
  
  def readExtended(self,f):
    raise Warning("Derp")
