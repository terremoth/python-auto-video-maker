def choicer(itens):
	print("Choose one option")
	
	for item in itens:
		index = itens.index(item)
		print(f"[{index}] ", item)
	
	try:		
		choice = int(input("Choice: "))
	except:
		print(f"Only numbers from 0 to {len(itens)-1} are allowed")
		return choicer(itens)
		
	if choice < 0 or choice > len(itens)-1:
		print("This choice does not exist")
		return choicer(itens)
	else:
		choosed = itens[choice]
		print(f" You have choosed {choosed}")
		return choosed

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