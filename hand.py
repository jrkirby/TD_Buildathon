
class Hand(object):
	"""docstring for Hand"""
	def __init__(self, deck):
		super(Hand, self).__init__()
		self.deck = deck

		self.cards = []

		for(range(STARTING_CARDS)):
			self.add_card(self.deck.draw_card())

	def add_card(card):
		self.cards.append(card)

# returns card at index 
	def select_card(index):
		return self.cards[index]

	def remove_card(index):
		self.cards.remove(index)

	def draw():
		for(i in range(len(self.cards))):
			card = self.cards[i]
			card.draw(Hand.index_to_offset(i))

	def index_to_offset(index):
		y = screen_size - 
		return (x,y)
