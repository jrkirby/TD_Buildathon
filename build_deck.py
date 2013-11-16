
class BuildDeck(object):
	"""docstring for BuildDeck"""
	def __init__(self):
		super(BuildDeck, self).__init__()
		self.cards = []
		self.getNewCards()

	def draw(self, surface):
		self.cards[0].draw()
		self.cards[1].draw()
		self.cards[2].draw() 
		
	#happens every time you select a card
	def getNewCards(self):
		# self.cards[0] = new_random_card()	#todo
		# self.cards[1] = new_random_card()	#todo
		# self.cards[2] = new_random_card()	#todo
		x = 0

	def click(self, x, y):
		if(click_on(self.cards[0], x, y)):
			# todo
			# add to deck self.cards[0]
			self.getNewCards()
		elif(click_on(self.cards[1], x, y)):
			# todo
			# add to deck self.cards[1]
			self.getNewCards()
		elif(click_on(self.cards[2], x, y)):
			# todo
			# add to deck self.cards[2]
			self.getNewCards()

