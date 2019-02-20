#!/usr/bin/python
# GUI requests-html module :
#   Use request infomatin from html web 
# https://html.python-requests.org/

# from random import *  # Gọi hàm random số tự nhiên trong 1 khoảng nào đó : randint(1,5)
# # from random import choice   # Gọi hàm random giá trị trong mảng
# import turtle         # Gọi thư viện dùng cho Project 3
# import pygal

# import json
# import urllib.request
# import time



####################################################################################################
# Project 12 : Call HTML from Python
####################################################################################################
#______________________________________________Library_____________________________________________#
from lxml import html
import requests
#____________________________________________END_Library___________________________________________#
#____________________________________________CODE_DRIVER___________________________________________#
def P12_call_html():
    page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
    tree = html.fromstring(page.content)
    print(tree.text)
# print(help(requests))
#__________________________________________END_CODE_DRIVER_________________________________________#
####################################################################################################
# Project 11 : Craft
####################################################################################################
#______________________________________________Library_____________________________________________#
import turtle
import random
from variables import *
from math import ceil
#____________________________________________END_Library___________________________________________#
#____________________________________________CODE_SUPPORT__________________________________________#
#############
# CodeCraft #
#############

#---
#Game functions
#---

#moves the player left 1 tile.
def moveLeft():
  global playerX
  if(playerX > 0):
    playerX -= 1
    drawPlayer()

#moves the player right 1 tile.
def moveRight():
  global playerX, MAPWIDTH
  if(playerX < MAPWIDTH - 1):
    playerX += 1
    drawPlayer()

#moves the player up 1 tile.
def moveUp():
  global playerY
  if(playerY > 0):
    playerY -= 1
    drawPlayer()

#moves the player down 1 tile.
def moveDown():
  global playerY, MAPHEIGHT
  if(playerY < MAPHEIGHT - 1):
    playerY += 1
    drawPlayer()

#picks up the resource at the player's position.
def pickUp():
  global playerX, playerY
  drawing = True
  currentTile = world[playerX][playerY]
  #if the user doesn't already have too many...
  if inventory[currentTile] < MAXTILES:
    #player now has 1 more of this resource
    inventory[currentTile] += 1
    #the player is now standing on dirt
    world[playerX][playerY] = DIRT
    #draw the new DIRT tile
    drawResource(playerX, playerY)
    #redraw the inventory with the extra resource.
    drawInventory()

#place a resource at the player's current position
def place(resource):
  print('placing: ', names[resource])
  #only place if the player has some left...
  if inventory[resource] > 0:
    #find out the resourcee at the player's current position
    currentTile = world[playerX][playerY]
    #pick up the resource the player's standing on
    #(if it's not DIRT)
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    #place the resource at the player's current position
    world[playerX][playerY] = resource
    #add the new resource to the inventory
    inventory[resource] -= 1
    #update the display (world and inventory)
    drawResource(playerX, playerY)
    drawInventory()
    print('   Placing', names[resource], 'complete')
  #...and if they have none left...
  else:
    print('   You have no', names[resource], 'left')

#craft a new resource
def craft(resource):
  print('Crafting: ', names[resource])
  #if the resource can be crafted...
  if resource in crafting:
    #keeps track of whether we have the resources
    #to craft this item
    canBeMade = True
    #for each item needed to craft the resource
    for i in crafting[resource]:
      #...if we don't have enough...
      if crafting[resource][i] > inventory[i]:
      #...we can't craft it!
        canBeMade = False
        break
    #if we can craft it (we have all needed resources)
    if canBeMade == True:
      #take each item from the inventory
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      #add the crafted item to the inventory
      inventory[resource] += 1
      print('   Crafting', names[resource], 'complete')
    #...otherwise the resource can't be crafted...
    else:
      print('   Can\'t craft', names[resource])
    #update the displayed inventory
    drawInventory()

#creates a function for placing each resource
def makeplace(resource):
    return lambda: place(resource)

#attaches a 'placing' function to each key press
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

#creates a function for crafting each resource
def makecraft(resource):
  return lambda: craft(resource)

#attaches a 'crafting' function to each key press
def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

#draws a resource at the position (y,x)
def drawResource(y, x):
  #this variable stops other stuff being drawn
  global drawing
  #only draw if nothing else is being drawn
  if drawing == False:
    #something is now being drawn
    drawing = True
    #draw the resource at that position in the tilemap, using the correct image
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    #draw tile with correct texture
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    screen.update()
    #nothing is now being drawn
    drawing = False

