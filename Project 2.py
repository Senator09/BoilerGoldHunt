# CS 177-Project2.py
# Alhagie K Jaiteh
# Program name : The Gold Hunt Game
# Program Discription: This program is a game that prompt user to enter player name, it will then take user to the Gold hunt window
#                       where a hidden and random gold colored circle is assigned and once you are able to locate that, the player
#                       will earn points base on the number of clicks it took the player to locate the gold circle.
#                       After five rounds, the games will reset until a new player enters the game and all player names and scores will
#                       be saved in a txt file call score.

from graphics import *
from random import *
from math import sqrt




# PART 1: THE GAME CONTROL PANEL
def Data_Entry():
      # I design my Game Control pannel
      win=GraphWin("Game Control",250,200)
      win.setBackground("light grey")

      # I make a Boiler Gold Hunt! and Player name  heading
      head=Rectangle(Point(0,30),Point(250,0)).draw(win)
      head.setFill("black")
      headline=Text(Point(125,15)," BOILER GOLD HUNT!").draw(win)
      headline.setFill("Yellow")

      Player_Name= Text(Point(125,50),"PLAYER NAME").draw(win)
      Player_Name.setStyle("bold")

      # Under this code I design the Player Name entry Point , New Game and Exit Point
      Enter_Name=Entry(Point(125,90),13).draw(win)
      Enter_Name.setFill("white")

      New_Game=Rectangle(Point(4,115), Point(115,196))
      New_Game.draw(win)
      New_Game.setFill("Gold")

      text=Text(Point(55,155),"NEW GAME").draw(win)
      text.setStyle("bold")

      # Here i design my Exit botton

      Exit=Rectangle(Point(180,115), Point(246,196)).draw(win)
      Exit.setFill("Black")
      
      Exit_Text=Text(Point(213,155),"EXIT").draw(win)
      Exit_Text.setFill("White")
      Exit_Text .setStyle("bold")

      return(Enter_Name, New_Game, Exit, win)

# PART 2: THE BOILER GOLD HUNT WINDOW

def Play_Ground():
      # Here i start by designing my hunt graphic window and all the lebels on it.
      Gold_Hunt=GraphWin("GoldHunt",480,520, autoflush=False)
      Black_Rectangle= Rectangle(Point(0,0),Point(480,40)).draw(Gold_Hunt)
      Black_Rectangle.setFill("Black")

      Round=Text(Point(50,20),"Round: ").draw(Gold_Hunt)
      Round.setFill("yellow")
      

      Clicks=Text(Point(410,20),"Clicks: ").draw(Gold_Hunt)
      Clicks.setFill("yellow")

      return(Round, Clicks, Gold_Hunt)

      # The Round,palyer and Click functions are the all done as seperate funtions, so
      # I can call them in my enable game function

def Round(Gold_Hunt,Round_Number):
      Rounds_Box=Text(Point(80,20), str(Round_Number))
      Rounds_Box.draw(Gold_Hunt)
      Rounds_Box.setFill("yellow")
      Rounds_Box.setStyle("bold")

      return Rounds_Box
      
def player(Gold_Hunt,Player_Name):
      Player_Box=Text(Point(240,20),"Player: " + Player_Name)
      Player_Box.draw(Gold_Hunt)
      Player_Box.setFill("yellow")
      Player_Box.setStyle("bold")

      return Player_Box

def Click(Gold_Hunt,Click_Number):
      Click_Box=Text(Point(445,20), str(Click_Number))
      Click_Box.draw(Gold_Hunt)
      Click_Box.setStyle("bold")
      Click_Box.setFill("yellow")
 
      return Click_Box
      

      # Here fomulate the pythagorian theory as a function of its own for i can have to
      # keep writing it over and over agin in my distance calculation

def distance(point,circle):
      x=abs(point.getX()-circle.getX())
      y=abs(point.getY()-circle.getY())

      return abs(sqrt(x**2 + y**2))



      # Under the circle funtion, I design my black circles and put them in list call
      # blacklist, I assign my colors using boolean logic and cann in my distance function.
      
def Make_Circle(Gold_Hunt):
      # To have 15 circles fill black rows and columns, i put it in a nested for loop.
      blacklist=[]
      for row in range (0,15):
          for column in range (1,16):
                  Black_Cir=Circle(Point(27.5+(30*row),42+(30*column)),15).draw(Gold_Hunt)
                  Black_Cir.setFill("black")
                  blacklist.append(Black_Cir)

      # Color variable is a random variable 0-224, i copied all list of colors and paste it in fillColor
  
      Gold_Color=randint(0,224)
      fillColors = blacklist.copy()
      fillColors[Gold_Color] = "gold"
      goldencoin=blacklist[Gold_Color].getCenter()

      for i in (blacklist):
            
            if fillColors[blacklist.index(i)] !="gold":

                  circlePoint=i.getCenter()

                  if distance(circlePoint, goldencoin)==30 or distance(circlePoint,goldencoin)==sqrt(1800):
                        fillColors[blacklist.index(i)]="tan"

                  elif distance(circlePoint, goldencoin) in [60, sqrt(4500), sqrt(7200)]:
                         fillColors[blacklist.index(i)]="grey"

                  else:
                         fillColors[blacklist.index(i)]="white"

      
      return blacklist,fillColors,Gold_Color
   
      
      # The Mother_Circle funtion is a tool that allows me to get the closest circle to my
      # my mouse click at any point on the Gold_Hunt window

