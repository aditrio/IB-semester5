class Galoon : 

	capacityTemp = 0
	volumeTemp = 0

	def __init__(self, capacity, volume):
		self.capacity = capacity
		self.volume  = volume
		self.capacityTemp = capacity
		self.volumeTemp = volume

	# def normalize(val):
	# 	self.volume = val

	def setVolume(self,vol):
		self.volume = vol

	# def fillGaloon(self, volume):
	# 	self.capacity -= volume
	# 	self.volume = volume
	# 	self.checkGaloon()

	def fullGaloon(self):
		self.capacity = self.volumeTemp
		self.volume = self.capacityTemp

	def emptyGaloon(self):
		self.capacity = self.capacityTemp
		self.volume = self.volumeTemp

	def pourGaloon(self, volume, otherObject):
		self.volume -= volume
		self.capacity += volume
		otherObject.fullGaloon()
		otherObject.checkGaloon()

	def checkGaloon(self):
		if self.volume > self.capacityTemp:
			self.volume = self.capacityTemp
			self.capacity = self.volumeTemp

	def difference(self):
		val = self.capacity - self.volume
		return abs(val)



def updateGraph(queue,graph,i) : 
	a.fullGaloon()
	graph[i].append([a.volume, b.volume])
	b.fullGaloon()
	graph[i].append([a.volume, b.volume])
	a.pourGaloon(b.difference(), b)
	graph[i].append([a.volume, b.volume])
	print(graph)




graph = {}

a = Galoon(5, 0)
b = Galoon(3, 0)

graph[0] = [[a.volume,b.volume]]
visited = []
queue = [graph[0]]

while queue:
	node = queue.pop(0)
	if node not in visited : 
		visited.append(node)
		updateGraph(queue, graph,0)
		break


print(visited)



