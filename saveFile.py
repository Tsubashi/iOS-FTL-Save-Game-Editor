from enum import IntEnum
from ship import MainShip
from map import Sector
from fileUtils import *
from crew import *

class GameDifficulty(IntEnum):
  Easy   = 0
  Normal = 1
  Hard   = 2

class SaveFile:
  ## Header
  fileVersion = 0
  isAE = False
  difficulty = GameDifficulty.Easy
  unknown_alpha = 0
  beaconsExplored = 0
  scrapCollected = 0
  totalCrewHired = 0
  shipName = ""
  shipCode = ""
  sectorNumber = 1 # 1-indexed
  unknown_beta = 0
  unknown_gamma = 0
  beaconType = ""
  shipName2 = ""
  shipGFXBaseName = ""
  initalCrew = []
  ## Ship Data
  ship = MainShip()
  cash = 0
  crew = []
  sector = Sector()
  beacon = []
  quest = []
  distantQuest = []
  everythingElse = 0
  
  def __init__(self, file):
    with open(file, "rb") as f:
        self.fileVersion = getInt(f)
        self.isAE = getBool(f)
        self.difficulty = getInt(f)
        self.unknown_alpha = getInt(f)
        self.beaconsExplored = getInt(f)
        self.scrapCollected = getInt(f)
        self.totalCrewHired = getInt(f)
        self.shipName = getString(f)
        self.shipCode = getString(f)
        self.sectorNumber = getInt(f)
        self.unknown_beta = getInt(f)
        self.unknown_gamma = getInt(f)
        self.beaconType = getString(f)
        self.shipName2 = getString(f)
        if (self.shipName != self.shipName2):
          raise Exception("Ship Name Mismatch")
        self.shipGFXBaseName = getString(f)
        initalCrewCount = getInt(f)
        for i in initalCrewCount:
          self.initalCrew[i] = InitialCrewMember()
          initalCrew[i].read(f)
        self.ship = Ship()
        ship.read(f)
        
  def toString(self):
    return self.ship.unknown_alpha