def Mother_Circle(number,list_number):
      return min(list_number,key=lambda x: abs(x-number))
      

      # The Enable game function is where I design how the game will be played,
      # assign all my mouse clicks on the on the gold hunt window

def enable_game(Gold_Hunt,win,Player_Box,Player_Name):
      # At the begining of the game, Round number and click number are 1 and 0 repectively.
      Round_Number=1
      Click_Number=0
      
      # The use of global allows me call in any local variable that belongs outside the
      # enable funtion into the enable function.

      global circle,blacklist,Gold_Color
      blacklist,fillColors,Gold_Color=Make_Circle(Gold_Hunt)
      All_X_Centers=[]
      All_Y_Centers=[]

      # I put all the center of both X and Y coodinate values and assign them to the list.

      for circle in blacklist:
            All_X_Centers.append(circle.getCenter().getX())
      for circle in blacklist:
            All_Y_Centers.append(circle.getCenter().getY())
      # ere I call in my round and clcik funtion.
      Round_Box=Round(Gold_Hunt,Round_Number)
      Click_Box=Click(Gold_Hunt,Click_Number)
            
      Game_board=Gold_Hunt.getMouse()
     
      while True:
          
            # Undraw number of clicks from 0 to whatever number of clicks it took the player took the player to win.
            Click_Box.undraw()
            Click_Number+=1
            Click_Box=Click(Gold_Hunt,Click_Number)

            Circle_Closer_X=Mother_Circle(Game_board.getX(),All_X_Centers)
            Circle_Closer_Y=Mother_Circle(Game_board.getY(),All_Y_Centers)
           

            for x in range(0,len(blacklist),1):
                  if (Circle_Closer_X==blacklist[x].getCenter().getX()) and (Circle_Closer_Y==blacklist[x].getCenter().getY()):
                        blacklist[x].setFill(fillColors[x])
                  # After the Gold coler is found the text BOILER UP AND CLICK TO CONTINUE  will appear
            if (Circle_Closer_X)==blacklist[Gold_Color].getCenter().getX() and (Circle_Closer_Y)== blacklist[Gold_Color].getCenter().getY():
                  Animate_Circle(blacklist,Gold_Color)
                  blacklist[Gold_Color].undraw()
                  Victory_Text=Text(Point(240,250),"Good job PFC Winn!").draw(Gold_Hunt)
                  Victory_Text.setStyle("bold")
                  Victory_Text.setSize(18)
                  print("      ")

                  Continue_Line= Text(Point(240,270),"CLICK TO CONTINUE..").draw(Gold_Hunt)

                  # After the click to continue, everything on the Gold_Hunt win will undraw

                  Gold_Hunt.getMouse()
                  Victory_Text.undraw()
                  Continue_Line.undraw()
                  
                  # And a player enters the game, everything appears on the screen
                
                  blacklist,fillColors,Gold_Color=Make_Circle(Gold_Hunt)

                  Round_Box.undraw()
                  Round_Number+=1
                  Round_Box=Round(Gold_Hunt,Round_Number)
                  # If Round number is beyong 5 rounds, it will reset to a new player.
                  if Round_Number>5:
                        Click_Box.undraw()
                        Round_Box.undraw()
                        Player_Box.undraw()

                  # All palyer names and thier correspoding scores will be saved ina file score

                        Score_File=open("score.txt","w")
                        Score_File.write(Player_Name+" "+str(Click_Number) +"\n")
                        Score_File.close()

                        Round_Number=0
                        Click_Number=0

                        for elements in blacklist:
                              elements.undraw()
                  

                        break


           # To EXIT the game at anytime, while is detected and it is on the EXIT botton,
           #  close the win
            panelClick = win.checkMouse()
            while True:
                  if (panelClick!= None) and ((panelClick.getX()>=180 and panelClick.getX()<=246) and (panelClick.getY()>=115 and panelClick.getY()<=196)):
                        win.close()
                        Gold_Hunt.close()
                  else:
                        # the condition is just reassigning the clicks so you can be able to click somehwere else
                        panelClick = win.checkMouse()
                        Game_board=Gold_Hunt.checkMouse()
                  if (Game_board!=None):
                        break 
                        

            
      ## Thi                    
      # PART 4: The Main Function.
      # Here is where I call in every function to the program in the other in which
      # they impacted the program

def Animate_Circle(blacklist,Gold_Color):
      for element in range(0,100,1):
            for elements in range(0,225,1):
                  if elements==Gold_Color:
                        blacklist[elements].move(0,0)
                  else:
                        blacklist[elements].move(0,480/100)
            update(30)
      
      
def main():
      # I call in my two main windows in the main()

      Player_Name, New_Game, Exit, win=Data_Entry()
      Round, Clicks, Gold_Hunt=Play_Ground()

      control=win.getMouse()
      xValue=control.getX()
      yValue=control.getY()

      while True:
            # if the player name entry is not an empty string and a click is made on the new game botton
            # start game
            if ((Player_Name.getText() !='') and (xValue>=4 and xValue<=115) and (yValue>=115 and yValue<=196)):
                  Player_Box=player(Gold_Hunt,Player_Name.getText())
                  enable_game(Gold_Hunt,win,Player_Box,Player_Name.getText())

            # if the Exit botton is clicked, close win, close gold hunt win       

            if ((xValue>=180 and xValue<=246) and (yValue>=115 and yValue<=196)):
                  win.close()
                  Gold_Hunt.close()
                  break

            control=win.getMouse()
            xValue=control.getX()
            yValue=control.getY()

main()

