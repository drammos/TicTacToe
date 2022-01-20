from cProfile import run
from cgitb import grey
from turtle import Screen, width
import pygame

def draw():
    board = ''

    for i in range(-1,6):

        if i%2==0:
            board += '|     ' * 4
            board += '\n|     |     |     |'

        else:
            board += ' ____ ' * 3

        board += '\n'
    print (board)



class Button():
    
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale( image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = ( x,y)
        self.clicked = False
        
    def draw( self):
        find = False
        
        
        #get the mouse position
        position = pygame.mouse.get_pos()
        if self.rect.collidepoint( position):
            #if is the left click
            #not double click
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                find = True
                            
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        screen.blit( self.image, (self.rect.x, self.rect.y))
        return find
    
class Touch():
    def __init__( self, x, y):
        self.width = 100
        self.height = 100
        self.x = x
        self.y = y
        self.clicked = False
        self.rect = pygame.Rect((self.x,self.y), (self.width, self.height))
        self.find = False
        
    def check( self):
        
        if self.find == True:
            return False  
          
        position = pygame.mouse.get_pos()
        
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        if self.rect.collidepoint( position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.find = True

        return self.find
                
    def take_position( self):
        return ( self.x, self.y)
                
        
        
def draw_new(board):
    b = ''
    start = 0
    for i in range(-1,6):
        if i %2 == 0:
            b += '|     ' * 4
            List = board[start]
            p1 = List[0]
            if p1 == None:
                b += '\n|     |'
            
            elif p1 == "X":
                b += '\n|  X  |'
            else:
                b += '\n|  O  |'
            
            
            p2 = List[1]
            if p2 == None:
                b += '     |'
            
            elif p2 == "X":
                b += '  X  |'
            else:
                b += '  O  |'
            
            
            p3 = List[2]
            if p3 == None:
                b += '     |'
            
            elif p3 == "X":
                b += '  X  |'
            else:
                b += '  O  |'
            
            start += 1
            
        else:
            b += ' ____ ' * 3
            
        b += '\n'
    print(b)
    
    
def create_board():
    board = {}
    for i in range(3):
        board[i] = [( None, None), ( None, None), ( None, None)]
        
    return board


def update_board( board, x, y, symbol, pos):
    element = symbol
    List = board[x - 1]
    
    if List[y - 1] != (None, None):
        return None
    
    List[y - 1] = ( element, pos)
    board[x-1] = List
    return board    
    
    
def check_board( board):

    #check first line
    List = board[0]
    i0, pos1 = List[0]
    i1, pos2 = List[1]
    i2, pos3 = List[2]
    
    if( i0 == "X" and i1 == "X" and i2 == "X"):
        x1,y = pos1
        x3,y = pos3
        return ([x1,y+50], [x3+100,y+50])

    elif( i0 == "O" and i1 == "O" and i2 == "O"):
        x1,y = pos1
        x3,y = pos3
        return ([x1,y+50], [x3+100,y+50])

    #check second line
    List = board[1]
    i0, pos1 = List[0]
    i1, pos2 = List[1]
    i2, pos3 = List[2]

    if( i0 == "X" and i1 == "X" and i2 == "X"):
        x1,y = pos1
        x3,y = pos3
        return ([x1,y+50], [x3+100,y+50])
    
    elif( i0 == "O" and i1 == "O" and i2 == "O"):
        x1,y = pos1
        x3,y = pos3
        return ([x1,y+50], [x3+100,y+50])

    #check third line
    List = board[2]
    i0, pos1 = List[0]
    i1, pos2 = List[1]
    i2, pos3 = List[2]
    if( i0 == "X" and i1 == "X" and i2 == "X"):
        x1,y = pos1
        x3,y = pos3

        return ([x1,y+50], [x3+100,y+50])
    
    elif( i0 == "O" and i1 == "O" and i2 == "O"):
        x1,y = pos1
        x3,y = pos3
        return ([x1,y+50], [x3+100,y+50])
    
    
    List_1 = board[0]
    i0_1, pos1_1 = List_1[0]
    i1_1, pos2_1 = List_1[1]
    i2_1, pos3_1 = List_1[2]
    
    List_2 = board[1]
    i0_2, pos1_2 = List_2[0]
    i1_2, pos2_2 = List_2[1]
    i2_2, pos3_2 = List_2[2]
    
    List_3 = board[2]
    i0_3, pos1_3 = List_3[0]
    i1_3, pos2_3 = List_3[1]
    i2_3, pos3_3 = List_3[2]


    #check first katheti-line
    if( i0_1 == "X" and i0_2 == "X" and i0_3 == "X"):
        
        x,y1 = pos1_1
        x,y3 = pos1_3
        return ([x+50,y1], [x+50,y3+100])
    
    elif( i0_1 == "O" and i0_2 == "O" and i0_3 == "O"):
        x,y1 = pos1_1
        x,y3 = pos1_3
        return ([x+50,y1], [x+50,y3+100])
    
    #check second katheti-line
    if(i1_1 == "X" and i1_2 == "X" and i1_3 == "X"):
        x,y1 = pos2_1
        x,y3 = pos2_3
        return ([x+50,y1], [x+50,y3+100])
        
    elif( i1_1 == "O" and i1_2 == "O" and i1_3 == "O"):
        x,y1 = pos2_1
        x,y3 = pos2_3
        return ([x+50,y1], [x+50,y3+100])
        
    #check third katheti-line
    if( i2_1 == "X" and i2_2 == "X" and i2_3 == "X"):
        x,y1 = pos3_1
        x,y3 = pos3_3
        return ([x+50,y1], [x+50,y3+100])
        
    elif( i2_1 == "O" and i2_2 == "O" and i2_3 == "O"):
        x,y1 = pos3_1
        x,y3 = pos3_3
        return ([x+50,y1], [x+50,y3+100])
    
    
    #check the first side-line
    if( i0_1 == "X" and i1_2 == "X" and i2_3 == "X"):
        x1,y1 = pos1_1
        x3,y3 = pos3_3
        return ([x1,y1], [x3+100,y3+100])
    
    elif( i0_1 == "O" and i1_2 == "O" and i2_3 == "O"):
        x1,y1 = pos1_1
        x3,y3 = pos3_3
        return ([x1,y1], [x3+100,y3+100])
    
    #check the second side-line
    if( i2_1 == "X" and i1_2 == "X" and i0_3 == "X"):
        x1,y1 = pos1_3
        x3,y3 = pos3_1
        return ([x1,y1+100], [x3+100,y3])
    
    elif( i2_1 == "O" and i1_2 == "O" and i0_3 == "O"):
        x1,y1 = pos1_3
        x3,y3 = pos3_1
        return ([x1,y1+100], [x3+100,y3])
    
    return None
    
    
def two_players( screen):
    print("Start Game")
    board = create_board()
    
    e = pygame.image.load('exit.png').convert_alpha()
    b = pygame.image.load('go-back.png').convert_alpha()
    x_icon = pygame.image.load('pic_x.png').convert_alpha()
    o_icon = pygame.image.load('pic_o.png').convert_alpha()
    play_a = pygame.image.load('replay.png').convert_alpha()
    
    play_again = Button(370,470,play_a, 1)
    Exit = Button( 625, 450, e, 1)
    Back = Button( 50, 482, b, 1)
    
    x_l = Button( 100, 32, x_icon, 0.3)
    o_l = Button( 550, 24, o_icon, 0.4)
  
  
  
    start = 250
    y = 100
    Table = []
    num = 0
    while num < 9:
        x = start
        t = Touch( x, y)
        Table.append(t)
        num+=1
        
        x = start + 100
        t = Touch( x, y)
        Table.append(t)
        num += 1
        
        x = start + 200
        t = Touch( x, y)
        Table.append(t)
        num += 1
        
        y += 100    
        # start
    # Define the colors we will use in RGB format
    
    BLACK = (  0,   0,   0)
    BLACK_1 = (  74,   74,   74)

    WHITE = (255, 255, 255)
    BLUE =  (  0,   0, 255)
    BLUE_1 =  (  30,   144, 255)
    
    GREEN = (  0, 255,   0)
    RED =   (255,   0,   0)
    ORANGE = (255, 165, 0)
    GREY = ( 128, 128, 128)

    Font = pygame.font.SysFont("None",50)


    i = 0
    score_x = 0
    score_o = 0
    price_back = True
    running = True
    play = True
    square = 0
    while running:

        screen.fill( (30,144,255))

        if Exit.draw() == True:
            running = False    
            price_back = False
        if Back.draw() == True:
            running = False
            
        x_l.draw()
        o_l.draw()
        
                   
            
        pygame.draw.line( screen, BLACK_1, [350,100], [350,400], 5)
        pygame.draw.line( screen, BLACK_1, [450,100], [450,400], 5)

        pygame.draw.line( screen, BLACK_1, [250,200], [550,200], 5)
        pygame.draw.line( screen, BLACK_1, [250,300], [550,300], 5)
        
        
        
        if play == True:
            find_x_y = 0
            find_y = 1
            find_x = 1
            x = 0
            y = 0
            for t in Table:
                
                if t.check() == True:
                    pos = t.take_position()
                    x, y = pos
                    if find_x_y <= 2:
                        find_x = 1
                        find_y = find_x_y + 1
                    elif find_x_y <= 5:
                        find_x = 2
                        find_y = find_x_y - 2
                    else:
                        find_x = 3
                        find_y = find_x_y - 5
                    square+=1
                    if i == 0:
                        board = update_board(board, find_x, find_y, "X", pos)
                        i = 1
                    else:
                        board = update_board(board, find_x, find_y, "O", pos)
                        i = 0
                    break
                find_x_y += 1
                
        
        
        Font = pygame.font.SysFont("None", 60)


        score = Font.render( str(score_x), False, WHITE, BLUE_1)
        screen.blit( score, ( 225, 33))
        
        score = Font.render( str(score_o), False, WHITE, BLUE_1)
        screen.blit( score, ( 675, 34))
        
        
        
        
        
        for k in range(3):
            List = board[k]
            for elem in List:
                element, position = elem
                if element != None:
                    x, y = position
                    
                    if element == "X":
                        x1 = Button( x + 20, y + 20, x_icon, 0.5)
                        x1.draw()
                    else:
                        o1 = Button( x + 10, y + 10, o_icon, 0.6)
                        o1.draw() 
                        
        price = check_board( board)
        if price != None:
            l1,l2 = price
            if i == 0:
                if play == True:
                    score_o +=1
                #red
                pygame.draw.line( screen, RED, l1, l2, 5)

            else:
                if play == True:
                    score_x+=1
                #black                             
                pygame.draw.line( screen, BLACK, l1, l2, 5)
            play = False
            
        if play == True:
            if i == 0:
                pygame.draw.line( screen, GREY, [100,75], [275,75], 4)
            else:
                pygame.draw.line( screen, GREY, [550,77], [725,77], 4)
        
        
        if play == True and square == 9:
            play = False
            
        if play == False:
            if play_again.draw() == True:
                square = 0
                play = True
                board = create_board()
                Table.clear()
                Table = []
                start = 250
                y = 100
                num = 0
                while num < 9:
                    x = start
                    t = Touch( x, y)
                    Table.append(t)
                    num+=1
                    
                    x = start + 100
                    t = Touch( x, y)
                    Table.append(t)
                    num += 1
                    
                    x = start + 200
                    t = Touch( x, y)
                    Table.append(t)
                    num += 1
                    
                    y += 100 
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

        pygame.display.update()

    return price_back


        # print("\nFirst Player with X")
        # x = int(input("Give x   "))        
        # y = int(input("Give y   "))  
        # board = update_board( board, x, y, "X")
        # while board == None:
            
        #     print("\nWrong Input for Player 1, Please try again")
        #     x = int(input("Give x   "))        
        #     y = int(input("Give y   "))  
        #     board = update_board( board, x, y, "X")
        
        # if check_board( board) == True:
        #     break
        
        
        # print("\nSecond Player with O")
        # x = int(input("Give x   "))        
        # y = int(input("Give y   "))  
        # board = update_board( board, x, y, "O")
        # while board == None:
            
        #     print("\nWrong Input for Player 2, Please try again")
        #     x = int(input("Give x   "))        
        #     y = int(input("Give y   "))  
        #     board = update_board( board, x, y, "O")

        # if check_board( board) == True:
        #     break
        
        
def one_player( screen):
    print("Start Game")
    board = create_board()
    
    e = pygame.image.load('exit.png').convert_alpha()
    b = pygame.image.load('go-back.png').convert_alpha()
    x_icon = pygame.image.load('pic_x.png').convert_alpha()
    o_icon = pygame.image.load('pic_o.png').convert_alpha()
    play_a = pygame.image.load('replay.png').convert_alpha()
    
    play_again = Button(370,470,play_a, 1)
    Exit = Button( 625, 450, e, 1)
    Back = Button( 50, 482, b, 1)
    
    x_l = Button( 100, 32, x_icon, 0.3)
    o_l = Button( 550, 24, o_icon, 0.4)
  
  
  
    start = 250
    y = 100
    Table = []
    num = 0
    while num < 9:
        x = start
        t = Touch( x, y)
        Table.append(t)
        num+=1
        
        x = start + 100
        t = Touch( x, y)
        Table.append(t)
        num += 1
        
        x = start + 200
        t = Touch( x, y)
        Table.append(t)
        num += 1
        
        y += 100    
        # start
    # Define the colors we will use in RGB format
    
    BLACK = (  0,   0,   0)
    BLACK_1 = (  74,   74,   74)

    WHITE = (255, 255, 255)
    BLUE =  (  0,   0, 255)
    BLUE_1 =  (  30,   144, 255)
    
    GREEN = (  0, 255,   0)
    RED =   (255,   0,   0)
    ORANGE = (255, 165, 0)
    GREY = ( 128, 128, 128)

    Font = pygame.font.SysFont("None",50)


    i = 0
    score_x = 0
    score_o = 0
    price_back = True
    running = True
    play = True
    square = 0
    play_x = True
    while running:

        screen.fill( (30,144,255))

        if Exit.draw() == True:
            running = False    
            price_back = False
        if Back.draw() == True:
            running = False
            
        x_l.draw()
        o_l.draw()
        
                   
            
        pygame.draw.line( screen, BLACK_1, [350,100], [350,400], 5)
        pygame.draw.line( screen, BLACK_1, [450,100], [450,400], 5)

        pygame.draw.line( screen, BLACK_1, [250,200], [550,200], 5)
        pygame.draw.line( screen, BLACK_1, [250,300], [550,300], 5)
        
        
        
        if play == True and play_x == True:
            find_x_y = 0
            find_y = 1
            find_x = 1
            x = 0
            y = 0
            for t in Table:
                
                if t.check() == True:
                    pos = t.take_position()
                    x, y = pos
                    if find_x_y <= 2:
                        find_x = 1
                        find_y = find_x_y + 1
                    elif find_x_y <= 5:
                        find_x = 2
                        find_y = find_x_y - 2
                    else:
                        find_x = 3
                        find_y = find_x_y - 5
                    square+=1
                    if i == 0:
                        board = update_board(board, find_x, find_y, "X", pos)
                        i = 1
                        play_x = False
                    # else:
                        # board = update_board(board, find_x, find_y, "O", pos)
                        # i = 0
                    break
                find_x_y += 1
        if play == True and play_x == False:
            # theBestMove = 
            print("pao")
        
        Font = pygame.font.SysFont("None", 60)


        score = Font.render( str(score_x), False, WHITE, BLUE_1)
        screen.blit( score, ( 225, 33))
        
        score = Font.render( str(score_o), False, WHITE, BLUE_1)
        screen.blit( score, ( 675, 34))
        
        
        
        
        
        for k in range(3):
            List = board[k]
            for elem in List:
                element, position = elem
                if element != None:
                    x, y = position
                    
                    if element == "X":
                        x1 = Button( x + 20, y + 20, x_icon, 0.5)
                        x1.draw()
                    else:
                        o1 = Button( x + 10, y + 10, o_icon, 0.6)
                        o1.draw() 
                        
        price = check_board( board)
        if price != None:
            l1,l2 = price
            if i == 0:
                if play == True:
                    score_o +=1
                #red
                pygame.draw.line( screen, RED, l1, l2, 5)

            else:
                if play == True:
                    score_x+=1
                #black                             
                pygame.draw.line( screen, BLACK, l1, l2, 5)
            play = False
            
        if play == True:
            if i == 0:
                pygame.draw.line( screen, GREY, [100,75], [275,75], 4)
            else:
                pygame.draw.line( screen, GREY, [550,77], [725,77], 4)
        
        
        if play == True and square == 9:
            play = False
            
        if play == False:
            if play_again.draw() == True:
                square = 0
                play = True
                board = create_board()
                Table.clear()
                Table = []
                start = 250
                y = 100
                num = 0
                while num < 9:
                    x = start
                    t = Touch( x, y)
                    Table.append(t)
                    num+=1
                    
                    x = start + 100
                    t = Touch( x, y)
                    Table.append(t)
                    num += 1
                    
                    x = start + 200
                    t = Touch( x, y)
                    Table.append(t)
                    num += 1
                    
                    y += 100 
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

        pygame.display.update()

    return price_back


if __name__ == "__main__":
    
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    
    
    
    #title and icon
    pygame.display.set_caption("Tic Tac Toe")

    
    trie = pygame.image.load('tic-tac-toe256.png').convert_alpha()
    p1 = pygame.image.load('p2.jpg').convert_alpha()
    p2 = pygame.image.load('p1.jpg').convert_alpha()
    e = pygame.image.load('exit.png').convert_alpha()

    tic = Button( 300, 100, trie, 1)
    b_p1 = Button( 175, 375, p1, 1)
    b_p2 = Button( 450, 375, p2, 1)
    Exit = Button( 350, 450, e, 1)
    
    running = True
    while running:
        screen.fill((0,255,255))
        
        tic.draw()
        if b_p1.draw() == True:
            if one_player( screen) == False:
                running = False
                break
            print("One")
            
        if b_p2.draw() == True:
            if two_players( screen) == False:
                running = False
                break
            print("Two")
        
        if Exit.draw() == True:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False    
        
        pygame.display.update()
    
    # while(1):
        
    #     players = int(input("How many players?\n"))
    #     if players == 2:
    #         two_players()
    #         break
    #     elif players == 1:
    #         one_player()
    #         break
    #     else:
    #         print("Wrong input")

        
