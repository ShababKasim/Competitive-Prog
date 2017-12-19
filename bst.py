import random
class Node():
	def __init__(self,value):
		self.value = value
		self.leftChild = None
		self.rightChild = None

	def insert(self,data):
		if self.value == data:
			return False
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.insert(data)
			else:
				self.leftChild = Node(data)
				return True
		else:
			if self.rightChild:
				return self.rightChild.insert(data)
			else:
				self.rightChild = Node(data)
				return True

	def preOrder(self,her='r'):
		if self:
			printString = her+'('+str(self.value)+')'
			print(printString, end=' ')
			if self.leftChild:
				self.leftChild.preOrder('L')
			if self.rightChild:
				self.rightChild.preOrder('R')

	def postOrder(self):
		if self:
			if self.leftChild:
				self.leftChild.postOrder()
			if self.rightChild:
				self.rightChild.postOrder()
			print(str(self.value), end=' ')

	def inOrder(self):
		if self:
			if self.leftChild:
				self.leftChild.postOrder()
			print(str(self.value), end=' ')
			if self.rightChild:
				self.rightChild.postOrder()


class Tree():
	def __init__(self):
		self.root = None

	def insert(self,data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True

	def find(self,data):
		if self.root:
			return self.root.find(data)
		else:
			return False

	def preOrder(self):
		if self.root is not None:
			print("Pre-Order")
			self.root.preOrder()

	def postOrder(self):
		if self.root is not None:
			print("Post-Order")
			self.root.postOrder()

	def inOrder(self):
		if self.root is not None:
			print("In-Order")
			self.root.inOrder()


def main():
	bst = Tree()
	dataSet = list(range(10))
	random.shuffle(dataSet)
	print(dataSet)
	for data in dataSet:
		bst.insert(data)
	bst.preOrder()

if __name__ == '__main__':
	main()