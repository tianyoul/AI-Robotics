from FoxQueue import Queue, PriorityQueue

import LoadGraphs
import GridGraph
import time

# (1) get UCS and A* running, and (2) test them on a set of tasks of differing complexities,
# reporting the time taken, the number of nodes explored, and any differences in the final routes found.
#
# Test your function on all the map graphs we used in the activity in class, the Olin-Rice map, the Macalester campus map, and the grid maps.
# The focus here is on (a) collecting data and (b) summarizing and analyzing the results.
# For each, record the time taken by the algorithm (comment out all print statements within the algorithm before timing it).
# Also, add a counter to each algorithm to count how many nodes are removed from the queue during a run.
# Add code to store the maximum size of the queue at any point during a run.
# Report your results in a tabular form, summarize and explain them in your text, and also analyze and discuss what you found.
# Did it match expectations? What were your expectations? Did it surprise you? If so, why?

olinMap = LoadGraphs.olin
macMap = LoadGraphs.macCampus
grid1Map = GridGraph.GridGraph("grid1.txt")
print("Read in grid1 graph")
grid2Map = GridGraph.GridGraph("grid2.txt")
print("Read in grid2 graph")
grid4Map = GridGraph.GridGraph("grid4.txt")
print("Read in grid4 graph")
grid5Map = GridGraph.GridGraph("grid5.txt")
print("Read in grid5 graph")
grid6Map = GridGraph.GridGraph("grid6.txt")
print("Read in grid6 graph")
mapList = [olinMap, macMap, grid1Map, grid2Map, grid4Map, grid5Map]

startNode = 0
olinGoalNode = 63 -1
macGoalNode = 105 -1
grid1GoalNode = 100 -1
grid2GoalNode = 10000 -1
grid4GoalNode = 5000 -1
grid5GoalNode = 500000 -1
grid6GoalNode = 4000000 -1
GoalNodes = [olinGoalNode, macGoalNode, grid1GoalNode, grid2GoalNode, grid4GoalNode, grid5GoalNode]

# ---------------------------------------------------------------
def UCSRoute(graph, startVert, goalVert):
    nodesRemoved = 0
    maxSize = 0
    if startVert == goalVert:
        return []

    minHeap = PriorityQueue()
    minHeap.insert(0, startVert)
    pred_cost = {}

    visited = set()
    pred = {}
    while not minHeap.isEmpty():
        if minHeap.size > maxSize:
            maxSize = minHeap.size
        nextVert = minHeap.firstElement()  # nextVert = [cost, vert]
        minHeap.delete()
        nodesRemoved = nodesRemoved + 1
        # print("--------------")
        # print("Popping", nextVert)
        if nextVert[1] in visited:
            continue
        else:
            visited.add(nextVert[1])
            if (nextVert[0], nextVert[1]) in pred_cost.keys():
                pred[nextVert[1]] = pred_cost[(nextVert[0], nextVert[1])]
            else:
                pred[nextVert[1]] = None
            if goalVert == nextVert[1]:
                return nodesRemoved, maxSize, reconstructPath(startVert, goalVert, pred)
        neighbors = graph.getNeighbors(nextVert[1])
        for n in neighbors:
            neighNode = n[0]
            edgeCost = n[1]
            if neighNode not in visited:
                minHeap.insert(edgeCost + nextVert[0], neighNode)
                pred_cost[(edgeCost + nextVert[0], neighNode)] = nextVert[1]
    return "NO PATH"

# ---------------------------------------------------------------
def AStarRoute(graph, startVert, goalVert):
    nodesRemoved = 0
    maxSize = 0
    if startVert == goalVert:
        return []

    minHeap = PriorityQueue()
    minHeap.insert(0, startVert)
    pred_cost = {}

    visited = set()
    pred = {}
    while not minHeap.isEmpty():
        if minHeap.size > maxSize:
            maxSize = minHeap.size
        nextVert = minHeap.firstElement()  # nextVert = [cost, vert]
        # print("--------------")
        # print("Popping", nextVert)
        minHeap.delete()
        nodesRemoved = nodesRemoved + 1
        if nextVert[1] in visited:
            continue
        else:
            visited.add(nextVert[1])
            if (nextVert[0], nextVert[1]) in pred_cost.keys():
                pred[nextVert[1]] = pred_cost[(nextVert[0], nextVert[1])]
            else:
                pred[nextVert[1]] = None
            if goalVert == nextVert[1]:
                return nodesRemoved, maxSize, reconstructPath(startVert, goalVert, pred)
        neighbors = graph.getNeighbors(nextVert[1])
        # print('Adding neighbors to the queue: ')
        for n in neighbors:
            neighNode = n[0]
            edgeCost = n[1]
            if neighNode not in visited:
                Gcost = edgeCost + nextVert[0]
                Hcost = graph.heuristicDist(neighNode, goalVert)
                if startVert != nextVert[1]:
                    Gcost = Gcost - graph.heuristicDist(nextVert[1], goalVert)
                Fcost = Gcost + Hcost
                # print('Node ' + str(neighNode) + ' from ' + str(nextVert[1]))
                # print('G cost = ' + str(Gcost) + ' H cost = ' + str(Hcost) + ' F cost =  ' + str(Fcost))
                minHeap.insert(Fcost, neighNode)
                pred_cost[(Fcost, neighNode)] = nextVert[1]
    return "NO PATH"

# ---------------------------------------------------------------
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

# ---------------------------------------------------------------
def timeAndRun(searchAlg, graph, start, goal):
    """Takes ina  search algorithm and runs it, while timing how long it takes. Reports the time
    and the final route (if any), and prints the route."""
    t1 = time.time()
    nodesRemoved, maxSize, route = searchAlg(graph, start, goal)
    t2 = time.time()
    if goal < 10000:
        print("Route found is:")
        print(route)
    print("Time elapsed:", t2 - t1)
    print("nodes removed:", nodesRemoved)
    print("max size:", maxSize)
    if graph.__class__.__name__ == "GridGraph":
        graph.printWithRoute(route)

# ---------------------------------------------------------------
# [olinMap, macMap, grid1Map, grid2Map, grid4Map, grid5Map, grid6Map]

print("---------------------------------------------------------------")
for i in range(5):
    timeAndRun(UCSRoute, mapList[i], startNode, GoalNodes[i])

print("---------------------------------------------------------------")

for j in range(5):
    timeAndRun(AStarRoute, mapList[j], startNode, GoalNodes[j])

# timeAndRun(UCSRoute, grid6Map, startNode, grid6GoalNode)
# timeAndRun(AStarRoute, grid6Map, startNode, grid6GoalNode)