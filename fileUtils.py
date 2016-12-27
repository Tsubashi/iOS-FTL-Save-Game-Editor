def getInt(f):
  return int.from_bytes(f.read(4), byteorder='little')

def getDouble(f):
  return 0

def getBool(f):
  return bool(int.from_bytes(f.read(4), byteorder='little'))
  
def getString(f):
  size = getInt(f)
  return str(f.read(size))