#draws the player on the world
def drawPlayer():
    playerT.goto( (playerX * TILESIZE) + 20, height - (playerY * TILESIZE) -20 )

#draws the world map
def drawWorld():
  #loop through each row
  for row in range(MAPHEIGHT):
    #loop through each column in the row
    for column in range(MAPWIDTH):
      #draw the tile at the current position
      drawResource(column, row)

#draws the inventory to the screen
def drawInventory():
  #this variable stops other stuff being drawn
  global drawing
  #only draw if nothing else is being drawn
  if drawing == False:
    #something is now being drawn
    drawing = True
    #use a rectangle to cover the current inventory
    rendererT.color(BACKGROUNDCOLOUR)
    rendererT.goto(0,0)
    rendererT.begin_fill()
    #rendererT.setheading(0)
    for i in range(2):
      rendererT.forward(inventory_height - 60)
      rendererT.right(90)
      rendererT.forward(width)
      rendererT.right(90)
    rendererT.end_fill()
    rendererT.color('')
    #display the 'place' and 'craft' text
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("place")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("craft")
    #set the inventory position
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 80
    itemNum = 0
    for i, item in enumerate(resources):
      #add the image
      rendererT.goto(xPosition, yPostition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      #add the number in the inventory
      rendererT.goto(xPosition, yPostition - TILESIZE)
      rendererT.write(inventory[item])
      #add key to place
      rendererT.goto(xPosition, yPostition - TILESIZE - 20)
      rendererT.write(placekeys[item])
      #add key to craft
      if crafting.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 40)
        rendererT.write(craftkeys[item])     
      #move along to place the next inventory item
      xPosition += 50
      itemNum += 1
      #drop down to the next row every 10 items
      if itemNum % INVWIDTH == 0:
        xPosition = 70
        itemNum = 0
        yPostition -= TILESIZE + 80
    drawing = False

#generate the instructions, including crafting rules
def generateInstructions():
  instructions.append('Crafting rules:')
  #for each resource that can be crafted...
  for rule in crafting:
    #create the crafting rule text
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    #add the crafting rule to the instructions
    instructions.append(craftrule)
  #display the instructions
  yPos = height - 20
  for item in instructions:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, yPos)
    rendererT.write(item)
    yPos-=20

#generate a random world
def generateRandomWorld():
  #loop through each row
  for row in range(MAPHEIGHT):
    #loop through each column in that row
    for column in range(MAPWIDTH):
      #pick a random number between 0 and 10
      randomNumber = random.randint(0,10)
      #WATER if the random number is a 1 or a 2
      if randomNumber in [1,2]:
        tile = WATER
      #GRASS if the random number is a 3 or a 4
      elif randomNumber in [3,4]:
        tile = GRASS
      #otherwise it's DIRT
      else:
        tile = DIRT
      #set the position in the tilemap to the randomly chosen tile
      world[column][row] = tile
#__________________________________________END_CODE_SUPPORT________________________________________#
#---
#Code starts running here
#---
#____________________________________________CODE_DRIVER___________________________________________#
def P11_Craft():
    TILESIZE = 20
    #the number of inventory resources per row
    INVWIDTH = 8
    drawing = False

    #create a new 'screen' object
    screen = turtle.Screen()
    #calculate the width and height
    width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
    num_rows = int(ceil((len(resources) / INVWIDTH)))
    inventory_height =  num_rows * 120 + 40
    height = (TILESIZE * MAPHEIGHT) + inventory_height

    screen.setup(width, height)
    screen.setworldcoordinates(0,0,width,height)
    screen.bgcolor(BACKGROUNDCOLOUR)
    screen.listen()

    #register the player image  
    screen.register_shape(playerImg)
    #register each of the resource images
    for texture in textures.values():
      screen.register_shape(texture)
      
    #create a new player object
    playerT = turtle.Turtle()
    playerT.hideturtle()
    playerT.shape(playerImg)
    playerT.penup()
    playerT.speed(0)

    #create another turtle to do the graphics drawing
    rendererT = turtle.Turtle()
    rendererT.hideturtle()
    rendererT.penup()
    rendererT.speed(0)
    rendererT.setheading(90)

    #create a world of random resources.
    world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

    #map the keys for moving and picking up to the correct functions.
    screen.onkey(moveUp, 'w')
    screen.onkey(moveDown, 's')
    screen.onkey(moveLeft, 'a')
    screen.onkey(moveRight, 'd')
    screen.onkey(pickUp, 'space')

    #set up the keys for placing and crafting each resource
    bindPlacingKeys()
    bindCraftingKeys()

    #these functions are defined above
    generateRandomWorld()
    drawWorld()
    drawInventory()
    generateInstructions()
    drawPlayer()
    playerT.showturtle()
