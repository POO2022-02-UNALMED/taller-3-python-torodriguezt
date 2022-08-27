class TV:
  __numTV = 0
  def __init__(self, marca, estado):
    self.__marca = marca
    self.__canal = 1
    self.__precio = 500
    self.__estado = estado
    self.__volumen = 1
    self.__control = None
    TV.__numTV += 1

  def setMarca(self, marca):
    self.__marca = marca

  def getMarca(self):
    return self.__marca

  def setControl(self, control):
    self.__control = control

  def getControl(self):
    return self.__control

  def setPrecio(self, precio):
    self.__precio = precio

  def getPrecio(self):
    return self.__precio

  def setVolumen(self, volumen):
    self.__volumen = volumen

  def getVolumen(self):
    return self.__volumen

  def setCanal(self, canal):
    self.__canal = canal
    
  def getCanal(self):
    return self.__canal

  def turnOn(self):
    self.__estado = True

  def turnOff(self):
    self.__estado = False

  def getEstado(self):
    return self.__estado

  def canalUp(self):
    if self.__canal < 120 and self.__estado == True :
      self.__canal += 1

  def canalDown(self):
    if self.__canal > 1 and self.__estado == True :
      self.__canal -= 1

  def volumenUp(self):
    if self.__volumen < 7 and self.__estado == True:
      self.__volumen += 1

  def volumenDown(self):
    if self.__volumen > 0 and self.__estado == True:
      self.__volumen -= 1

  def setNumTV(self, numero):
    __numTV = numero

  def getNumeroTV(self):
    return TV.__numTV  
