class train:


  def _init_(self,engineSizeInput,bodyColorInput,windowNumberInput,seatNumberInput,isBulletTrain):
    self.engineSize=engineSizeInput
    self.bodyColor=bodyColorInput
    self.windowNumber=windowNumberInput
    self.seatNumber=seatNumberInput
    self.BulletTrain=isBulletTrain


#Drive Method
  def drive(self):
    print("We're heading to New York City!!")

  def speedup(self):
    print("WOOOOOOOOOOOOOOOOOOOOOO")

  def crash(self):
    print("BAAAAAMMMMMGGGG")

  def slowingdown(self):
    print("We're slwoing down!")


TakumaTrain=train(200,"black",50,50,True)

TakumaTrain.drive()
TakumaTrain.speedup()
TakumaTrain.crash()
TakumaTrain.slowingdown()
 
