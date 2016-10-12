# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best
##        print bestIndices, chosenIndex
##        print legalMoves
##        print chosenIndex
##        print gameState.generatePacmanSuccessor(legalMoves[chosenIndex]).getPacmanPosition()
        "Add more of your code here if you want to"

        #print range(len(scores))
        #print scores,"best score" , bestScore, " at", bestIndices
        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        
##        for b in newFood:
##            if b == True:
##                d+=1


        
##        for row in newFood:
##          for point in row:
##              if  point == True:
##                  food += 1
##        print "range" ,range(len(newFood[0]))
##        print newFood.winfo_height()
##        foodpos = []
##        for row in range(len(newFood[0])):
##            for column in range(len(newFood[0])):
##                #print row, column
##                if newFood[row-1][column-1]:
##                    foodpos.append((row-1,column-1))
##                    food += 1
        
        
        #score= len(foodpos)
        #print newGhostStates[0]
        #print score
        #util.manhattanDistance(newPos, newGhostStates[index].getPosition()) 
##Ghost: (x,y)=(2, 7), Stop
##Ghost: (x,y)=(2, 7), Stop
##Ghost: (x,y)=(2, 7), Stop
##Ghost: (x,y)=(3.0, 7.0), East




        if successorGameState.isWin():
            return 99999999999999999
        
        score =0
        foodpos =[]
        foodpos = successorGameState.getFood().asList()

        
        ghostpos=[]
        ghostpos = successorGameState.getGhostStates()

        d=0
        for  ghost in ghostpos:
            d+= util.manhattanDistance(newPos, ghost.getPosition())

        #print d
        
        if d <= 2:
            score =-99999999
        else:
            score -= 1/(d*10)
        
        

        food_distance =0
        for food in foodpos:
            food_distance += util.manhattanDistance(newPos, food)


##        if not len(foodpos) == 0:
##            score +=20000/len(foodpos)
##        else:
##            score +=50000
##        
        if newPos in foodpos:
            score+=1
        
##        if not food_distance == 0:
##            score += (1/food_distance)*100000
##        else:
##            score+=2000

##        score+= newScaredTimes[0]*1000

        distance2=0
        t=[]
        for food in foodpos:
            t.append(util.manhattanDistance(newPos, food))
            
        if foodpos:
            distance2 = min(t)

        if len(foodpos)!=0 and distance2 != 0:
            score += 150/distance2
        else:
            score +=160

        score -= len(foodpos)*1000

        return score

##        if ghost.scaredTimer > 0:
##        score+= (1/distance2)*ghost.scaredTimer*20000

##
##        right = self.walls.width-2
##
##
##        corner = (23, 1)
##        if newPos != corner:
##            score+= 1/(util.manhattanDistance(newPos, corner)*1000)
##        

        
##        print newPos  
        


##        print d,"score  -> ",score        
##
##        if len(foodpos)==0:
##            score
  
##        print successorGameState
       
##       print newGhostStates

##        print score
##        score = +food
        
#        print score
##        return successorGameState.getScore()



