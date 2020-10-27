#  -*- coding: utf-8 -*-

import Algorithmia
from dotenv import load_dotenv
import os

load_dotenv()

def robot():
	
	def fetchContentFromWikipedia():
		client = Algorithmia.client(os.getenv("ALGORITHMIA_KEY"))
		wikipediaAlgorithm = client.algo('web/WikipediaParser/0.1.2')
		wikipediaResponse = wikipediaAlgorithm.pipe(content["searchTerm"])
		wikipediaContent = wikipediaResponse.result
		content["sourceContentOriginal"] = wikipediaContent
		
	def sanitizeContent():
		
		def getNotEmptyContent(text):
			return len(text.strip()) != 0
		
		def removeBlankLines(text):
			allLines = text.split('\n')
			filteredContent = list(filter(lambda txt: len(txt.strip()) > 0, allLines))
			return filteredContent
		
		withoutBlankLines = removeBlankLines(content["sourceContentOriginal"])
		print(withoutBlankLines)
		return withoutBlankLines
		
	#def breakIntoSentences(content)
	
	return content