#__________________________________________END_CODE_DRIVER_________________________________________#


####################################################################################################
# Project 10 : Where is the space Station
####################################################################################################
#____________________________________________CODE_DRIVER___________________________________________#
def P10_where_is_space():
    url = 'http://api.open-notify.org/astros.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    print(result)
    print('People in Space:',result['number'])
    people=result['people']
    for p in people:
        print(p['name']," in ",p['craft'])

    url_location = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url_location)
    result = json.loads(response.read())
    print(result)
    location = result['iss_position']
    lat = location['latitude']
    lon = location['longitude']
    print("Latitude: ",lat)
    print("Longitude:",lon)
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.jpg')

    screen.register_shape('iss.png')
    iss = turtle.Turtle()
    iss.shape('iss.png')
    iss.setheading(90)
    iss.penup()
    iss.goto(lon,lat)

    # Space center Houston
    lat = 29.5502
    lon = -95.097

    location = turtle.Turtle()
    location.penup()
    location.shape('turtle')
    location.dot(10)
    location.color('yellow')
    location.goto(lon,lat)
    location.hideturtle()

    url = 'http://api.open-notify.org/iss-pass.json'
    url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    over = result['response'][1]['risetime']
    print(over)
    print(result)
    stype = ('Arial',6,'bold')
    location.write(time.ctime(over),font=stype)
#__________________________________________END_CODE_DRIVER_________________________________________#
####################################################################################################
# Project 9 : design and code your own RPG maze game
####################################################################################################
#____________________________________________CODE_SUPPORT__________________________________________#
# Replace RPG starter project with this code when new instructions are live
def showInstructions():
  #print a main menu and the commands
    print('''
    RPG Game
    ______==
    Commands:
      go [direction]
      get [item]
    ''')
def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
        print("---------------------------")
#__________________________________________END_CODE_SUPPORT________________________________________#
#____________________________________________CODE_DRIVER___________________________________________#
def P9_game_escape():

    #an inventory, which is initially empty
    inventory = []

    #a dictionary linking a room to other rooms
    rooms = {

        'Hall' : { 
            'south' : 'Kitchen',
            'east'  : 'Dining Room',
            'item'  : 'key'
            },

        'Kitchen' : {
            'north' : 'Hall',
            'item'  : 'monster'
            },
        'Dining Room' : {
            'west'  : 'Hall',
            'south' : 'Garden',
            'item'  : 'potion'
            },
        'Garden'      : {
            'north'   : 'Dining Room'
            }
        }

    #start the player in the Hall
    currentRoom = 'Hall'

    showInstructions()

    #loop forever
    while True:
        showStatus()
        #get the player's next 'move'
        #.split() breaks it up into an list array
        #eg typing 'go east' would give the list:
        #['go','east']
        move = ''
        while move == '':  
            move = input('>')
            move = move.lower().split()

            #if they type 'go' first
            if move[0] == 'go':
                #check that they are allowed wherever they want to go
                if move[1] in rooms[currentRoom]:
                #set the current room to the new room
                    currentRoom = rooms[currentRoom][move[1]]
                #there is no door (link) to the new room
            else:
                print('You can\'t go that way!')

            #if they type 'get' first
            if move[0] == 'get' :
            #if the room contains an item, and the item is the one they want to get
                if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                    #add the item to their inventory
                    inventory += [move[1]]
                    #display a helpful message
                    print(move[1] + ' got!')
                    #delete the item from the room
                    del rooms[currentRoom]['item']
                    #otherwise, if the item isn't there to get
            else:
                #tell them they can't get it
                print('Can\'t get ' + move[1] + '!')
        if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
            print('A monster has go you ... GAME OVER!')
            break
        if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
            print('You escape the house ... YOU WIN!')
            break
