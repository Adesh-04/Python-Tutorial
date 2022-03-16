#Position is from white's Perspective

  #      movement  ||   capture   ||    checking   ||    special  
#pawn -     done          done            not           promotion not done | en-passant not done
#rook -     not           not             not               --*--
#knight-    not           not             not           forks maybe never
#bishop-    not           not             not               --*--
#queen-     not           not             not               --*--
#king -     not           not             not           castling done



pieces = [ 'R', 'N', 'B', 'Q', 'K']  # Rooks, KNights, Bishops, Queen, King respectively

emptySquare = '    '
cover = '='

moveNo = 0
position = ''
capture = ''
isWhite = True
canMove = False
target = []
diff = 0

white_rookA_moves = False
white_rookH_moves = False 
white_king_moves = False

black_rookA_moves = False
black_rookH_moves = False 
black_king_moves = False

chess_squares = {

'a1' : 'W{R}','b1' : 'W{N}','c1' : 'W{B}','d1' : 'W{Q}','e1' : 'W{K}','f1' : 'W{B}','g1' : 'W{N}','h1' : 'W{R}',
'a2' : 'W{P}','b2' : 'W{P}','c2' : 'W{P}','d2' : 'W{P}','e2' : 'W{P}','f2' : 'W{P}','g2' : 'W{P}','h2' : 'W{P}',
'a3' : emptySquare,'b3' : emptySquare,'c3' : emptySquare,'d3' : emptySquare,'e3' : emptySquare,'f3' : emptySquare,'g3' : emptySquare,'h3' : emptySquare,
'a4' : emptySquare,'b4' : emptySquare,'c4' : emptySquare,'d4' : emptySquare,'e4' : emptySquare,'f4' : emptySquare,'g4' : emptySquare,'h4' : emptySquare,
'a5' : emptySquare,'b5' : emptySquare,'c5' : emptySquare,'d5' : emptySquare,'e5' : emptySquare,'f5' : emptySquare,'g5' : emptySquare,'h5' : emptySquare,
'a6' : emptySquare,'b6' : emptySquare,'c6' : emptySquare,'d6' : emptySquare,'e6' : emptySquare,'f6' : emptySquare,'g6' : emptySquare,'h6' : emptySquare,
'a7' : 'B{P}','b7' : 'B{P}','c7' : 'B{P}','d7' : 'B{P}','e7' : 'B{P}','f7' : 'B{P}','g7' : 'B{P}','h7' : 'B{P}',
'a8' : 'B{R}','b8' : 'B{N}','c8' : 'B{B}','d8' : 'B{Q}','e8' : 'B{K}','f8' : 'B{B}','g8' : 'B{N}','h8' : 'B{R}'

}

possible_pawn_moves = [
    'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'b2' 'b3', 'b4', 'b5', 'b6', 'b7', 'c2' 'c3', 'c4', 'c5', 'c6', 'c7', 'd2' 'd3', 'd4', 'd5', 'd6', 'd7',
    'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'f2' 'f3', 'f4', 'f5', 'f6', 'f7', 'g2' 'g3', 'g4', 'g5', 'g6', 'g7', 'h2' 'h3', 'h4', 'h5', 'h6', 'h7'
]


board_files = [ 'a', 'b', 'c', 'd', 'e', 'f' ,'g', 'h'] 
board_ranks = [ 1, 2, 3, 4, 5, 6, 7, 8]  


