#for stars
import random
import java.awt.Font as Font

def main():

  #see if the image location can be found
  try:
    showInformation("Find the folder Image in this project file")
    setMediaPath()
    health = makePicture("Health_Powerup.png")
    energy = makePicture("Energy_Powerup.png")
    potion = makePicture("Potion_Powerup.png")
    light = makePicture("Light_Powerup.png")
  #if fails request user to locate folder with images
  except StandardError:
    showError("Image location could not be found, please locate the folder")
    setMediaPath()
 
 #request user to choose powerup
  powerup = requestIntegerInRange("Choose a powerup: health [1], energy [2], potion [3] or light[4]", 1, 4)
  if powerup == 1:
    powerupChoice = health
    powerupName = "Health"
    powerupText = "Healing"
  elif powerup == 2:
    powerupChoice = energy
    powerupName = "Energy"
    powerupText = "Charging"
  elif powerup == 3:
    powerupChoice = potion
    powerupName = "Potion"
    powerupText = "Replenish"
  else:
    powerupChoice = light
    powerupName = "Light"
    powerupText = "Super"
  #getting the picture height helps alignment
  pic = powerupChoice
  picHeight=getHeight(pic)
  picWidth=getWidth(pic)
  star = makePicture("Star.png")
  glow = makePicture("Glow.png")
  
  #text format
  text = powerupText
  myFont = makeStyle("Comic Sans", Font.BOLD, 40)
  xpos = picWidth/4
  ypos = picHeight-40

  #set the canvas height and width, black
  canvasHeight=picHeight+40
  canvasWidth=picWidth+40
  canvas=makeEmptyPicture(canvasWidth, canvasHeight, black)
 
  show(canvas) 
  
  #make pic centered
  targetX=(canvasHeight-picHeight)/2
  targetY=targetX

  #make image move up then down
  loopNumber = 4
  for loop in range (0, loopNumber):
    #number of pixels move
    maxHeight=4

    #move image up
    for up in range (0,maxHeight):
      setAllPixelsToAColor(canvas, black)    
      copyInto(pic, canvas, targetX, targetY-up)
      addText(canvas, canvasWidth/4, 14, "This is the " + powerupName + " powerup", white)   
      
      #random stars
      for i in range(0,4):
        starX = random.randint(0, picWidth)
        starY = random.randint(0, picHeight)
        copyInto(star, canvas, starX, starY) 
      
      #text
      color = makeColor((random.randint(0,255)), (random.randint(0,255)), (random.randint(0,255)))
      addTextWithStyle(canvas, xpos, ypos, text, myFont, color)
                
      repaint(canvas)
      
      #make image lighter
      for px in getPixels(pic):     
        r1=getRed(px)*1.05
        g1=getGreen(px)*1.05
        b1=getBlue(px)*1.05

        newColor=makeColor(r1,g1,b1)
        setColor(px,newColor)   
               
    #move image down
    for down in range (0,maxHeight):
      setAllPixelsToAColor(canvas, black)
      addText(canvas, canvasWidth/4, 14, "This is the " + powerupName + " powerup", white) 
      copyInto(pic, canvas, targetX, targetY-maxHeight+down)
      
      #random stars
      for i in range(0,4):
        starX = random.randint(0, picWidth)
        starY = random.randint(0, picHeight)
        copyInto(star, canvas, starX, starY)
        
      #text
      color = makeColor((random.randint(0,255)), (random.randint(0,255)), (random.randint(0,255)))
      addTextWithStyle(canvas, picWidth/4, picHeight-40, text, myFont, color)
      
      repaint(canvas)

      #make image darker
      for px in getPixels(pic):
        r1=getRed(px)*0.95
        g1=getGreen(px)*0.95
        b1=getBlue(px)*0.95
        newColor=makeColor(r1,g1,b1)
        setColor(px,newColor)
        
  repeat = requestString("Do you want to return to selection? y/n")
  if repeat == "y":
    main()
  else:
    showInformation("Please exit the program")
    setAllPixelsToAColor(canvas, black) 
    text = "Thank you for using this program"
    myFont = makeStyle("Comic Sans", Font.BOLD, 14)
    xpos = 14
    ypos = picHeight/2
    addTextWithStyle(canvas, xpos, ypos, text, myFont, white)
    repaint(canvas)