#__________________________________________END_CODE_DRIVER_________________________________________#
####################################################################################################
# Project 8 : Create pie charts and bar graphs from data that you collect from members of 
####################################################################################################
def P8_create_char_bar():
    piechar=pygal.Pie() 
    file = open('data.txt','r')
    for line in file.read().splitlines():
      if line:
        lable, value = line.split(' ')
        piechar.add(lable,int(value))
    piechar.render()
    barchar=pygal.Bar()
    for line in file.read().splitlines():
      if line:
        lable, value = line.split(' ')
        barchar.add(lable,int(value))
    barchar.render()
    file.close()

####################################################################################################
# Project 7 : Create modern art om the computer
####################################################################################################
def random_color():
    a = hex(randrange(0,256))
    b = hex(randrange(0,256))
    c = hex(randrange(0,256))
    a = a[2:]
    b = b[2:]
    c = c[2:]
    if len(a)<2:
        a = "0" + a
    if len(b)<2:
        b = "0" + b
    if len(c)<2:
        c = "0" + c
    z = a + b + c
    x=("#" + z.upper())
    color(x)
def random_place():
    penup()
    x=randint(-250,150)
    y=randint(-150,250)
    goto(x,y)
    pendown()
def draw_rectang():
    hideturtle()
    length=randint(10,100)
    height=randint(10,100)
    begin_fill()
    forward(length)
    right(90)
    forward(height)
    right(90)
    forward(length)
    right(90)
    forward(height)
    right(90)
    end_fill()
def draw_turtle():
    shape("turtle")
    shapesize(randint(1,4))
    random_color()
    random_place()
    right(randint(0,360))
    stamp()
    penup()
def draw_star():
    shape("star")
    shapesize(randint(1,4))
    random_color()
    random_place()
    right(randint(0,360))
    stamp()
    penup()
def draw_circle():
    dot(randint(30,150))
    random_color()
    random_place()
def P7_create_modern_art():
    speed(0)
    penup()
    hideturtle()
    for i in range(50):
        draw_circle()
    clear()
    for i in range(50):
        draw_turtle()
    clear()
    for i in range(50):
        draw_star()
    clear()
    for i in range(50):
        draw_rectang()
        shapesize(randint(1,4))
        random_color()
        random_place()
        right(randint(0,360))
def P7_FUNCTION_DETAIL():
    print(help(begin_fill))
    print(help(end_fill))
    print(help(shapesize))
    # print(help('turtle'))
    print(help(shapetransform))
    print(help(stamp))
                # No argument.
                # Stamp a copy of the turtle shape onto the canvas at the current
                # turtle position. Return a stamp_id for that stamp, which can be
                # used to delete it by calling clearstamp(stamp_id)
    print(help(clear))
                # No arguments.
                # Delete the turtle's drawings from the screen. Do not move
                # State and position of the turtle as well as drawings of other
                # turtles are not affected
    print(help(setheading))
                # setheading(to_angle)
                # to_angle -- a number (integer or float)
                #      standard - mode:          logo-mode:
                # -------------------|--------------------
                #    0 - east                0 - north
                #   90 - north              90 - east
                #  180 - west              180 - south
                #  270 - south             270 - west
####################################################################################################
# Project 6 : Encrypt secret message
####################################################################################################
def P6_encrypt_secret_message():
    alphabet='abcdefghijklmnopqrstuvwxyz'
    letter=input('Please Enter Message: ')
    key=input('Enter key(1-26):  ')
    print('Message secret: ',end='')
    message_encrypt=[]
    message_decryption=[]
    for i in letter:
        if i in alphabet:
            message_encrypt+=alphabet[(int(alphabet.index(i)) + int(key))%26]
        else:
            message_encrypt+=i

    for j in message_encrypt:
        print(j,end='')
    print('\n')

    for i in message_encrypt:
        if i in alphabet:
            message_decryption+=alphabet[(int(alphabet.index(i))%26 - int(key))]
        else:
            message_decryption+=i

    for k in message_decryption:
        print(k,end='')
