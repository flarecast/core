class Message():
  id = 0
  def __init__(self, addr, kind):
    self.addr = addr
    self.kind = kind
    self.id = self.id++


  def compose():
    return (self.id+'-'+self.addr+' '+self.kind)