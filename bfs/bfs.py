graph =  {'A':set(['B']),
         'B':set(['A','C','D']),
         'C':set(['B','E']),
         'D':set(['B','G','H']),
         'E':set(['C','F','G']),
         'F':set(['E']),
         'G':set(['D','E','I','J']),
         'H':set(['D','J']),
  'I':set(['G'])}
    

def bfs(graph, init, search):
    queue = [[init]]
    visited = set()

    while queue:     
        path = queue.pop(0)
        state = path[-1]
        if state == search:
            return path
        elif state not in visited: 
            for node in graph.get(state, []): 
                newPath = list(path) 
                newPath.append(node) 
                queue.append(newPath) 
            visited.add(state)
        val = len(queue)
        if val == 0:
            print("not found")


init = input("masukan parent node : ")
finish = input("masukan finish node: ")

data = bfs(graph, init, finish)

print("path : ", data)