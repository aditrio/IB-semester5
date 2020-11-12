import pdb

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

	def setVolume(self,vol):
		self.volume = vol

	def fillGaloon(self,pour):
		self.volume += pour
		if self.volume > self.capacity:
			self.volume = self.capacity
		
	def fullGaloon(self):
		self.capacity = self.volumeTemp
		self.volume = self.capacityTemp

	def emptyGaloon(self):
		self.capacity = self.capacityTemp
		self.volume = self.volumeTemp

	#need fix
	def pourGaloon(self, pour, otherObject):
		otherObject.fillGaloon(self.volume)
		self.volume -= pour
		if self.volume < 0:
			self.volume = 0
		
		otherObject.checkGaloon()

	def checkGaloon(self):
		if self.volume > self.capacityTemp:
			self.volume = self.capacityTemp
			self.capacity = self.volumeTemp

	def difference(self):
		val = self.capacity - self.volume
		return abs(val)

def update(valA,valB):
	tempList = []
	tempList.append(valA)
	tempList.append(valB)
	if tempList not in visited:
		visited.append(tempList)
		queue.append(tempList)
		
def normalize(a,b,current):
	a.setVolume(current[0])
	b.setVolume(current[1])

visited = []
queue = []
	
a = Galoon(5, 0)
b = Galoon(3, 0)

LNode = []
LNode.append(a.volume)
LNode.append(b.volume)

update(LNode[0],LNode[1])

count = 0

while queue:
	temp =[]
	currentNode = queue.pop(0)

	a.fullGaloon()
	update(a.volume,b.volume)
	temp.append([a.volume,b.volume])
	normalize(a, b, currentNode)
	
	b.fullGaloon()
	update(a.volume,b.volume)
	temp.append([a.volume,b.volume])
	normalize(a, b, currentNode)
	
	a.emptyGaloon()
	update(a.volume,b.volume)
	temp.append([a.volume,b.volume])
	normalize(a, b, currentNode)
	
	b.emptyGaloon()
	update(a.volume,b.volume)
	temp.append([a.volume,b.volume])
	normalize(a, b, currentNode)

	if a.volume != 0 : 
		a.pourGaloon(b.difference(), b)
		update(a.volume,b.volume)
		temp.append([a.volume,b.volume])
		normalize(a, b, currentNode)
		
	if b.volume != 0 : 
		b.pourGaloon(a.difference(), a)
		update(a.volume,b.volume)
		temp.append([a.volume,b.volume])
		normalize(a, b, currentNode)
	
	print("Visited : ")
	print(visited)
	print("Queue : ")
	print(queue)
	print("\n")
	
	# count += 1
	# if count == 9:
		# pdb.set_trace()

	if visited[-1] == [4,3]:
		break
	
	
	
	

