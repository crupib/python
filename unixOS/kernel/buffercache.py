import double_linklist
class buffer_head:
    def __init__(self, devnum, blocknum,status, dataarea):
       self.devnum = None
       self.blocknum  = None
       self.status = None
       self.dataarea = dataarea
       self.nexthash = None
       self.prevhash = None
       self.nextfree = None
       self.prevfree = None
       self.next = None 
       self.prev = None

