class Node : 
	def __init__(self, a,b):
		self.data = {

			'a' : a,
			'b' : b		
		}
		
	def cetak(self):
		print(self.data)

	def getData(self):
		return self.data

	def getA(self):
		return self.data['a']

	def getB(self):
		return self.data['b']	

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


def update(volA,volB):
	node = Node(volA,volB)
	if node.getData() not in visited:
		visited.append(node.getData())
		queue.append(node.getData())
		return node

def normalize(a,b,current):
	a.setVolume(current['a'])
	b.setVolume(current['b'])

visited = []
queue = []
	
a = Galoon(5, 0)
b = Galoon(3, 0)

node = update(a.volume,b.volume)

# for q in queue:
# 	print(q.getData())

while queue:
	currentNode = queue.pop(0)

	a.fullGaloon()
	update(a.volume,b.volume)
	normalize(a, b, currentNode)

	b.fullGaloon()
	update(a.volume,b.volume)
	normalize(a, b, currentNode)

	a.emptyGaloon()
	update(a.volume,b.volume)
	normalize(a, b, currentNode)

	b.emptyGaloon()
	update(a.volume,b.volume)
	normalize(a, b, currentNode)

	if a.volume != 0 : 
		a.pourGaloon(b.difference(), b)
		update(a.volume,b.volume)
		normalize(a, b, currentNode)

	if b.volume != 0 : 
		b.pourGaloon(a.difference(), a)
		update(a.volume,b.volume)
		normalize(a, b, currentNode)

	print(visited)

	if a.volume == 4 or b.volume == 4 : 
		break