####################################################################################################
# Project 5 : Create a dictionary of colours which maps hard to remember colour codes into friendly names
####################################################################################################
def P5_create_dictionary_color_map():
    speed(1)
    screen= Screen()            # gán biến confix Screen cho 1 biến để sử dụng
    screen.setup(600,600)   # Cài đặt khung màn hình hiển thị
    colours={
      'verrylome': '#A7E30E',
      'reallyraspberry': '#FA057F',
      'yellow' : '#F3E41B',
      'white' : '#F7F6E7',
      'blue__' : '#1E14DF'
    }
    screen.bgcolor(colours['reallyraspberry'])  # Cài đặt màu nền cho màn hình hiển thị

    penup()
    hideturtle()    # Hiden mouse on the screen
    color(colours['yellow'])     # Set color for text
    circle(50,360,6)
    dot(400,colours['verrylome'])
    right(90)
    forward(-100)

    color(colours['reallyraspberry'])     # Set color for text
    stype=('Arial', 40, 'bold')
    write('Thiên Địa',font=stype, align='center')
    forward(60)

    color(colours['blue__'])     # Set color for text
    write('Nhân Gian',font=stype, align='center')
    forward(60)

    color(colours['blue__'])     # Set color for text
    write('Tình Say Đắm',font=stype, align='center')
    forward(220)
    left(90)
    forward(100)

    color('black')     # Set color for text
    stype=('Times New Roman', 20, 'bold')
    write('Mr.ThienCo - 2020',font=stype, align='center')

    forward(2000)
def P5_FUNCTION_DETAIL():
    print(help(dot))        # Vẽ hình tròn dot(Size=None >=1, *color)
    print(help(circle))     # circle(radius, extent, steps) radius:Bán kính; extent : góc hình tròn; steps: cạnh
    print(help(write))      # write(arg, move=False, align='left', font=('Arial', 8, 'normal'))
    print(help(color))      # color(*args)  Cài đặt màu cho thông tin bên dưới của câu lệnh color(x)
    print(help(hideturtle)) # hideturtle()  Ẩn đi chuột trên màn hình terminal
    print(help(bgcolor))    # bgcolor(*args) Cài đặt màu nền
    print(help(setup))      # setup(width=0.5, height=0.75, startx=None, starty=None)
                                # Set the size and position of the main window.
                                # Arguments:
                                # width: as integer a size in pixels, as float a fraction of the
                                #   Default is 50% of
                                # height: as integer the height in pixels, as float a fraction of the
                                #    Default is 75% of
                                # startx: if positive, starting position in pixels from the left
                                #   edge of the screen, if negative from the right edge
                                #   Default, startx=None is to center window horizontally.
                                # starty: if positive, starting position in pixels from the top
                                #   edge of the screen, if negative from the bottom edge
                                #   Default, starty=None is to center window vertically.
                                # Examples:
                                # >>> setup (width=200, height=200, startx=0, starty=0)
                                # sets window to 200x200 pixels, in upper left of screen
####################################################################################################
# Project 4 : Create 2 random teams from a list of players
####################################################################################################
def P4_create_rando_team():

    file=open('player_name.txt','r')
    file_team=open('team_name.txt','r')
    Players=file.read().splitlines()
    Team_Names=file_team.read().splitlines()
    print(Players)

    teamA=[]
    teamB=[]
    teamC=[]

    print('\nPlayers:',Players,'\nTeam Name:',Team_Names,'\nHere are your teams:\n')

    while len(Players) > 0:
      playersA=choice(Players)
      teamA.append(playersA)
      Players.remove(playersA)
      if len(Players)!=0:
          playersB=choice(Players)
          teamB.append(playersB)
          Players.remove(playersB)
      if len(Players)!=0:
          playersC=choice(Players)
          teamC.append(playersC)
          Players.remove(playersC)

    while len(Team_Names) > 0:
      lead_teamA=choice(Team_Names)
      Team_Names.remove(lead_teamA)
      if len(Team_Names)!=0:
          lead_teamB=choice(Team_Names)
          Team_Names.remove(lead_teamB)
      if len(Team_Names)!=0:
          lead_teamC=choice(Team_Names)
          Team_Names.remove(lead_teamC)
          break

    print(lead_teamA,teamA)
    print(lead_teamB,teamB)
    print(lead_teamC,teamC)
