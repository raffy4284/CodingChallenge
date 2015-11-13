import random
class Card:
  __suit = None
  __card_number = None
  def __init__(self,suit,card_number):
    self.set_suit(suit)
    self.set_card_number(card_number)
  def set_suit(self,suit):
    if suit not in ["spades","hearts","diamonds","clubs"]:
      print "Not a proper suit\nAuto setting to spades!"
      self.__suit = "spades"
    else:
      self.__suit = suit
  def set_card_number(self,card_number):
    if card_number not in ["ace",'1','2','3','4','5','6','7','8','9','J','K','Q']:
      print "Not a proper card number!\nAuto setting to ace"
      self.__card_number = "ace" 
    else:
      self.__card_number = card_number
  def get_card_number(self):
    return self.__card_number
  def get_suit(self):
    return self.__suit
  def __str__(self):
    print "Suit: "+self.get_suit()+", Card Number: "+self.get_card_number()
  def __repr__(self):
    return "Suit: "+self.get_suit()+", Card Number: "+self.get_card_number()

class Deck:
  __card_list = None
  __card_index = 0
  def __init__(self):
    self.__card_list = list()
    str_types = ["spades","hearts","diamonds","clubs"]
    for type in str_types:
      self.__card_list.append(Card(type,"ace"))
      for number in range(1,10):
        self.__card_list.append(Card(type,str(number)))
      self.__card_list.append(Card(type,"J"))
      self.__card_list.append(Card(type,"K"))
      self.__card_list.append(Card(type,"Q"))
    self.__card_index=51
  def Shuffle(self):
    random.shuffle(self.__card_list)
    self.__card_index=51
  def GetNextCard(self):
    try:
      return_card = self.__card_list[self.__card_index]
      self.__card_index-=1
    except:
      print "No more cards on stack!"
      return_card = None
    return return_card

def driver():
  print "Calling Driver to test functions!"
  Deck_of_cards = Deck()
  cards_seen = set()
  current_card = Deck_of_cards.GetNextCard()
  while current_card != None:
    cards_seen.add(current_card)
    current_card = Deck_of_cards.GetNextCard()
  print "Testing GetNextCard()..."
  if len(cards_seen) != 52:
    print "GetNextCard() is broken!"
    return "GetNextCard() failed"
  else:
    print "GetNextCard() has successfully seen all 52!"
  print "Testing Shuffle..."
  first_set = list()
  second_set = list()
  Deck_of_cards.Shuffle()
  current_card = Deck_of_cards.GetNextCard()
  while current_card != None:
    first_set.append(current_card)
    current_card = Deck_of_cards.GetNextCard()
  Deck_of_cards.Shuffle()
  current_card = Deck_of_cards.GetNextCard()
  while current_card != None:
    second_set.append(current_card)
    current_card = Deck_of_cards.GetNextCard()
  uniqueness = False
  for i in range(0,52):
    print "first_set "+first_set[i].get_card_number()+" "+first_set[i].get_suit()
    print "second_set "+second_set[i].get_card_number()+" "+second_set[i].get_suit()

    if first_set[i].get_card_number() != second_set[i].get_card_number() and first_set[i].get_suit() != second_set[i].get_suit():
      uniqueness = True
  if uniqueness:
    print "All cards were of different ordering!"
  else:
    print "Not shuffled...slimmest chance that calling shuffle twice returned the same ordering of cards!"
    return "Shuffle Failed"
  return "All Tests Passed!"
  
print(driver())
