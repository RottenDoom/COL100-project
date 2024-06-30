from simple_calculator import SimpleCalculator
from stack import Stack

class AdvancedCalculator(SimpleCalculator):
	def __init__(self):
		super().__init__()
		

	def evaluate_expression(self, input_expression):
		list_tokens = self.tokenize(input_expression)
		ans =  self.evaluate_list_tokens(list_tokens)
		
		self.history_stack.push((input_expression,ans))
		return ans
	
		 
	def tokenize(self, input_expression):
		list_tokens = []
		current_token = ""
		for char in input_expression:
			if char == ' ':
				continue
			elif char.isdigit():
				current_token += char
			elif char == '.':
				current_token += char
			elif current_token != "":
				if '.' in current_token:
					list_tokens.append(float(current_token))
				else:
					list_tokens.append(int(current_token))
				current_token = ""
				list_tokens.append(char)
			else:
				list_tokens.append(char)
		if current_token != "":
			if '.' in current_token:
				list_tokens.append(float(current_token))
			else:
				list_tokens.append(int(current_token))
		return list_tokens


	def check_brackets(self, list_tokens):
		brackets = dict(('()', '{}'))
		checker = '{()}'
		stack = []
		for char in list_tokens:
			if str(char) in checker:
				if char == '{':
					if '(' in stack:
						return False
					else:
						stack.append(char)
				elif char == '(':
					stack.append(char)
				else:
					if len(stack) == 0 or char != brackets[stack.pop()]:
						return False
			else:
				pass
		return len(stack) == 0
	

	def evaluate_list_tokens(self, list_tokens):
		token= ''
		calculator = SimpleCalculator()
		check = True
		for char in list_tokens:
			token= token + str(char)
		for item in list_tokens:
			if isinstance(item, str) and any(bracket in item for bracket in ['{','}','(',')']):
				check = False
				break
		if len(list_tokens) == 1 and type(list_tokens[0]) == float:
			return list_tokens[0]
		if check:
			if len(list_tokens) > 3:
				new_char = ''
				for i in range(len(list_tokens[:3])):
					new_char += str(list_tokens[i])
				new_ans = calculator.evaluate_expression(new_char)
				new_list_tokens = [new_ans] + list_tokens[3:]
				return self.evaluate_list_tokens(new_list_tokens)
			return calculator.evaluate_expression(token)
		else:
			par_check = self.check_brackets(list_tokens)
			if not par_check:
				return 'Error'
			else:
				index = 0
				par_expression = ''
				cal_value = None
				for i in range(len(list_tokens)):
					if str(list_tokens[i]) in ')}':
						index = i
						break
				for i in range(index - 3,index):
					par_expression += str(list_tokens[i])
				cal_value = calculator.evaluate_expression(par_expression)
				if index - 4 == 0:					
					new_list_token = [cal_value] + list_tokens[index + 1:]
				elif index == len(list_tokens) - 1:					
					new_list_token = list_tokens[:index - 4] + [cal_value]
				elif (index != len(list_tokens) - 1) or (index - 4 != 0):
					new_list_token = list_tokens[:index - 4] + [cal_value] + list_tokens[index + 1:]
				else:
					new_list_token = [cal_value]
				return self.evaluate_list_tokens(new_list_token)
				

	def get_history(self):
		return self.history_stack.items

