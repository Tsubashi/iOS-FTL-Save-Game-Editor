from enum import IntEnum
from ship import Ship
from map import Sector
from crew import InitialCrewMember
from fileUtils import *

class GameDifficulty(IntEnum):
  Easy   = 0
  Normal = 1
  Hard   = 2

class GameState:
  id = ""
  value = 0
  
  def __init__(self,f):
    self.read(f)
  
  def read(self,f):
    self.id = getString(f)
    self.value = getInt(f)
  
  def write(self,f):
    writeString(self.id, f)
    writeInt(self.value, f)

class SaveFile:
  ## Header
  fileVersion = 0
  isAE = False
  difficulty = GameDifficulty.Easy
  shipsDefeated = 0
  beaconsExplored = 0
  scrapCollected = 0
  totalCrewHired = 0
  shipName = ""
  sectorNumber = 1 # 1-indexed
  unknown_beta = 0
  gameState = []
  shipBlueprintID = ""
  shipGFXBaseName = ""
  initialCrew = []
  ## Ship Data
  mainShip = 0
  sector = Sector()
  beacon = []
  quest = []
  distantQuest = []
  everythingElse = 0
  
  def __init__(self, file):
    with open(file, "rb") as f:
        # Header
        self.fileVersion = getInt(f)
        self.isAE = getBool(f)
        if not self.isAE:
          raise Exception("AE not detected")
        
        # Game Info
        self.difficulty = getInt(f)
        self.shipsDefeated = getInt(f)
        self.beaconsExplored = getInt(f)
        self.scrapCollected = getInt(f)
        self.totalCrewHired = getInt(f)
        self.shipName = getString(f)
        self.shipBlueprintID = getString(f)
        self.sectorNumber = getInt(f)
        self.unknown_beta = getInt(f)
        
        # Game State
        self.gameState = [GameState(f) for i in range(getInt(f))]
        
        # Ship Info
        if self.shipBlueprintID != getString(f):
          raise Exception("Ship Blueprint ID Mismatch") 
        if (self.shipName != getString(f)):
          raise Exception("Ship Name Mismatch")
        self.shipGFXBaseName = getString(f)
        self.initialCrew = [InitialCrewMember(f) for i in range(getInt(f))]
        self.mainShip = Ship(self.shipBlueprintID, f)
        self.mainShip.cargo = [getString(f) for i in range(getInt(f))]
        
        
        
        # Everything Else
        self.everythingElse = f.read()
        
  def write(self,file):
    with open(file, "wb") as f:
      # Header
        writeInt(self.fileVersion, f)
        writeBool(self.isAE, f)
        
        # Game Info
        writeInt(self.difficulty, f)
        writeInt(self.shipsDefeated, f)
        writeInt(self.beaconsExplored, f)
        writeInt(self.scrapCollected, f)
        writeInt(self.totalCrewHired, f)
        writeString(self.shipName, f)
        writeString(self.shipBlueprintID, f)
        writeInt(self.sectorNumber, f)
        writeInt(self.unknown_beta, f)
        
        # Game State
        writeInt(len(self.gameState), f)
        for state in self.gameState:
          state.write(f)
        
        # Ship Info
        writeString(self.shipBlueprintID, f)
        writeString(self.shipName, f)
        writeString(self.shipGFXBaseName, f)
        writeInt(len(self.initialCrew), f)
        for crew in self.initialCrew:
          crew.write(f)
        self.mainShip.write(f)   
        
        # Everything Else
        f.write(self.everythingElse)
      

