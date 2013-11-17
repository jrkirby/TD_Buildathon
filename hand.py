
STARTING_CARDS = 4


class Hand(object):
	"""docstring for Hand"""
	def __init__(self, deck):
		super(Hand, self).__init__()
		self.deck = deck

		self.cards = []

		for i in range(STARTING_CARDS):
			self.add_card(self.deck.draw_card())

	def add_card(self, card, surface):
		self.cards.append(card)
		card.position = index_to_pos(i)

# returns card at index 
	def select_card(self, index):
		return self.cards[index]

	def remove_card(self, index):
		self.cards.remove(index)
		for i in range(len(self.cards)):
			card = self.cards[i]
			card.position = index_to_pos(i)

	def draw(self, surface):
		for i in range(len(self.cards)):
			card = self.cards[i]
			card.draw(surface)

	def index_to_pos(index, surface):
		y = surface.get_height() - 133
		x = index * 100
		return (x,y)
