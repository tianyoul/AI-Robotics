from FoxQueue import Queue, PriorityQueue
from FoxStack import Stack

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

def UCSRoute(graph, startVert, goalVert):
    """ This algorithm searches a graph using breadth-first search
    looking for a path from some start vertex to some goal vertex
    It uses a queue to store the indices of vertices that it still
    needs to examine."""

    if startVert == goalVert:
        return []
    q = PriorityQueue()
    cost, element = q.firstElement()
    q.insert(cost, element)
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