def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"



    
##    actions = []
##    legalMoves = gameState.getLegalActions()
##
##    child =[]
##    for action in actions:
##        child = gameState.generateSuccessor(agentIndex, action):
##
##    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
##    bestScore = max(scores)
##    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
##    chosenIndex = random.choice(bestIndices) # Pick randomly among the best
##        
        
    
##    print num


        ghostno =  gameState.getNumAgents()-1
        value=-float("inf")
        
        for action in gameState.getLegalActions(0):
            pvalue = value
            value = max(value, self.MinValue(gameState.generateSuccessor(0, action), self.depth, ghostno,1))
            
            if value > pvalue:
                Finalaction = action

        if value==-float("inf"):
            return Directions.STOP
        
        return Finalaction


    def MaxValue(self,gameState,depth,ghostno):
        
        if gameState.isWin() or gameState.isLose() or depth == 0:
            return self.evaluationFunction(gameState)
        
        value=-float("inf")        
        for action in gameState.getLegalActions(0):
            value = max(value, self.MinValue(gameState.generateSuccessor(0, action), depth, ghostno,1))
        
        return value
    
    def MinValue(self, gameState,depth,ghostno,agentIndex):

        if gameState.isWin() or gameState.isLose() or depth == 0:
            return self.evaluationFunction(gameState)
        
        value=float("inf")
        for action in gameState.getLegalActions(agentIndex):
            if ghostno == agentIndex:
                value = min(value, self.MaxValue(gameState.generateSuccessor(agentIndex, action), depth-1, ghostno))

            else:
                value = min(value, self.MinValue(gameState.generateSuccessor(agentIndex, action), depth, ghostno,agentIndex+1))

        return value
    

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        ghostno =  gameState.getNumAgents()-1
        value=-float("inf")
        alpha =-float("inf")
        beta =float("inf")

        
        for action in gameState.getLegalActions(0):
            pvalue = value
            value = max(value, self.MinValue(gameState.generateSuccessor(0, action), self.depth, ghostno,1,alpha,beta))
            
            if value > pvalue:
                Finalaction = action

            alpha =max(alpha,value)

        if value==-float("inf"):
            return Directions.STOP
        
        return Finalaction


    def MaxValue(self,gameState,depth,ghostno,alpha,beta):
        
        if gameState.isWin() or gameState.isLose() or depth == 0:
            return self.evaluationFunction(gameState)
        
        value=-float("inf")        
        for action in gameState.getLegalActions(0):
            value = max(value, self.MinValue(gameState.generateSuccessor(0, action), depth, ghostno,1,alpha,beta))
            if value >beta:
                return value
            alpha =max(alpha,value)
        
        return value
    
    def MinValue(self, gameState,depth,ghostno,agentIndex,alpha,beta):

        if gameState.isWin() or gameState.isLose() or depth == 0:
            return self.evaluationFunction(gameState)
        
        value=float("inf")
        for action in gameState.getLegalActions(agentIndex):
            if ghostno == agentIndex:
                value = min(value, self.MaxValue(gameState.generateSuccessor(agentIndex, action), depth-1, ghostno,alpha,beta))

            else:
                value = min(value, self.MinValue(gameState.generateSuccessor(agentIndex, action), depth, ghostno,agentIndex+1,alpha,beta))


            if value < alpha:
                return value
            beta =min(beta,value)

            

        return value

    

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        ghostno =  gameState.getNumAgents()-1
        value=-float("inf")
        
        for action in gameState.getLegalActions(0):
            pvalue = value
            value = max(value, self.Chancevalue(gameState.generateSuccessor(0, action), self.depth, ghostno,1))
            
            if value > pvalue:
                Finalaction = action

        if value==-float("inf"):
            return Directions.STOP
        
        return Finalaction


    def MaxValue(self,gameState,depth,ghostno):
        
        if gameState.isWin() or gameState.isLose() or depth == 0:
            return self.evaluationFunction(gameState)
        
        value=-float("inf")        
        for action in gameState.getLegalActions(0):
            value = max(value, self.Chancevalue(gameState.generateSuccessor(0, action), depth, ghostno,1))
        
        return value
    
    def Chancevalue(self, gameState,depth,ghostno,agentIndex):

        if gameState.isWin() or gameState.isLose() or depth == 0:
            return self.evaluationFunction(gameState)
        
        value=[]
        for action in gameState.getLegalActions(agentIndex):
            if ghostno == agentIndex:
                value.append(self.MaxValue(gameState.generateSuccessor(agentIndex, action), depth-1, ghostno))

            else:
                value.append(self.Chancevalue(gameState.generateSuccessor(agentIndex, action), depth, ghostno,agentIndex+1))
        sum = 0.0
        for v in value:
            sum +=v
        avg = sum /len(value)
        
        return avg

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"

##        successorGameState = currentGameState.generatePacmanSuccessor(action)

    successorGameState = currentGameState
    newPos = successorGameState.getPacmanPosition()
    newFood = successorGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    
    

    
    score =0
    foodpos =[]
    foodpos = successorGameState.getFood().asList()

    
    ghostpos=[]
    ghostpos = successorGameState.getGhostStates()
    

    d=0
    for  ghost in ghostpos:
        d+= util.manhattanDistance(newPos, ghost.getPosition())


    
    if d <= 2:
        score =-99999999
    else:
        score -= 10.0/d
    
    

    food_distance =0
    for food in foodpos:
        food_distance += util.manhattanDistance(newPos, food)


    if newPos in foodpos:
        score+=10000


    distance2=0
    t=[]

    
    for food in foodpos:
        t.append(util.manhattanDistance(newPos, food))

    if foodpos:
        distance2 = min(t)

    if len(foodpos) >1:
        distance2 +=max(t)
        
    if len(foodpos)!=0:
        score += 15.5/(1+distance2)
    else:
        score +=250/(1+len(foodpos))

    
    score -= len(foodpos)*len(foodpos)*len(foodpos)*len(foodpos)

    score +=1.0/(1+(distance2))

    
    if newScaredTimes[0] >=20:
        score += 2
        

    return score   



# Abbreviation
better = betterEvaluationFunction

