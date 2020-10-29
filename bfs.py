

graph = {
	
	'1' : ['2','4'],
	'2' : ['1','3','5','7','8'],
	'3' : ['2','4','9','10'],
	'4' : ['1','3'],
	'5' : ['2','6','7','8'],
	'6' : ['5'],
	'7' : ['2','5','8'],
	'8' : ['2','5','7'],
	'9' : ['3'],
	'10' : ['3'],
}



def _bfs(initial, graph,search):
	visited = []
	queue = [initial]

	while queue : 
		
		node = queue.pop(0)
		if node not in visited:
			visited.append(node)
			neighbours = graph[node]
			for n in neighbours:
				queue.append(n)
			if visited[-1] == search:
				return visited
	



data = _bfs('6',graph,'9')

print(data)		