def pawn(notation, list_of ):
    global moveNo
    if chess_squares.get(notation, 'garbage') == emptySquare :
        if isWhite :
            list_of.append( int(list_of.pop() ) - 1) 
            position = ''.join(map(str, list_of))
            if chess_squares.get(position) == "W{P}" :      # checking for moving one square for white
                chess_squares.update({position : emptySquare})  
                chess_squares.update({notation : "W{P}"})
                moveNo +=1
                print(f'Move = {moveNo}')
            else :
                list_of.append( int(list_of.pop() ) - 1)
                position = ''.join(map(str, list_of))
                if chess_squares.get(position) == "W{P}" and list_of[1] == 2 :    # checking for moving two square for white
                    chess_squares.update({position : emptySquare})
                    chess_squares.update({notation : "W{P}"})
                    moveNo +=1
                    print(f'Move = {moveNo}')
                else :
                    print('Invalid Command')
                

        else :
            list_of.append( int(list_of.pop() ) + 1)
            position = ''.join(map(str, list_of))
            if chess_squares.get(position) == "B{P}" :        # checking for moving one square for Black
                chess_squares.update({position : emptySquare})
                chess_squares.update({notation : "B{P}"})
                moveNo +=1
                print(f'Move = {moveNo}')
            else :
                list_of.append( int(list_of.pop() ) + 1)
                position = ''.join(map(str, list_of))
                if chess_squares.get(position) == "B{P}" and list_of[1] == 7 :    # checking for moving two square for Black
                    chess_squares.update({position : emptySquare})
                    chess_squares.update({notation : "B{P}"})
                    moveNo +=1
                    print(f'Move = {moveNo}')
                else :
                    print('Invalid Command')    
    else:
        print('The Sqaure is occupied by a piece')
    return moveNo
        

def castle(notation):
    global moveNo
    if notation == 'O-O-O':    # long castle
        if isWhite:
            if chess_squares.get('a1') == 'W{R}' and chess_squares.get('e1') == 'W{K}':    # checking for rook and king position   
                if white_rookA_moves == False and white_king_moves == False:                # checking if moved
                    if chess_squares.get('b1') == emptySquare and chess_squares.get('c1') == emptySquare and chess_squares.get('d1') == emptySquare:
                        chess_squares.update({ 'c1' : 'W{K}' })
                        chess_squares.update({ 'd1' : 'W{R}' })
                        chess_squares.update({ 'e1' : emptySquare })
                        chess_squares.update({ 'a1' : emptySquare })
                        moveNo += 1
                    else :
                        print('Move Pieces first')
                else:
                    print('pieces already moved')
            else:
                print('Invalid Command')
        else :
            if chess_squares.get('a8') == 'W{R}' and chess_squares.get('e8') == 'W{K}':    # checking for rook and king position   
                if black_rookA_moves == False and black_king_moves == False:                # checking if moved
                    if chess_squares.get('b8') == emptySquare and chess_squares.get('c8') == emptySquare and chess_squares.get('d8') == emptySquare:
                        chess_squares.update({ 'c8' : 'B{K}' })
                        chess_squares.update({ 'd8' : 'B{R}' })
                        chess_squares.update({ 'e8' : emptySquare })
                        chess_squares.update({ 'a8' : emptySquare })
                        moveNo += 1
                    else :
                        print('Move Pieces first')
                else:
                    print('pieces already moved')
            else:
                print('Invalid Command')

    elif notation == 'O-O':    # short castle
        if isWhite:
            if chess_squares.get('h1') == 'W{R}' and chess_squares.get('e1') == 'W{K}':    # checking for rook and king position   
                if white_rookH_moves == False and white_king_moves == False:                # checking if moved
                    if chess_squares.get('f1') == emptySquare and chess_squares.get('g1') == emptySquare:
                        chess_squares.update({ 'g1' : 'W{K}' })
                        chess_squares.update({ 'f1' : 'W{R}' })
                        chess_squares.update({ 'e1' : emptySquare })
                        chess_squares.update({ 'h1' : emptySquare })
                        moveNo += 1
                    else :
                        print('Move Pieces first')
                else:
                    print('pieces already moved')
            else:
                print('Invalid Command')
        else :
            if chess_squares.get('h8') == 'B{R}' and chess_squares.get('e8') == 'B{K}':    # checking for rook and king position   
                if black_rookH_moves == False and black_king_moves == False:                # checking if moved
                    if chess_squares.get('f8') == emptySquare and chess_squares.get('g8') == emptySquare:
                        chess_squares.update({ 'g8' : 'B{K}' })
                        chess_squares.update({ 'f8' : 'B{R}' })
                        chess_squares.update({ 'e8' : emptySquare })
                        chess_squares.update({ 'h8' : emptySquare })
                        moveNo += 1
                    else :
                        print('Move Pieces first')
                else:
                    print('pieces already moved')
            else:
                print('Invalid Command')

    else:
        print('for Castling use Capital O not zero')

    return moveNo


