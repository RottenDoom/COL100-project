class Stack:

	def __init__(self):
		self.items = []
	
	def push(self, item):
		self.items.insert(0,item)

	def peek(self):
		if self.items == []:
			return 'Error'
		else:
			return (self.items)[-1]		
		
	def pop(self):
		if self.items == []:
			return 'Error'
		else:
			self.items.pop(0)

	def is_empty(self):
		if self.items == []:
			return True
		else:
			return False
		
	def __str__(self):
		string = ''
		for item in self.items:
			string += ' ' + str(item)
		
	def __len__(self):
		return len(self.items)