class Test:
			


	mylistQ = ["please describe what you find positive or negative about a vacation by the beach or among the hills",
		  "what is your approach towards risk taking",
		  "how do you respond towards being placed in unfamiliar situations ",
		  "to what extent do you find yourself comfortable with leaving your comfort zones",
		  "how would you describe the role played by the people around you in your life ",
		  "to what extent are your decisions influenced by some form of social consequences ",
		  "what would your first instinct be in the eventuality of a challenge ",
		  "what would your headspace be like when things don't go your way" ]

	
	mylistA = []

	def something(mylistQ, mylistA):
		
		#self.mylistQ = mylistQ 		
		for words in mylistQ[0:2]:
			#mylistA.append(words)
			print words	
			#print mylistQ[0]
			answer = raw_input("Eneter your answer :")
			mylistA.append(answer)
			#print answer 
		return
		
	
	
	
	#test = Test()
	something(mylistQ, mylistA)
	#wtv()
	
	for i in mylistA:
			print i	


