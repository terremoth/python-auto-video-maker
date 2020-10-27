from robots.choicer import choicer 

def askAndReturnSearchTerm():
	return input("Type a Wikipedia search term: ")
	
def askAndReturnPrefix():
	prefixes = ['Who is', 'What is', 'The history of']
	return choicer(prefixes)