#!/usr/bin/python
from random import *  # Gọi hàm random số tự nhiên trong 1 khoảng nào đó : randint(1,5)
# from random import choice   # Gọi hàm random giá trị trong mảng
from turtle import *        # Gọi thư viện dùng cho Project 3
import pygal

import json
import urllib.request

####################################################################################################
# Project 10 : Where is the space Station
####################################################################################################
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)


####################################################################################################
# Project 9 : design and code your own RPG maze game
####################################################################################################


# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
    print('''
    RPG Game
    ========
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
