from stack import Stack

class SimpleCalculator:
	def __init__(self):
		self.history_stack = Stack()
	def evaluate_expression(self, input_expression):
		# main code
		try:
			if '/' in input_expression:
				input_expression = input_expression.split('/')
				ans = float(input_expression[0]) / float(input_expression[1])
				self.history_stack.push((str(input_expression[0])+'/'+str(input_expression[1]),ans))
				return ans
		
		
			elif '*' in input_expression:
				input_expression = input_expression.split('*')
				ans = float(input_expression[0]) * float(input_expression[1])
				self.history_stack.push((str(input_expression[0])+'*'+str(input_expression[1]),ans))
				return ans 
			

			elif '+' in input_expression:
				input_expression = input_expression.split('+')
				ans = float(input_expression[0]) + float(input_expression[1])
				self.history_stack.push((str(input_expression[0])+'+'+str(input_expression[1]),ans))
				return ans
			

			elif '-' in input_expression:
				input_expression = input_expression.split('-')
				ans = float(input_expression[0]) - float(input_expression[1])
				self.history_stack.push((str(input_expression[0])+'-'+str(input_expression[1]),ans))
				return ans
			
			
			else:
				self.history_stack.push((str(input_expression[0] + str(input_expression[1]) + str(input_expression)),'Error'))
				return 'Error' # For the error cases
		except:
			self.history_stack.push((str(input_expression[0] + str(input_expression[1]) + str(input_expression)),'Error'))
			return 'Error'
	def get_history(self):
		return self.history_stack.items

