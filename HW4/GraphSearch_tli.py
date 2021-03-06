###############################################
# Breadth-First and Depth-First Search on a graph
# Susan Fox
# Spring 2014
# Spring 2016: This Homework version also contains working
#              implementations of UCS and A*


from FoxQueue import Queue, PriorityQueue
from FoxStack import Stack


# ---------------------------------------------------------------
def BFSRoute(graph, startVert, goalVert):
    """ This algorithm searches a graph using breadth-first search
    looking for a path from some start vertex to some goal vertex
    It uses a queue to store the indices of vertices that it still
    needs to examine."""

    if startVert == goalVert:
        return []
    q = Queue()
    q.insert(startVert)
    visited = {startVert}
    pred = {startVert: None}
    while not q.isEmpty():
        nextVert = q.firstElement()
        q.delete()
        neighbors = graph.getNeighbors(nextVert)
        for n in neighbors:
            if type(n) != int:
                # weighted graph, strip and ignore weights
                n = n[0]
            if n not in visited:
                visited.add(n)
                pred[n] = nextVert        
                if n != goalVert:
                    q.insert(n)
                else:
                    return reconstructPath(startVert, goalVert, pred)
    return "NO PATH"






# ---------------------------------------------------------------
def DFSRoute(graph, startVert, goalVert):
    """This algorithm searches a graph using depth-first search
    looking for a path from some start vertex to some goal vertex
    It uses a stack to store the indices of vertices that it still
    needs to examine."""
    
    if startVert == goalVert:
        return []
    s = Stack()
    s.push(startVert)
    visited = {startVert}
    pred = {startVert: None}
    while not s.isEmpty():
        nextVert = s.top()
        s.pop()
        neighbors = graph.getNeighbors(nextVert)
        for n in neighbors:
            if type(n) != int:
                # weighted graph, strip and ignore weights
                n = n[0]
            if n not in visited:
                visited.add(n)
                pred[n] = nextVert        
                if n != goalVert:
                    s.push(n)
                else:
                    return reconstructPath(startVert, goalVert, pred)
    return "NO PATH"



# ---------------------------------------------------------------
def UCSRoute(graph, startVert, goalVert):

    if startVert == goalVert:
        return []

    minHeap = PriorityQueue()
    minHeap.insert(0, startVert)
    pred_cost = {}

    visited = set()
    pred = {}
    while not minHeap.isEmpty():
        nextVert = minHeap.firstElement() #nextVert = [cost, vert]
        minHeap.delete()
        print("--------------")
        print("Popping", nextVert)
        if nextVert[1] in visited:
            continue
        else:
            visited.add(nextVert[1])
            if (nextVert[0], nextVert[1]) in pred_cost.keys():
                pred[nextVert[1]] = pred_cost[(nextVert[0], nextVert[1])]
            else:
                pred[nextVert[1]] = None
            if goalVert == nextVert[1]:
                return reconstructPath(startVert, goalVert, pred)
        neighbors = graph.getNeighbors(nextVert[1])
        for n in neighbors:
            neighNode = n[0]
            edgeCost = n[1]
            if neighNode not in visited:
                minHeap.insert(edgeCost + nextVert[0], neighNode)
                pred_cost[(edgeCost + nextVert[0], neighNode)] = nextVert[1]

    return "NO PATH"



# ---------------------------------------------------------------
def dijkstras(graph, startVert, goalVert):
    """ This algorithm searches a graph using Dijkstras algorithm to find
    the shortest path from every point to a goal point (actually
    searches from goal to every point, but it's the same thing.
    It uses a priority queue to store the indices of vertices that it still
    needs to examine.
    It returns the best path frmo startVert to goalVert, but otherwise
    startVert does not play into the search."""

    if startVert == goalVert:
        return []
    q = PriorityQueue()
    visited = set()
    pred = {}
    cost = {}
    for vert in graph.getVertices():
        cost[vert] = 1000.0
        pred[vert] = None
        q.insert(cost[vert], vert)
    visited.add(goalVert)
    cost[goalVert] = 0
    q.update(cost[goalVert], goalVert)
    while not q.isEmpty():
        (nextCTG, nextVert) = q.firstElement()
        q.delete()
        visited.add(nextVert)
        print("--------------")
        print("Popping", nextVert, nextCTG)
        neighbors = graph.getNeighbors(nextVert)
        for n in neighbors:
            neighNode = n[0]
            edgeCost = n[1]
            if neighNode not in visited and\
               cost[neighNode] > nextCTG + edgeCost:
                print("Node", neighNode, "From", nextVert)
                print("New cost =", nextCTG + edgeCost)
                cost[neighNode] = nextCTG + edgeCost
                pred[neighNode] = nextVert
                q.update( cost[neighNode], neighNode )
    for vert in graph.getVertices():
        bestPath = reconstructPath(goalVert, vert, pred)
        bestPath.reverse()
        print("Best path from ", vert, "to", goalVert, "is", bestPath)
    finalPath = reconstructPath(goalVert, startVert, pred)
    finalPath.reverse()
    return finalPath



# ---------------------------------------------------------------
def AStarRoute(graph, startVert, goalVert):

    if startVert == goalVert:
        return []

    minHeap = PriorityQueue()
    minHeap.insert(0, startVert)
    pred_cost = {}

    visited = set()
    pred = {}
    while not minHeap.isEmpty():
        nextVert = minHeap.firstElement() #nextVert = [cost, vert]
        print("--------------")
        print("Popping", nextVert)
        minHeap.delete()
        if nextVert[1] in visited:
            continue
        else:
            visited.add(nextVert[1])
            if (nextVert[0], nextVert[1]) in pred_cost.keys():
                pred[nextVert[1]] = pred_cost[(nextVert[0], nextVert[1])]
            else:
                pred[nextVert[1]] = None
            if goalVert == nextVert[1]:
                return reconstructPath(startVert, goalVert, pred)
        neighbors = graph.getNeighbors(nextVert[1])
        print('Adding neighbors to the queue: ')
        for n in neighbors:
            neighNode = n[0]
            edgeCost = n[1]
            if neighNode not in visited:
                Gcost = edgeCost + nextVert[0]
                Hcost = graph.heuristicDist(neighNode, goalVert)
                if startVert != nextVert[1]:
                    Gcost = Gcost - graph.heuristicDist(nextVert[1], goalVert)
                Fcost = Gcost + Hcost
                print('Node ' + str(neighNode) + ' from ' + str(nextVert[1]))
                print('G cost = ' + str(Gcost) + ' H cost = ' + str(Hcost) + ' F cost =  ' + str(Fcost))
                minHeap.insert(Fcost, neighNode)
                pred_cost[(Fcost, neighNode)] = nextVert[1]

    return "NO PATH"
    


# ---------------------------------------------------------------
# This function is used by all the algorithms in this file to build
# the path after the fact

def reconstructPath(startVert, goalVert, preds):
    """ Given the start vertex and goal vertex, and the table of
    predecessors found during the search, this will reconstruct the path 
    from start to goal"""

    path = [goalVert]
    p = preds[goalVert]
    while p != None:
        path.insert(0, p)
        p = preds[p]
    return path

