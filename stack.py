
class Stack:
	def __init__(self):
		self.stack = list()

	def push(self,element):
		self.stack.append(element)

	def pop(self):
		r = self.stack[-1]
		del self.stack[-1]
		return r

	def top(self):
		return self.stack[-1]

	def display(self):
		return self.stack


def main():
	s = Stack()
	for i in range(10):
		s.push(i)
	print('Stack: {}'.format(s.display()))
	print('Stack top: {}'.format(s.top()))
	s.pop()
	print('Stack top: {}'.format(s.top()))


if __name__ == '__main__':
		main()	
