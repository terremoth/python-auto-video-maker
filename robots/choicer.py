def choicer(itens, prompt = "Choose one option:"):
	print(prompt)
	
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