#########################################################################
# Project 3 : Turtle walking run 
####################################################################################################
def P3_turtle_racing():
    bgcolor('white')
    speed(20)
    penup()
    goto(-240,140)
    for step in range(18):
      write(step, align='center')
      right(90)
      forward(10)
      pendown()
      for i in range(10):
          penup()
          forward(10)
          pendown()
          forward(10)
      penup()
      backward(210)
      left(90)
      forward(20)

    a_turtle=Turtle()
    a_turtle.color('red')
    a_turtle.shape('turtle')
    a_turtle.penup()
    a_turtle.goto(-240,100)
    a_turtle.right(360)
    a_turtle.pendown()

    b_turtle=Turtle()
    b_turtle.color('blue')
    b_turtle.shape('turtle')
    b_turtle.penup()
    b_turtle.goto(-240,70)
    b_turtle.right(360)
    b_turtle.pendown()

    c_turtle=Turtle()
    c_turtle.color('green')
    c_turtle.shape('turtle')
    c_turtle.penup()
    c_turtle.goto(-240,40)
    c_turtle.right(360)
    c_turtle.pendown()

    d_turtle=Turtle()
    d_turtle.color('yellow')
    d_turtle.shape('turtle')
    d_turtle.penup()
    d_turtle.goto(-240,10)
    d_turtle.right(360)
    d_turtle.pendown()

    e_turtle=Turtle()
    e_turtle.color('black')
    e_turtle.shape('turtle')
    e_turtle.penup()
    e_turtle.goto(-240,-20)
    e_turtle.right(360)
    e_turtle.pendown()

    f_turtle=Turtle()
    f_turtle.color('pink')
    f_turtle.shape('turtle')
    f_turtle.penup()
    f_turtle.goto(-240,-50)
    f_turtle.right(360)
    f_turtle.pendown()

    for i in range(90):
      a_turtle.forward(randint(1,6))
      b_turtle.forward(randint(1,6))
      c_turtle.forward(randint(1,6))
      d_turtle.forward(randint(1,6))
      e_turtle.forward(randint(1,6))
      f_turtle.forward(randint(1,6))
def P3_FUNCTION_DETAIL():
    #____________________________________________ NOTE ________________________________________________#
    print(help(speed))      # Cài đặt tốc độ chạy của rùa trên terminal (x)
    print(help(goto))       # Di chuyển tới tọa độ (x,y)
    print(help(shape))      # Một số hình dạng có sẵn :"arrow, turtle, circle, square, triangle, classic".
    print(help(right))      # Quay 1 góc x độ sang bên phải
    print(help(left))       # Quay 1 góc x độ sang bên trái
    print(help(forward))    # Di chuyển thẳng từ hướng đã định
    print(help(backward))   # Di chuyển lùi về phía sau từ vị trí hiện tại
    print(help(penup))      # Xóa đường di chuyển trên màn hình command
    print(help(pendown))    # Hiện đường di chuyển trên màn hình command
    print(help(write))      # Viết giá trị thể hiện lên màn hình
####################################################################################################
####################################################################################################
# Project 2 : Rock, Paper, Scissors ( Búa kéo giấy ) Game choise rundom number
####################################################################################################
def P2_rock_paper_scissors():
    player=input('Rock: r ; Paper: p ; Scissors: s :\t')
    rock='0'
    paper='____'
    scissors='>8'

    if player == 'r':
      print(rock, 'vs',end=' ')
    elif player == 's':
      print(scissors, 'vs',end=' ')
    elif player == 'p':
      print(paper, 'vs',end=' ')
    else:
      print('???\n', 'vs' , end=' ')

    choise=randint(1,3)
    if choise==1:
      computer = 'r'
      print(rock)
    elif choise==2:
      computer = 'p'
      print(paper)
    else:
      computer = 's'
      print(scissors)

    if player == computer:
      print('Draw')
    elif player == 'r':
      if computer == 'p':
          print('Computer win !')
      elif computer == 's':
          print('Player win !')
    elif player == 's':
      if computer == 'r':
          print('Computer win !')
      elif computer == 'p':
          print('Player win !')
    elif player == 'p':
      if computer == 's':
          print('Computer win !')
      elif computer == 'r':
          print('Player win !')
    else:
      print('Huh?')
####################################################################################################
# Project 1
####################################################################################################
def P1_caculate_age_in_dog_year():
    print('''
      Hello
      I will guess your age in a next dog year ?
      ''')
    print('In the next dog year you will',2030-2018+int(input('What is your age ? \n')) ,'year old')
    print('ha' *4)
    print('ba' + 'na'*2)
    print('Hello' + '!' *10)
####################################################################################################
