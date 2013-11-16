
class BuildDeck(object):
	"""docstring for BuildDeck"""
	def __init__(self, deck):
		super(BuildDeck, self).__init__()
		self.cards = []
		self.getNewCards()
		self.deck = deck

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

	def click(self, pos):
		if(self.cards[0].click_on(pos.x, pos.y)):
			# todo
			self.deck.add_card(self.cards[0])
			self.getNewCards()
		elif(self.cards[0].click_on(pos.x, pos.y)):
			# todo
			self.deck.add_card(self.cards[1])
			self.getNewCards()
		elif(self.cards[0].click_on(pos.x, pos.y)):
			# todo
			self.deck.add_card(self.cards[2])
			self.getNewCards()