def capture_pawn(list_of):
    global moveNo
    target.clear()
    target.append( list_of[2] )
    target.append( list_of[3] )
    capture = ''.join(map(str, target))      #d3
    target.clear()

    if chess_squares.get(capture, 'garbage') != emptySquare:
        if isWhite:
            target.append( list_of[0] )
            target.append( int(list_of[3]) - 1 )
            position = ''.join(map(str,target))   #f2
            target.clear()
            if chess_squares.get(position) == 'W{P}':       # capture for pawn for white
                chess_squares.update({position : emptySquare})
                chess_squares.update({capture : 'W{P}'})
                moveNo +=1
        else:
            target.append( list_of[0] )
            target.append( int(list_of[3]) + 1 )
            position = ''.join(map(str,target))   #f2
            target.clear()
            if chess_squares.get(position) == 'B{P}':       # capture for pawn for Black
                chess_squares.update({position : emptySquare})
                chess_squares.update({capture : 'B{P}'})
                moveNo +=1
            else :
                pass      # remaining for others
                
    else :
        print('There is nothing to be captured')

    return moveNo


def rook(list_of):
    global moveNo
    global canMove
    if len(list_of) == 4:                         # for Rad4  or Rdd4
        target.clear()
        target.append(list_of[2])
        target.append(list_of[3])
        capture = ''.join(target)               # not capture but where to move
        target.clear()

        if chess_squares.get(capture) == emptySquare:   
            if isWhite:                       
                if list_of[1] == list_of[2] :               # for Rdd4
                    target.append(list_of[1])

                    for i in board_ranks:
                        target.append(i)
                        position = ''.join(map(str, target))
                        
                        if chess_squares.get(position, 'garbage') == 'W{R}':
                            break
                        else:
                            position = ''
                    
                    if position != '':
                        
                        if target[1] < int(list_of[3]):
                            diff = int(list_of[3]) - int(target[1])
                            
                            for i in range(1,diff):
                                
                                target[1] += 1
                                diff = ''.join(map(str, target))
                                if chess_squares.get(diff) == emptySquare:
                                    canMove = True
                                    continue
                                else:
                                    canMove = False
                                    break
                            if canMove :
                                chess_squares.update({capture : 'W{R}'})
                                chess_squares.update({position : emptySquare})
                                moveNo += 1
                                
                            else :
                                print('move pieces first')

                        elif int(list_of[3]) < target[1]:
                            diff = int(target[1]) - int(list_of[3])
                            
                            for i in range(1,diff):
                                
                                target[1] -= 1
                                diff = ''.join(map(str, target))
                                if chess_squares.get(diff) == emptySquare:
                                    canMove = True
                                    continue
                                else:
                                    canMove = False
                                    break
                            if canMove :
                                chess_squares.update({capture : 'W{R}'})
                                chess_squares.update({position : emptySquare})
                                moveNo += 1
                                
                            else :
                                print('move pieces first')
                    else:
                        print('Enter Valid Rank')

            else:                       
                if list_of[1] == list_of[2] :               # for Rdd4
                    target.append(list_of[1])

                    for i in board_ranks:
                        target.append(i)
                        position = ''.join(map(str, target))
                        
                        if chess_squares.get(position, 'garbage') == 'B{R}':
                            print(position)                                         ##############
                            break
                        else:
                            position = ''
                    
                    if position != '':
                        
                        if target[1] < int(list_of[3]):
                            diff = int(list_of[3]) - int(target[1])
                            
                            for i in range(1,diff):
                                
                                target[1] += 1
                                diff = ''.join(map(str, target))
                                if chess_squares.get(diff) == emptySquare:
                                    canMove = True
                                    continue
                                else:
                                    canMove = False
                                    break
                            if canMove :
                                chess_squares.update({capture : 'B{R}'})
                                chess_squares.update({position : emptySquare})
                                moveNo += 1
                                
                            else :
                                print('move pieces first')
                        
                        elif target[1] > int(list_of[3]):
                            diff =  int(target[1]) - int(list_of[3]) 
                            
                            for i in range(1,diff):
                                
                                target[1] -= 1
                                diff = ''.join(map(str, target))
                                if chess_squares.get(diff) == emptySquare:
                                    canMove = True
                                    continue
                                else:
                                    canMove = False
                                    break
                            if canMove :
                                chess_squares.update({capture : 'B{R}'})
                                chess_squares.update({position : emptySquare})
                                moveNo += 1
                                
                            else :
                                print('move pieces first')
                    else:
                        print('Enter Valid Rank')
        else: 
            print('square is occupied')
    return moveNo




