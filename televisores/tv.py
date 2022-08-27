class TV():
    numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control
        TV.numTV += 1
        
        
    def setMarca(self, marca):
        self._marca = marca
    
    def getMarca(self):
        return self._marca
    
    def setControl(self, control):
        self._control = control
        
    def getControl(self):
        return self._control
    
    def setPrecio(self, precio):
        self._precio = precio
        
    def getPrecio(self):
        return self._precio
        
    def setVolumen(self, volumen):
        self._volumen = volumen
    
    def getVolumen(self):
        return self._volumen
    
    def setCanal(self, canal):
        if self._estado == True and self._canal <= 120 and self._canal >= 0:
            self._canal = canal 
    
    def getCanal (self):
        return self._canal
        
    def setNumTv(self, num):
        TV.numTV = num
        
    def getNumTv(self):
        return TV.numTV
    
    def turnOn(self):
        self._estado = True
        
    def turnOff(self):
        self._estado = True
        
    def getEstado(self):
        return self._estado
    
    def volumenUp(self):
        if self._volumen < 7 and self._estado == True:
            self._volumen += 1
    
    def volumenDown(self):
        if self._volumen > 0 and self._estado == True:
            self._volumen -= 1
            
    def canalUp(self):
        if self._canal < 120 and self._estado == True:
            self._canal += 1
            
    def canalDown(self):
        if self._canal > 0 and self._estado == True:
            self._canal -= 1