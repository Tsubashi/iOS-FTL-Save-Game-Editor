from fileUtils import *

class Animation:
  isPlaying = False
  isLooping = False
  currentFrame = 0
  progressTicks = 0
  scale = 0
  x = 0
  y = 0
  
  def __init__(self, *args, **kwargs):
    if len(args) > 1:
      raise Warning("Extra positional arguments ignored")
    if len(args) > 0:
      self.read(args[0])
    self.__dict__.update(kwargs)

  def read(self,f):
    self.isPlaying = getBool(f)
    self.isLooping = getBool(f)
    self.currentFrame = getInt(f)
    self.progressTicks = getInt(f)
    self.scale = getInt(f)
    self.x = getInt(f)
    self.y = getInt(f)

  def write(self,f):
    writeBool(self.isPlaying, f)
    writeBool(self.isLooping, f)
    writeInt(self.currentFrame, f)
    writeInt(self.progressTicks, f)
    writeInt(self.scale, f)
    writeInt(self.x, f)
    writeInt(self.y, f)
