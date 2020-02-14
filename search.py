# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
"""
num_hours_i_spent_on_this_assignment = 26 hours
"""
#
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
<Your feedback goes here>
I find the course very enjoyable and informative. I would appreciate it 
it could get more in depth with the coding aspects of the course as it would 
help support the theory we are covering. Posting lecture notes before class
would be a huge help for us. I found A* algorithm to be very interesting. 
The topics I had trouble understanding would be admissibility, heuristics and consistency.
"""
#####################################################
#####################################################

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Q1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print ( problem.getStartState() )
    You will get (5,5)

    print (problem.isGoalState(problem.getStartState()) )
    You will get True

    print ( problem.getSuccessors(problem.getStartState()) )
    You will get [((x1,y1),'South',1),((x2,y2),'West',1)]
    """
    "*** YOUR CODE HERE ***"
    from util import Stack
    fringe = Stack()
    visited = []
    fringe.push((problem.getStartState(), []))
    while not fringe.isEmpty():
        pState, pDir = fringe.pop()
        
        if(pState in visited):
            continue
        
        if(problem.isGoalState(pState)):
            return pDir
        
        visited.append(pState)
        
        successors = problem.getSuccessors(pState)
        for child, direction, cost in successors:
            if(child in visited):
                continue
            tempPath = pDir+[direction]
            fringe.push((child, tempPath))
    return []
            
   
    
           
           
            
        
        
def breadthFirstSearch(problem):
    """
    Q1.2
    Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    """
    Nodes is a list of dictionary to store the current node, previous nodes,
    action, and if the node is expanded/traveled
    """
    from util import Queue
    fringe = Queue()
    visited = []
    fringe.push((problem.getStartState(), []))
    while not fringe.isEmpty():
        pState, pDir = fringe.pop()
        
        if(pState in visited):
            continue
        
        if(problem.isGoalState(pState)):
            return pDir
        
        visited.append(pState)
        
        successors = problem.getSuccessors(pState)
        for child, direction, cost in successors:
            if(child in visited):
                continue
            tempPath = pDir+[direction]
            fringe.push((child, tempPath))
    return []
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Q1.3
    Search the node that has the lowest combined cost and heuristic first."""
    """Call heuristic(s,problem) to get h(s) value."""
    "*** YOUR CODE HERE ***"
   
    from util import PriorityQueue
    fringe = PriorityQueue()
    visited = []
    fringe.push((problem.getStartState(),[], 0), 0)
    while not fringe.isEmpty():
        cState, cMoves, cCost = fringe.pop()
        
        if(cState in visited):
            continue
        
        if(problem.isGoalState(cState)):
            return cMoves
        
        visited.append(cState)
        
        successors = problem.getSuccessors(cState)
        for child, direction, cost in successors:
            if(child in visited):
                continue
            HeuVal = heuristic(child, problem)
            tempPath = cMoves + [direction]
            fringe.push((child, tempPath, cCost + cost), cCost+cost+HeuVal)
    return []

def priorityQueueDepthFirstSearch(problem):
    """
    Q1.4a.
    Reimplement DFS using a priority queue.
    """
    "*** YOUR CODE HERE ***"
    
   
    from util import PriorityQueue
    fringe = PriorityQueue()
    visited = []
    fringe.push((problem.getStartState(), []), 0)
    while not fringe.isEmpty():
        pState, pDir = fringe.pop()
        
        if(pState in visited):
            continue
        
        if(problem.isGoalState(pState)):
            return pDir
        
        visited.append(pState)
        
        successors = problem.getSuccessors(pState)
        for child, direction, cost in successors:
            if(child in visited):
                continue
            tempPath = pDir+[direction]
            fringe.push((child, tempPath), cost)
    return []
    

def priorityQueueBreadthFirstSearch(problem):
    """
    Q1.4b.
    Reimplement BFS using a priority queue.
    """
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    fringe = PriorityQueue()
    visited = []
    fringe.push((problem.getStartState(), []), 0)
    while not fringe.isEmpty():
        pState, pDir = fringe.pop()
        
        if(pState in visited):
            continue
        
        if(problem.isGoalState(pState)):
            return pDir
        
        visited.append(pState)
        
        successors = problem.getSuccessors(pState)
        for child, direction, cost in successors:
            if(child in visited):
                continue
            tempPath = pDir+[direction]
            fringe.push((child, tempPath), cost)
    return []
    

#####################################################
#####################################################
# Discuss the results of comparing the priority-queue
# based implementations of BFS and DFS with your original
# implementations.

"""
<Your discussion goes here>
"""
"""
DFS:
Stack implementation: expands 146 nodes
Priority Queue implementation: expands 269 nodes

Stack implementation is better as it expands lesser nodes and has a O(1) time 
complexity for push and pop vs a O(log n) time complexity for push and pop for Priority Queues

BFS:
Queue implementation: expands 269 nodes
Priority Queue implementation: expands 269 nodes

Both implementations expands the same number of nodes but Queue implementation 
is superior as it has a O(1) time 
complexity for push and pop vs a O(log n) time complexity for push and pop for Priority Queues
"""
''
''


#####################################################
#####################################################



# Abbreviations (please DO NOT change these.)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
bfs2 = priorityQueueBreadthFirstSearch
dfs2 = priorityQueueDepthFirstSearch