print('\nExit: exit the game\n')





while True:

    if chess_squares.get('a1') == emptySquare:
        white_rookA_moves = True
    elif chess_squares.get('a8') == emptySquare:
        black_rookA_moves = True
    elif chess_squares.get('h8') == emptySquare:
        black_rookH_moves = True
    elif chess_squares.get('h1') == emptySquare:
        white_rookH_moves = True


    a1 = chess_squares.get('a1' , 'W{R}')
    b1 = chess_squares.get('b1' , 'W{N}')
    c1 = chess_squares.get('c1' , 'W{B}')
    d1 = chess_squares.get('d1' , 'W{Q}')
    e1 = chess_squares.get('e1' , 'W{K}')
    f1 = chess_squares.get('f1' , 'W{B}')
    g1 = chess_squares.get('g1' , 'W{N}')
    h1 = chess_squares.get('h1' , 'W{R}')

    a2 = chess_squares.get('a2' , 'W{P}')
    b2 = chess_squares.get('b2' , 'W{P}')
    c2 = chess_squares.get('c2' , 'W{P}')
    d2 = chess_squares.get('d2' , 'W{P}')
    e2 = chess_squares.get('e2' , 'W{P}')
    f2 = chess_squares.get('f2' , 'W{P}')
    g2 = chess_squares.get('g2' , 'W{P}')
    h2 = chess_squares.get('h2' , 'W{P}')

    a3 = chess_squares.get('a3' , emptySquare)
    b3 = chess_squares.get('b3' , emptySquare)
    c3 = chess_squares.get('c3' , emptySquare)
    d3 = chess_squares.get('d3' , emptySquare)
    e3 = chess_squares.get('e3' , emptySquare)
    f3 = chess_squares.get('f3' , emptySquare)
    g3 = chess_squares.get('g3' , emptySquare)
    h3 = chess_squares.get('h3' , emptySquare)

    a4 = chess_squares.get('a4' , emptySquare)
    b4 = chess_squares.get('b4' , emptySquare)
    c4 = chess_squares.get('c4' , emptySquare)
    d4 = chess_squares.get('d4' , emptySquare)
    e4 = chess_squares.get('e4' , emptySquare)
    f4 = chess_squares.get('f4' , emptySquare)
    g4 = chess_squares.get('g4' , emptySquare)
    h4 = chess_squares.get('h4' , emptySquare)

    a5 = chess_squares.get('a5' , emptySquare)
    b5 = chess_squares.get('b5' , emptySquare)
    c5 = chess_squares.get('c5' , emptySquare)
    d5 = chess_squares.get('d5' , emptySquare)
    e5 = chess_squares.get('e5' , emptySquare)
    f5 = chess_squares.get('f5' , emptySquare)
    g5 = chess_squares.get('g5' , emptySquare)
    h5 = chess_squares.get('h5' , emptySquare)

    a6 = chess_squares.get('a6' , emptySquare)
    b6 = chess_squares.get('b6' , emptySquare)
    c6 = chess_squares.get('c6' , emptySquare)
    d6 = chess_squares.get('d6' , emptySquare)
    e6 = chess_squares.get('e6' , emptySquare)
    f6 = chess_squares.get('f6' , emptySquare)
    g6 = chess_squares.get('g6' , emptySquare)
    h6 = chess_squares.get('h6' , emptySquare)

    a7 = chess_squares.get('a7' , 'B{P}')
    b7 = chess_squares.get('b7' , 'B{P}')
    c7 = chess_squares.get('c7' , 'B{P}')
    d7 = chess_squares.get('d7' , 'B{P}')
    e7 = chess_squares.get('e7' , 'B{P}')
    f7 = chess_squares.get('f7' , 'B{P}')
    g7 = chess_squares.get('g7' , 'B{P}')
    h7 = chess_squares.get('h7' , 'B{P}')

    a8 = chess_squares.get('a8' , 'B{R}')
    b8 = chess_squares.get('b8' , 'B{N}')
    c8 = chess_squares.get('c8' , 'B{B}')
    d8 = chess_squares.get('d8' , 'B{Q}')
    e8 = chess_squares.get('e8' , 'B{K}')
    f8 = chess_squares.get('f8' , 'B{B}')
    g8 = chess_squares.get('g8' , 'B{N}')
    h8 = chess_squares.get('h8' , 'B{R}')

    print(f'\n   {cover * 44}\n ')
    print(f'8. | {a8}|{b8}|{c8}|{d8}|{e8}|{f8}|{g8}|{h8} |   <----- Black ')
    print(f'   |  -- + -- + -- + -- + -- + -- + -- + --  | ')
    print(f'7. | {a7}|{b7}|{c7}|{d7}|{e7}|{f7}|{g7}|{h7} | ')
    print(f'   |  -- + -- + -- + -- + -- + -- + -- + --  | ')
    print(f'6. | {a6}|{b6}|{c6}|{d6}|{e6}|{f6}|{g6}|{h6} | ')
    print(f'   |  -- + -- + -- + -- + -- + -- + -- + --  | ')
    print(f'5. | {a5}|{b5}|{c5}|{d5}|{e5}|{f5}|{g5}|{h5} | ')
    print(f'   |  -- + -- + -- + -- + -- + -- + -- + --  | ')
    print(f'4. | {a4}|{b4}|{c4}|{d4}|{e4}|{f4}|{g4}|{h4} | ')
    print(f'   |  -- + -- + -- + -- + -- + -- + -- + --  | ')
    print(f'3. | {a3}|{b3}|{c3}|{d3}|{e3}|{f3}|{g3}|{h3} | ')
    print(f'   |  -- + -- + -- + -- + -- + -- + -- + --  | ')
    print(f'2. | {a2}|{b2}|{c2}|{d2}|{e2}|{f2}|{g2}|{h2} | ')
    print(f'   |  -- + -- + -- + -- + -- + -- + -- + --  | ')
    print(f'1. | {a1}|{b1}|{c1}|{d1}|{e1}|{f1}|{g1}|{h1} |   <----- White ')
    print(f'\n   {cover * 44} ')
    print(f'       a    b    c    d    e    f    g    h \n')




    if moveNo%2 == 0 :
        isWhite = True
        print('----White to move----')
    else :
        isWhite = False
        print('----Black to move----')



    input_move = input('Enter: ')

    moves = list(input_move)
    print(moves)                            # for debugging

    if input_move.capitalize() == 'Exit' :             # exiting the simulation
        break


    elif input_move in possible_pawn_moves  :        # possible pawn move
        pawn(input_move, moves)


    elif 'O' in moves:                               # checking for castling
        castle(input_move)
       

    elif 'x' in moves:                              # must be capture i.e.  fxd3
        if moves[0] in pieces:
            if 'R' in moves:
                pass
            elif 'N' in moves:
                pass
            elif 'B' in moves:
                pass
            elif 'Q' in moves:
                pass
            elif 'K' in moves:
                pass
        elif moves[0] not in pieces and moves[0] in board_files :
            capture_pawn(moves)
        else :
            print('Invalid command ,code "capture"')


    elif 'R' in moves:                              # must be rook move i.e. Rad4 or Ra3
        rook(moves)            


    else :
        print('Enter Valid notation')
        continue

print(f'Total Moves Played: {moveNo}')