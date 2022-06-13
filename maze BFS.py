import queue



def createMaze():
    maze = []
    maze.append(["#", "#","O","#"])
    maze.append(["#", " "," ","#"])
    maze.append(["#", " "," ","X"])
    maze.append(["#", "#","#","#"])

    return maze


def createMaze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["X"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])

    return maze


def printMaze(maze, path=""):
    x , y =findStart(maze)
    pos = set()
    for move in path:
        if move == "L":
            x -= 1

        elif move == "R":
            x += 1

        elif move == "U":
            y -= 1

        elif move == "D":
            y += 1
        pos.add((y, x))
    
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if (y, x) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
    
                   
def valid(maze, moves):
    
    x , y =findStart(maze)
    
    for move in moves:
        if move == "L":
            x -= 1

        elif move == "R":
            x += 1

        elif move == "U":
            y -= 1

        elif move == "D":
            y += 1

        if not(0 <= x < len(maze[0]) and 0 <= y < len(maze)):
            return False
        elif (maze[y][x] == "#"):
            return False

    return True


def findEnd(maze, moves):
    
    x , y =findStart(maze)
    
    for move in moves:
        if move == "L":
            x -= 1

        elif move == "R":
            x += 1

        elif move == "U":
            y -= 1

        elif move == "D":
            y += 1

    # print('x:', x)
    # print('y:', y)
   
    
    if maze[y][x] == "X":
        print('###################### final solution ######################')
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False


def findStart(maze):
    for posY,y in enumerate(maze):    
        for posX,x  in enumerate(y):
            if x == "O":
                startX =posX
                startY=posY

                return (startX,startY)


def validMove (pos,path):
    
    if path == '':
        return False
    elif (pos=="L" and  path[-1]=='R') :
        return True
    elif  (pos=="R" and  path[-1]=='L') :
        return True
    elif (pos=="U" and  path[-1]=='D') :
        return True
    elif  (pos=="D" and  path[-1]=='U'): 
        return True

    return False


def maze_solve(maze):
  
    Queue = queue.Queue()
    Queue.put("")
    path = ""
    testPath=''
    itr= 0
    # print((list)(enumerate(maze)))




    while not findEnd(maze, path): 
        itr= itr + 1
        print("itr: ", itr)
        # print("Queue: ", (list)(Queue))
        print("path: ", path)
        print("testPath:", testPath)
        print("testPath size:", len(testPath))
        print("Queue size:", Queue.qsize())
        print()
        printMaze(maze, path)
        print()
        
        # if Queue.qsize()!= 0:
        path = Queue.get() 
        
        for j in ["L", "R", "U", "D"]:
            
            
            if  validMove(j,path):
                continue
            # else: 
            testPath = path + j
            
            
            if valid(maze, testPath):
                Queue.put(testPath)
    
      

# print(dir(Queue)) 


maze_solve(createMaze2())

            