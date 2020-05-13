from choicer import choicer

def start():

	def askAndReturnSearchTerm():
		return input("Type a Wikipedia search term: ")
		
	def askAndReturnPrefix():
		prefixes = ['Who is', 'What is', 'The history of']
		return choicer(prefixes)
					
	content = {}
	content["searchTerm"] = askAndReturnSearchTerm()	
	content["prefix"] = askAndReturnPrefix()	
	
	print(content)

start()