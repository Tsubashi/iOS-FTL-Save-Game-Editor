def getInt(f):
  return int.from_bytes(f.read(4), byteorder='little')
  
def writeInt(data,f):
  f.write(data.to_bytes(4, byteorder='little'))

def getBool(f):
  return bool(int.from_bytes(f.read(4), byteorder='little'))
  
def writeBool(data,f):
  f.write(data.to_bytes(4, byteorder='little'))
  
def getString(f):
  size = getInt(f)
  return f.read(size).decode()

def writeString(data, f):
  writeInt(len(data), f)
  f.write(data.encode())
