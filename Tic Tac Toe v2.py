# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 00:26:25 2015

@author: PanosXY
"""


ttt1 = '   |   |   '
ttt2 = '---|---|---'
ttt3 = '   |   |   '
ttt4 = '---|---|---'
ttt5 = '   |   |   '

EndOfGame = False
player    = 1
history   = []
match     = True

l1 = [0]*3
l2 = [0]*3
l3 = [0]*3

indexes = { 'index00' : 1,
            'index01' : 5,
            'index02' : 9,
            'index10' : 1,
            'index11' : 5,
            'index12' : 9,
            'index20' : 1,
            'index21' : 5,
            'index22' : 9 }

def CheckInput(cell):
    while cell[0] > 2 or cell[1] > 2:
        print "Maximum cell is '2, 2'"
	try:
            cell = list(input('Put a cell player %d: ' %player))
	except KeyboardInterrupt:
	    print 'Keyboard Interrupt'
	    exit()
	except:
	    print 'Put a valid cell (X,Y)'
            cell = [3, 3]
    return cell

def PrintTicTacToe():    
    global ttt1, ttt2, ttt3, ttt4, ttt5
    
    if EndOfGame == True:
        return
    
    print ttt1
    print ttt2
    print ttt3
    print ttt4
    print ttt5

def SwitchPlayer():
    global player
    player += 1
    if player > 2:
        player = 1

WriteHistory = lambda cell: history.append(cell)

def Winner(player):
    global EndOfGame

    if EndOfGame:
        print 'This is a double win!!!'
        return
    
    print '\n\nCongratulations Player %d, you are the winner!' %player
    EndOfGame = True

PrintTicTacToe()
while EndOfGame == False:
    #Prompt User for a cell
    try:
    	cell = list(input('Put a cell player %d: ' %player))
    except KeyboardInterrupt:
        print 'Keyboard Interrupt'
        exit()
    except:
	print 'Put a valid cell (X,Y)'
	cell = [3, 3]
    cell = CheckInput(cell)
     
    #Check if the cell is allready written 
    while match == True:
        match = False
        for i in xrange(len(history)):
            if cell == history[i]:
                print 'This cell is already written'
		try:
		    cell = list(input('Put a cell player %d: ' %player))
	        except KeyboardInterrupt:
        	    print 'Keyboard Interrupt'
	            exit()
		except:
		    print 'Put a valid cell (X,Y)'
		    cell = [3, 3]
                cell = CheckInput(cell)
                match = True
    
    #Put the mark of the respective player on the right spot
    for key in indexes:
        key0 = int(key[5])
        key1 = int(key[6]) 
        if cell[0] == key0 and cell[1] == key1:
            if player == 1:
                if key0 == 0:
                    ttt1 = ttt1[:indexes[key]] + ttt1[indexes[key]].replace(" ", "X") + ttt1[indexes[key]+1:]
                    l1[cell[1]] = 'X'
                elif key0 == 1:
                    ttt3 = ttt3[:indexes[key]] + ttt3[indexes[key]].replace(" ", "X") + ttt3[indexes[key]+1:]
                    l2[cell[1]] = 'X'
                elif key0 == 2:
                    ttt5 = ttt5[:indexes[key]] + ttt5[indexes[key]].replace(" ", "X") + ttt5[indexes[key]+1:]
                    l3[cell[1]] = 'X'
            if player == 2:
                if key0 == 0:
                    ttt1 = ttt1[:indexes[key]] + ttt1[indexes[key]].replace(" ", "O") + ttt1[indexes[key]+1:]
                    l1[cell[1]] = 'O'
                elif key0 == 1:
                    ttt3 = ttt3[:indexes[key]] + ttt3[indexes[key]].replace(" ", "O") + ttt3[indexes[key]+1:]
                    l2[cell[1]] = 'O'
                elif key0 == 2:
                    ttt5 = ttt5[:indexes[key]] + ttt5[indexes[key]].replace(" ", "O") + ttt5[indexes[key]+1:]
                    l3[cell[1]] = 'O'
                    
    #Print the table
    PrintTicTacToe()  
    
    #Check if there is a winner
    #Horizontal
    if len(set(l1)) == 1 or len(set(l2)) == 1 or len(set(l3)) == 1:
        if set(l1) == set(['X']) or set(l2) == set(['X']) or set(l3) == set(['X']):
            Winner(player)
        elif set(l1) == set(['O']) or set(l2) == set(['O']) or set(l3) == set(['O']):
            Winner(player)
    
    #Vertical
    for i in xrange(3):
        if l1[i] == l2[i] == l3[i] == 'X':
            Winner(player)
        elif l1[i] == l2[i] == l3[i] == 'O':
            Winner(player)
    
    #Diagonal        
    if l1[0] == l2[1] == l3[2] == 'X' or l1[2] == l2[1] == l3[0] == 'X':
        Winner(player)
    elif l1[0] == l2[1] == l3[2] == 'O' or l1[2] == l2[1] == l3[0] == 'O':
        Winner(player)
        
    #Continue if there is no winner            
    match = True
    WriteHistory(cell)   

    #Check for tie
    if len(history) == 9 and EndOfGame == False:
        print "\n\nStalemate!"
        EndOfGame = True
    
    SwitchPlayer()
